#!/usr/bin/env python3
"""
answers.py — create, update, inspect and validate the ECD Checklist answers document.

The answers document (answers.json) is the single source of truth that
render_outputs.py turns into Markdown / HTML / DOCX / PDF. One record per
Checklist question id (see references/ecd_checklist_schema_v1.json):

  {"id": "S7.2", "choice": "Yes", "text": null, "list": [], "links": ["https://..."], "image": null,
   "status": "verified", "confidence": "high",
   "evidence": [{"source": "identifiers.org", "url": "...", "snippet": "...", "retrieved": "..."}],
   "hint": null, "notes": null}

status:
  pending            not yet assessed
  verified           answered from evidence that directly shows the fact (every Yes cites >= 1 evidence URL)
  inferred           answered/drafted from indirect evidence; applicant must review (drafted text, bands)
  needs_applicant    only the applicant can answer (may carry a hint)
  applicant_provided answered by the applicant during Q&A
  not_found          registry/website queries succeeded and found nothing (supports a "No")
  query_failed       the lookup itself failed; cannot support "No" -> ask the applicant

Subcommands:
  init      --answers F --name N --url U [--reapplication] [--community C]
  set       --answers F --id QID [--choice C] [--text T] [--list-item X ...] [--link L ...] [--image PATH]
            [--status S] [--confidence C] [--evidence-json JSON] [--hint H] [--notes N]
  patch     --answers F --patch patch.json      (object {qid: {field: value}} or list of records; merges)
  pending   --answers F                         (compact list for the applicant Q&A)
  validate  --answers F [--strict]              (exit 1 on errors; --strict also fails on unresolved items)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import iter_questions, load_json, load_reference_lists, load_schema, now_iso, today, write_json  # noqa: E402

STATUSES = ["pending", "verified", "inferred", "needs_applicant", "applicant_provided", "not_found", "query_failed"]
UNRESOLVED = {"pending", "needs_applicant", "query_failed"}
CONFIDENCE = [None, "high", "medium", "low"]


def option_values(schema: dict, option_set: str) -> list[str]:
    spec = schema["option_sets"].get(option_set)
    if isinstance(spec, dict) and spec.get("from_reference_list"):
        return [c["name"] for c in (load_reference_lists().get(spec["from_reference_list"]) or {}).get("items", [])]
    return spec or []


def blank_record(q: dict) -> dict:
    return {"id": q["id"], "choice": None, "text": None, "list": [], "links": [], "image": None,
            "status": "pending", "confidence": None, "evidence": [], "hint": None, "notes": None}


def cmd_init(args) -> None:
    schema = load_schema()
    path = Path(args.answers)
    if path.exists() and not args.force:
        sys.exit(f"{path} exists; pass --force to overwrite")
    answers = {}
    for section, q in iter_questions(schema):
        answers[q["id"]] = blank_record(q)
    url = args.url if "://" in args.url else f"https://{args.url}"
    answers["APP.resource_name"].update(text=args.name, status="verified", confidence="high",
                                        evidence=[{"source": "input", "url": None, "snippet": "provided by user"}])
    answers["APP.resource_url"].update(links=[url], status="verified", confidence="high",
                                       evidence=[{"source": "input", "url": url, "snippet": "provided by user"}])
    answers["APP.date_submitted"].update(text=today(), status="inferred", confidence="medium",
                                         hint="Set to the actual submission date before sending.")
    if args.community:
        answers["APP.community"].update(choice=args.community, status="applicant_provided", confidence="high")
    doc = {"meta": {"schema_id": schema["schema_id"], "schema_version": schema["schema_version"],
                    "checklist_doi": schema["source"]["checklist"]["doi"], "process_doi": schema["source"]["process"]["doi"],
                    "resource_name": args.name, "resource_url": url, "reapplication": bool(args.reapplication),
                    "created": now_iso(), "updated": now_iso(), "generator": "ECD Agent Skill"},
           "answers": answers}
    write_json(path, doc)
    print(json.dumps({"written": str(path), "questions": len(answers)}))


def apply_update(rec: dict, upd: dict) -> None:
    for key, val in upd.items():
        if key == "id" or key.startswith("_"):
            continue
        if key in ("list", "links", "evidence") and isinstance(val, str):
            val = [val]
        if key == "evidence_add":
            rec["evidence"].extend(val if isinstance(val, list) else [val])
            continue
        rec[key] = val


def cmd_set(args) -> None:
    doc = load_json(args.answers)
    if args.id not in doc["answers"]:
        sys.exit(f"unknown question id {args.id}")
    upd = {}
    for field in ("choice", "text", "image", "status", "confidence", "hint", "notes"):
        val = getattr(args, field)
        if val is not None:
            upd[field] = val
    if args.list_item:
        upd["list"] = args.list_item
    if args.link:
        upd["links"] = args.link
    if args.evidence_json:
        upd["evidence_add"] = json.loads(args.evidence_json)
    apply_update(doc["answers"][args.id], upd)
    doc["meta"]["updated"] = now_iso()
    write_json(args.answers, doc)
    print(json.dumps({"updated": args.id, "fields": sorted(upd)}))


def cmd_patch(args) -> None:
    doc = load_json(args.answers)
    patch = load_json(args.patch)
    items = patch.items() if isinstance(patch, dict) else [(r["id"], r) for r in patch]
    unknown = []
    for qid, upd in items:
        if qid not in doc["answers"]:
            unknown.append(qid)
            continue
        apply_update(doc["answers"][qid], upd)
    doc["meta"]["updated"] = now_iso()
    write_json(args.answers, doc)
    print(json.dumps({"patched": len(list(items)) - len(unknown) if isinstance(patch, list) else len(patch) - len(unknown),
                      "unknown_ids": unknown}))


def words(text: str | None) -> int:
    return len(re.findall(r"\S+", text or ""))


def validate(doc: dict, strict: bool = False) -> dict:
    schema = load_schema()
    answers = doc["answers"]
    reapp = doc["meta"].get("reapplication")
    errors, warnings = [], []
    known = set()
    for section, q in iter_questions(schema):
        known.add(q["id"])
        if section.get("conditional_on") == "reapplication" and not reapp:
            continue
        rec = answers.get(q["id"])
        if rec is None:
            errors.append(f"{q['id']}: missing record")
            continue
        parts = q["parts"]
        st = rec.get("status")
        if st not in STATUSES:
            errors.append(f"{q['id']}: invalid status {st!r}")
        if rec.get("confidence") not in CONFIDENCE:
            errors.append(f"{q['id']}: invalid confidence {rec.get('confidence')!r}")
        choice = rec.get("choice")
        if "choice" in parts and choice is not None:
            opts = option_values(schema, parts["choice"]["option_set"])
            if opts and choice not in opts:
                errors.append(f"{q['id']}: choice {choice!r} not in option set {parts['choice']['option_set']} {opts}")
        if "choice" not in parts and choice is not None:
            warnings.append(f"{q['id']}: has a choice but the question has no dropdown")
        text_spec = parts.get("text") or {}
        if text_spec.get("word_limit") and words(rec.get("text")) > text_spec["word_limit"]:
            errors.append(f"{q['id']}: text has {words(rec.get('text'))} words (limit {text_spec['word_limit']})")
        answered = st in ("verified", "inferred", "applicant_provided", "not_found")
        if answered:
            for part, spec in parts.items():
                need = spec.get("required") or (spec.get("required_if") and spec["required_if"] == choice)
                if not need:
                    continue
                value = {"choice": choice, "text": rec.get("text"), "list": rec.get("list"), "links": rec.get("links"),
                         "image": rec.get("image")}[part]
                if not value:
                    (errors if part == "choice" else warnings).append(f"{q['id']}: required part '{part}' is empty")
        if st in ("verified", "inferred") and choice in ("Yes", "Met") and not any(e.get("url") for e in rec.get("evidence", [])):
            errors.append(f"{q['id']}: '{choice}' marked {st} without any evidence URL")
        if st == "query_failed" and choice == "No":
            errors.append(f"{q['id']}: 'No' cannot rest on a failed query — ask the applicant")
        if st == "verified" and q.get("automation") == "applicant":
            warnings.append(f"{q['id']}: applicant-only question marked verified (should be applicant_provided)")
        if q["id"] in ("S1.confirm", "S8.declaration") and st not in ("applicant_provided", "needs_applicant", "pending"):
            errors.append(f"{q['id']}: must be confirmed by the applicant (status applicant_provided)")
        if rec.get("image") and not Path(rec["image"]).exists():
            warnings.append(f"{q['id']}: image path does not exist: {rec['image']}")
    for qid in answers:
        if qid not in known:
            errors.append(f"{qid}: not a Checklist question id")
    active = {qid: r for qid, r in answers.items() if qid in known and not (qid.startswith("APX1") and not reapp)}
    counts = Counter(r.get("status") for r in active.values())
    unresolved = sorted(qid for qid, r in active.items() if r.get("status") in UNRESOLVED)
    if strict and unresolved:
        errors.append(f"{len(unresolved)} unresolved items: {', '.join(unresolved)}")
    return {"valid": not errors, "errors": errors, "warnings": warnings, "status_counts": dict(counts),
            "unresolved": unresolved,
            "inferred_to_review": sorted(qid for qid, r in active.items() if r.get("status") == "inferred"),
            "ready_to_submit": not errors and not unresolved and all(
                active[q].get("status") == "applicant_provided" for q in ("S1.confirm", "S8.declaration"))}


def cmd_validate(args) -> None:
    report = validate(load_json(args.answers), args.strict)
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["valid"] else 1)


def cmd_pending(args) -> None:
    schema = load_schema()
    doc = load_json(args.answers)
    reapp = doc["meta"].get("reapplication")
    out = []
    for section, q in iter_questions(schema):
        if section.get("conditional_on") == "reapplication" and not reapp:
            continue
        rec = doc["answers"][q["id"]]
        if rec["status"] in UNRESOLVED or (args.include_inferred and rec["status"] == "inferred"):
            choice = q["parts"].get("choice")
            out.append({"id": q["id"], "section": section["title"], "status": rec["status"],
                        "prompt": q["prompt"], "options": option_values(schema, choice["option_set"]) if choice else None,
                        "parts": sorted(q["parts"]), "current": {k: rec[k] for k in ("choice", "text", "list", "links") if rec[k]},
                        "hint": rec.get("hint")})
    print(json.dumps(out, indent=2, ensure_ascii=False))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init")
    p.add_argument("--answers", required=True)
    p.add_argument("--name", required=True)
    p.add_argument("--url", required=True)
    p.add_argument("--community")
    p.add_argument("--reapplication", action="store_true")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_init)
    p = sub.add_parser("set")
    p.add_argument("--answers", required=True)
    p.add_argument("--id", required=True)
    for f in ("choice", "text", "image", "status", "confidence", "hint", "notes", "evidence-json"):
        p.add_argument(f"--{f}")
    p.add_argument("--list-item", action="append")
    p.add_argument("--link", action="append")
    p.set_defaults(func=cmd_set)
    p = sub.add_parser("patch")
    p.add_argument("--answers", required=True)
    p.add_argument("--patch", required=True)
    p.set_defaults(func=cmd_patch)
    p = sub.add_parser("pending")
    p.add_argument("--answers", required=True)
    p.add_argument("--include-inferred", action="store_true")
    p.set_defaults(func=cmd_pending)
    p = sub.add_parser("validate")
    p.add_argument("--answers", required=True)
    p.add_argument("--strict", action="store_true")
    p.set_defaults(func=cmd_validate)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
