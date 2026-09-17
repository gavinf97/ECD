#!/usr/bin/env python3
"""
fair_check.py — Checklist S7.8 ("Please provide a screenshot from the FAIRchecker
result for your resource").

Steps:
  1. Check FAIR-Checker (https://fair-checker.france-bioinformatique.fr) is reachable.
  2. If so, call its API  GET /api/check/metrics_all?url=<resource>  (slow: minutes) and save the
     metric scores, then try to screenshot the web UI result with Playwright (render_pages.py).
  3. Always compute LOCAL FAIR SIGNALS from identity.json + website.json (PIDs, Bioschemas JSON-LD,
     licence, HTTPS, registries, ontologies). These are clearly labelled as NOT FAIR-Checker output
     and can never stand in for the screenshot the Checklist asks for.

If FAIR-Checker is down (it was under maintenance on 2026-09-17) or no screenshot could be taken,
S7.8 stays `needs_applicant`, with instructions for the applicant to run it by hand.

Usage:
    python fair_check.py --identity WORKDIR/identity.json --website WORKDIR/evidence/website.json
                         --out WORKDIR/evidence/fairchecker.json [--png WORKDIR/fairchecker.png] [--api-timeout 420]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import emit, get_json, http_get, load_json, log, now_iso  # noqa: E402
from render_pages import playwright_python  # noqa: E402

BASE = "https://fair-checker.france-bioinformatique.fr"
SCRIPTS = Path(__file__).resolve().parent
UI_METRIC_ORDER = ["F1A", "F1B", "F2A", "F2B", "A11", "A12", "I1", "I2", "I3", "R11", "R12", "R13"]
METRIC_LABELS = {"F1A": "Unique IDs", "F1B": "Persistent IDs", "F2A": "Structured metadata",
                 "F2B": "Shared vocabularies for metadata", "A11": "Open resolution protocol",
                 "A12": "Authorisation procedure or access rights", "I1": "Machine readable format",
                 "I2": "Use shared ontologies", "I3": "External links", "R11": "Metadata includes license",
                 "R12": "Metadata includes provenance", "R13": "Community standards"}


def local_signals(identity: dict, website: dict | None) -> dict:
    m = identity["matches"]
    web = website or {}
    entry = web.get("entry_page") or {}
    jsonld_types = sorted({str(j.get("@type")) for block in web.get("jsonld", []) for j in block.get("summary", [])} |
                          {str(j.get("@type")) for j in entry.get("jsonld", [])})
    lic = web.get("signals", {}).get("license", [])
    return {
        "_label": "LOCAL FAIR SIGNALS computed by the ECD Agent Skill — NOT FAIR-Checker output",
        "F1_persistent_identifiers": {"identifiers_org_prefix": m.get("identifiers_org", {}).get("id"),
                                      "resolver_example": m.get("identifiers_org", {}).get("resolver_example")},
        "F2_machine_readable_metadata": {"jsonld_types": jsonld_types, "entry_page_jsonld": bool(entry.get("jsonld"))},
        "F4_indexed_in_registries": {k: m.get(k, {}).get("status") for k in ("fairsharing", "re3data", "biotools", "bioregistry")},
        "A1_open_protocol": {"https": (identity["homepage"].get("final_url") or "").startswith("https://")},
        "I1_structured_formats": {"content_negotiation": web.get("content_negotiation"),
                                  "api_endpoints": [e.get("url") for e in web.get("api_endpoints", [])]},
        "I2_vocabularies": [o["prefix"] for o in web.get("ontology_prefixes", []) if o.get("in_ols")],
        "R1_1_license": {"website_license_snippets": [s for x in lic[:2] for s in x.get("text_snippets", [])][:2],
                         "biotools_license": (m.get("biotools", {}).get("record") or {}).get("license")},
    }


def parse_metrics(api_result) -> list[dict]:
    """FAIR-Checker returns DQV QualityMeasurement JSON-LD; value 0 = fail, 1 = weak, 2 = strong."""
    rows = []
    for m in api_result or []:
        if not isinstance(m, dict):
            continue
        metric = ((m.get("http://www.w3.org/ns/dqv#isMeasurementOf") or [{}])[0].get("@id") or "").rsplit("/", 1)[-1]
        value = (m.get("http://www.w3.org/ns/dqv#value") or [{}])[0].get("@value")
        if value is None:
            continue  # non-measurement nodes (assessment/provenance records)
        rows.append({"metric": metric, "label": METRIC_LABELS.get(metric), "score": value, "evaluation_url": m.get("@id"),
                     "generated": (m.get("http://www.w3.org/ns/prov#generatedAtTime") or [{}])[0].get("@value")})
    # Since 2026-09 the API sometimes emits .../eval/None as the metric id; results then arrive in the
    # web UI's fixed order, so map them by position (flagged) when exactly 12 unnamed rows come back.
    if rows and all(r["metric"] in ("", "None") for r in rows) and len(rows) == len(UI_METRIC_ORDER):
        for r, name in zip(rows, UI_METRIC_ORDER):
            r["metric"], r["label"], r["metric_id_inferred_by_position"] = name, METRIC_LABELS[name], True
        return rows
    order = {"F": 0, "A": 1, "I": 2, "R": 3}
    return sorted(rows, key=lambda r: (order.get(r["metric"][:1], 9), r["metric"]))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--identity", required=True)
    ap.add_argument("--website")
    ap.add_argument("--out")
    ap.add_argument("--png")
    ap.add_argument("--api-timeout", type=int, default=420)
    ap.add_argument("--skip-api", action="store_true")
    args = ap.parse_args()
    identity = load_json(args.identity)
    website = load_json(args.website) if args.website and Path(args.website).exists() else None
    target = identity["homepage"].get("final_url") or identity["input"]["url"]
    out = {"generated": now_iso(), "target_url": target, "fair_checker_url": f"{BASE}/check",
           "local_signals": local_signals(identity, website)}

    r, err = http_get(BASE + "/", timeout=30)
    reachable = r is not None and r.status_code == 200 and "maintenance" not in r.text.lower()
    out["fair_checker_reachable"] = reachable
    if not reachable:
        out["status"] = "query_failed"
        out["error"] = err or (f"HTTP {r.status_code}" if r is not None and r.status_code != 200 else "service reports maintenance")
    elif not args.skip_api:
        log(f"[fair] FAIR-Checker metrics_all for {target} (can take several minutes)")
        data, aerr = get_json(f"{BASE}/api/check/metrics_all", params={"url": target}, timeout=args.api_timeout)
        out["api_result"] = data
        out["api_error"] = aerr
        out["metric_scores"] = parse_metrics(data)
        out["score_legend"] = "0 = failed, 1 = weak, 2 = strong (FAIR-Checker scale)"
        out["status"] = "found" if data else "query_failed"

    png_path = args.png or (str(Path(args.out).parent.parent / "fairchecker.png") if args.out else "fairchecker.png")
    py = playwright_python()
    if reachable and py:
        log("[fair] screenshot of FAIR-Checker web UI")
        cmd = [py, str(SCRIPTS / "render_pages.py"), "--screenshot", f"{BASE}/check", "--png", png_path,
               "--fill-selector", "#url", "--fill-value", target, "--click-selector", "#btn_test_all",
               "--wait-selector", "#download_csv:not([disabled])", "--timeout-ms", "300000"]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=480)
        try:
            shot = json.loads(proc.stdout.strip().splitlines()[-1])
        except Exception:  # noqa: BLE001
            shot = {"status": "error", "error": proc.stderr[-500:]}
        out["screenshot"] = shot
        excerpt = (shot.get("text_excerpt") or "") + " " + " ".join(str(x) for x in shot.get("links") or [])
        link = re.search(r"https://fair-checker\.france-bioinformatique\.fr/assessment/[0-9a-f]+", excerpt)
        pct = re.search(r"FAIR assessment\s*([\d.]+)\s*%", excerpt)
        out["assessment_url"] = link.group(0) if link else None
        out["overall_percent"] = float(pct.group(1)) if pct else None
        out["screenshot_note"] = ("Automated screenshot: Claude must open/read the PNG and confirm it shows completed "
                                  "metric results for the target URL before using it for S7.8.")
    elif reachable:
        out["screenshot"] = {"status": "skipped", "error": "Playwright unavailable (set ECD_PLAYWRIGHT_PYTHON)"}
    out["manual_instructions"] = (f"Open {BASE}/check, paste {target}, run 'Check', wait for all metrics, then take a "
                                  "full-page screenshot and attach it to Checklist Section 7 item 8.")
    out.setdefault("status", "found" if out.get("api_result") else "query_failed")
    emit(out, args.out, summary={"reachable": reachable, "api": bool(out.get("api_result")),
                                 "screenshot": (out.get("screenshot") or {}).get("status")})


if __name__ == "__main__":
    main()
