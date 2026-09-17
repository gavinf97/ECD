#!/usr/bin/env python3
"""
import_resources.py — build uptime/resources.yml from the ELIXIR services audit
spreadsheet plus uptime/resources_manual.yml.

Selection: rows of sheet "Services" whose "Functional division" is
"Databases & knowledgebases" (161 rows in the 2026-09-14 audit).

Check URL: the resolved `url` column when present, else the ELIXIR-listed `URL`
column (kept as `listed_url` when the two differ).

Re-running is safe: for ids already in resources.yml, hand edits to `enabled`,
`ecd` and `check` are preserved. Manual entries override spreadsheet rows with
the same id.

Usage:
    python import_resources.py [--xlsx FILE] [--division NAME] [--out uptime/resources.yml]
                               [--baseline]   # run one check pass, list URLs needing review
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import UPTIME_ROOT, iso, log, slugify, utcnow  # noqa: E402

DEFAULT_XLSX = UPTIME_ROOT / "sources" / "ELIXIR_services_enriched_2026-09-14.xlsx"
DEFAULT_MANUAL = UPTIME_ROOT / "resources_manual.yml"
DEFAULT_DIVISION = "Databases & knowledgebases"
DEFAULT_ECD = {"provisional_start": None, "period_days": 365, "target": 0.99}
PRESERVED_KEYS = ("enabled", "ecd", "check")


def _clean(value) -> str | None:
    text = str(value).strip() if value is not None else ""
    return text or None


def normalise_url(value) -> str | None:
    """First http(s) URL in a cell, minus stale Java session state.

    Some cells list two URLs ("http://a/, https://b/") and some carry a captured
    session (";jsessionid=...?execution=e1s1") that would not survive between checks.
    """
    text = _clean(value)
    if not text:
        return None
    token = next((t for t in re.split(r"[\s,]+", text) if t.lower().startswith(("http://", "https://"))), None)
    if not token:
        return text
    token = re.sub(r";jsessionid=[^?#]*", "", token, flags=re.I)
    token = re.sub(r"\?execution=e\d+s\d+$", "", token)
    return token


def read_xlsx(path: Path, division: str) -> list[dict]:
    import openpyxl  # only needed for (re-)import, not for the scheduled checks

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    rows = list(wb["Services"].iter_rows(values_only=True))
    header_idx = next(i for i, r in enumerate(rows) if r and r[0] == "Functional division")
    header = rows[header_idx]
    col = {name: i for i, name in enumerate(header) if name}
    source = f"{path.name} (sheet Services, division '{division}')"

    out = []
    for r in rows[header_idx + 1:]:
        if not r or r[col["Functional division"]] != division:
            continue
        listed = normalise_url(r[col["URL"]])
        resolved = normalise_url(r[col["url"]]) if "url" in col else None
        url = resolved if resolved and resolved.lower().startswith(("http://", "https://")) else listed
        badge = _clean(r[col["ELIXIR badge"]])
        biotools = _clean(r[col["bio.tools link"]])
        entry = {
            "name": _clean(r[col["Resource name"]]),
            "url": url,
            "listed_url": listed if listed and listed.rstrip("/") != (url or "").rstrip("/") else None,
            "node": _clean(r[col["ELIXIR Node"]]),
            "badge": None if not badge or badge.startswith("No key-service") else badge,
            "domain": _clean(r[col["Scientific domain"]]),
            "biotools": biotools if biotools and biotools.startswith("http") else None,
            "source": source,
        }
        out.append({k: v for k, v in entry.items() if v is not None})
    return out


def assign_ids(entries: list[dict]) -> None:
    seen: dict[str, int] = {}
    for e in entries:
        base = e.get("id") or slugify(e["name"])
        n = seen.get(base, 0) + 1
        seen[base] = n
        e["id"] = base if n == 1 else f"{base}-{n}"


def build(xlsx: Path, manual: Path, division: str, existing: Path | None) -> list[dict]:
    entries = read_xlsx(xlsx, division)
    assign_ids(entries)
    by_id = {e["id"]: e for e in entries}

    manual_entries = (yaml.safe_load(manual.read_text(encoding="utf-8")) or {}).get("resources", []) \
        if manual.exists() else []
    for m in manual_entries:
        m = dict(m)
        m.setdefault("id", slugify(m["name"]))
        m.setdefault("source", manual.name)
        by_id[m["id"]] = m

    previous = {}
    if existing and existing.exists():
        previous = {r["id"]: r for r in (yaml.safe_load(existing.read_text(encoding="utf-8")) or {})
                    .get("resources", [])}

    resources = []
    for rid, e in by_id.items():
        bad = [f for f in ("name", "url") if not e.get(f)]
        if bad or not e["url"].lower().startswith(("http://", "https://")):
            raise ValueError(f"resource {rid!r} has missing/invalid {bad or 'url'}: {e}")
        e.setdefault("enabled", True)
        e.setdefault("ecd", dict(DEFAULT_ECD))
        for key in PRESERVED_KEYS:
            if key in previous.get(rid, {}):
                e[key] = previous[rid][key]
        order = ["id", "name", "url", "listed_url", "node", "badge", "domain", "biotools",
                 "source", "enabled", "ecd", "check"]
        resources.append({k: e[k] for k in order if k in e} | {k: v for k, v in e.items() if k not in order})
    resources.sort(key=lambda r: r["name"].lower())
    return resources


def write_yaml(resources: list[dict], out: Path, xlsx: Path, division: str) -> None:
    header = (
        "# ECD uptime tracker — monitored resources.\n"
        f"# Generated by uptime/scripts/import_resources.py on {iso(utcnow())}\n"
        f"# from {xlsx.name} (division '{division}') + resources_manual.yml.\n"
        "# Safe to hand-edit `enabled`, `ecd` and `check` (preserved on re-import).\n"
        "# ecd.provisional_start (YYYY-MM-DD) starts the ECD one-year 99% health check for a resource.\n"
        "# check.verify_tls: false skips TLS verification for a resource (use sparingly).\n"
    )
    body = yaml.safe_dump({"resources": resources}, sort_keys=False, allow_unicode=True, width=120)
    out.write_text(header + body, encoding="utf-8")


def baseline(resources: list[dict]) -> None:
    from check import run_checks

    log(f"baseline: checking {len(resources)} resources (failures re-checked after 10s)")
    results = run_checks(resources, retry_delay=10)
    groups = {"url_review (404/410)": [], "down (other)": [], "challenged": [], "tls_warning": []}
    for r in sorted(results.values(), key=lambda r: r["id"]):
        if r["url_review"]:
            groups["url_review (404/410)"].append(r)
        elif r["state"] == "down":
            groups["down (other)"].append(r)
        elif r["state"] == "challenged":
            groups["challenged"].append(r)
        if r.get("tls_warning"):
            groups["tls_warning"].append(r)
    up = sum(1 for r in results.values() if r["state"] == "up")
    print(f"\nBaseline: up={up} challenged={len(groups['challenged'])} "
          f"down={sum(1 for r in results.values() if r['state'] == 'down')}")
    for name, items in groups.items():
        if items:
            print(f"\n{name}: {len(items)}")
            for r in items:
                extra = r.get("tls_warning") if name == "tls_warning" else (r.get("error") or "")[:90]
                print(f"  {r['id']:<45} {r['reason']:<22} {r['url']}  {extra or ''}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--xlsx", type=Path, default=DEFAULT_XLSX)
    ap.add_argument("--manual", type=Path, default=DEFAULT_MANUAL)
    ap.add_argument("--division", default=DEFAULT_DIVISION)
    ap.add_argument("--out", type=Path, default=UPTIME_ROOT / "resources.yml")
    ap.add_argument("--baseline", action="store_true")
    args = ap.parse_args()

    resources = build(args.xlsx, args.manual, args.division, existing=args.out)
    write_yaml(resources, args.out, args.xlsx, args.division)
    manual = sum(1 for r in resources if r.get("source") == args.manual.name)
    print(f"wrote {len(resources)} resources ({len(resources) - manual} from spreadsheet, "
          f"{manual} manual) -> {args.out}")
    if args.baseline:
        baseline(resources)
    return 0


if __name__ == "__main__":
    sys.exit(main())
