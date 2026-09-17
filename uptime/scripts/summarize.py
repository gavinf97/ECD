#!/usr/bin/env python3
"""
summarize.py — build summary.json and STATUS.md from the uptime data directory.

Definitions (see uptime/README.md):
  uptime    = (up + challenged) / checks          over the checks actually recorded
  coverage  = checks / expected checks            expected = one per interval since the resource
                                                  was first seen; missed cron runs lower coverage,
                                                  they are never counted as up
  windows   = today (UTC), 7d, 30d, 90d, 365d     calendar days ending today (UTC)
  ECD verdict (only when ecd.provisional_start is set; ECD Process V1 §5, target 99%):
            NOT STARTED | ON TRACK | AT RISK | PASS | FAIL | INSUFFICIENT DATA (coverage < 90%)

Usage:
    python summarize.py --data DIR [--config uptime/resources.yml]
"""

from __future__ import annotations

import argparse
import math
import sys
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (DEFAULT_CONFIG, INTERVAL_MINUTES, N_BUCKETS, daily_path, daterange,  # noqa: E402
                    hist_percentile, iso, load_json, load_resources, log, parse_iso, state_path,
                    utcnow, write_json)

WINDOWS = [("today", 1), ("7d", 7), ("30d", 30), ("90d", 90), ("365d", 365)]
MIN_COVERAGE = 0.90


def load_days(data_dir: Path, start: date, end: date) -> dict[date, dict]:
    days = {}
    for d in daterange(start, end):
        doc = load_json(daily_path(data_dir, d))
        if doc:
            days[d] = doc
    return days


def expected_checks(day: date, now: datetime, first_seen: datetime | None,
                    interval: int = INTERVAL_MINUTES) -> int:
    start = datetime.combine(day, time.min, tzinfo=timezone.utc)
    end = min(start + timedelta(days=1), now)
    if first_seen:
        start = max(start, first_seen)
    if end <= start:
        return 0
    return math.ceil((end - start).total_seconds() / (interval * 60))


def aggregate(days: dict[date, dict], rid: str, start: date, end: date, now: datetime,
              first_seen: datetime | None, interval: int = INTERVAL_MINUTES) -> dict:
    agg = {"checks": 0, "up": 0, "challenged": 0, "down": 0, "latency_sum_ms": 0,
           "latency_hist": [0] * N_BUCKETS, "expected": 0}
    for d in daterange(start, end):
        # Measure each day against the interval in force that day, so a change of schedule
        # does not distort the coverage recorded for earlier days.
        agg["expected"] += expected_checks(d, now, first_seen,
                                           days.get(d, {}).get("interval_minutes", interval))
        counts = days.get(d, {}).get("resources", {}).get(rid)
        if not counts:
            continue
        for k in ("checks", "up", "challenged", "down", "latency_sum_ms"):
            agg[k] += counts.get(k, 0)
        for i, n in enumerate(counts.get("latency_hist", [])[:N_BUCKETS]):
            agg["latency_hist"][i] += n
    return agg


def rates(agg: dict) -> dict:
    checks = agg["checks"]
    uptime = (agg["up"] + agg["challenged"]) / checks if checks else None
    expected = max(agg["expected"], 1 if checks else 0)
    coverage = min(1.0, checks / expected) if expected else None
    return {"uptime": uptime, "coverage": coverage, "checks": checks, "down": agg["down"],
            "challenged": agg["challenged"]}


def ecd_verdict(ecd: dict | None, days: dict[date, dict], rid: str, today: date, now: datetime,
                first_seen: datetime | None) -> dict | None:
    if not ecd or not ecd.get("provisional_start"):
        return None
    start = date.fromisoformat(str(ecd["provisional_start"]))
    period = int(ecd.get("period_days", 365))
    target = float(ecd.get("target", 0.99))
    end = start + timedelta(days=period - 1)
    out = {"provisional_start": start.isoformat(), "period_end": end.isoformat(), "target": target}
    if today < start:
        return {**out, "status": "NOT STARTED", "uptime": None, "coverage": None}
    r = rates(aggregate(days, rid, start, min(today, end), now, first_seen))
    ended = today > end
    if ended:
        if r["coverage"] is None or r["coverage"] < MIN_COVERAGE:
            status = "INSUFFICIENT DATA"
        else:
            status = "PASS" if r["uptime"] >= target else "FAIL"
    elif not r["checks"]:
        status = "NO DATA"
    else:
        status = "AT RISK" if r["uptime"] < target else "ON TRACK"
    return {**out, "status": status, "uptime": r["uptime"], "coverage": r["coverage"],
            "days_elapsed": (min(today, end) - start).days + 1}


def build_summary(resources: list[dict], data_dir: Path, now: datetime) -> dict:
    today = now.date()
    state = load_json(state_path(data_dir)) or {"resources": {}, "runs_total": 0}
    oldest = today - timedelta(days=365)
    for res in resources:  # ECD windows may reach further back than 365 days
        start = (res.get("ecd") or {}).get("provisional_start")
        if start:
            oldest = min(oldest, date.fromisoformat(str(start)))
    days = load_days(data_dir, oldest, today)

    rows = []
    for res in resources:
        rid = res["id"]
        st = state["resources"].get(rid, {})
        first_seen = parse_iso(st["first_seen"]) if st.get("first_seen") else None
        windows = {}
        for name, n in WINDOWS:
            windows[name] = rates(aggregate(days, rid, today - timedelta(days=n - 1), today, now, first_seen))
        lat = aggregate(days, rid, today - timedelta(days=29), today, now, first_seen)
        ok = lat["up"] + lat["challenged"]
        rows.append({
            "id": rid, "name": res.get("name", rid), "url": res["url"],
            "node": res.get("node"), "badge": res.get("badge"),
            "state": st.get("state", "unknown"), "since": st.get("since"),
            "reason": st.get("reason"), "code": st.get("code"), "error": st.get("error"),
            "last_checked": st.get("last_checked"), "final_url": st.get("final_url"),
            "url_review": bool(st.get("url_review")), "tls_warning": st.get("tls_warning"),
            "windows": windows,
            "latency_30d": {"p50": hist_percentile(lat["latency_hist"], 0.5),
                            "p95": hist_percentile(lat["latency_hist"], 0.95),
                            "mean_ms": round(lat["latency_sum_ms"] / ok) if ok else None},
            "ecd": ecd_verdict(res.get("ecd"), days, rid, today, now, first_seen),
        })

    totals = {s: sum(1 for r in rows if r["state"] == s) for s in ("up", "challenged", "down", "unknown")}
    totals["url_review"] = sum(1 for r in rows if r["url_review"])
    return {"generated": iso(now), "interval_minutes": INTERVAL_MINUTES,
            "runs_total": state.get("runs_total", 0), "last_run": state.get("updated"),
            "resource_count": len(rows), "totals": totals, "resources": rows}


# --- STATUS.md ---------------------------------------------------------------

def pct(x: float | None) -> str:
    return "—" if x is None else f"{x * 100:.2f}%"


def cell(text) -> str:
    return str(text if text not in (None, "") else "—").replace("|", "\\|").replace("\n", " ")


def link(row: dict) -> str:
    return f"[{cell(row['name'])}]({row['url']})"


STATE_ICON = {"up": "🟢 up", "challenged": "🟡 challenged", "down": "🔴 down", "unknown": "⚪ unknown"}


def render_status(summary: dict) -> str:
    rows = summary["resources"]
    t = summary["totals"]
    out = [
        "# ECD uptime status",
        "",
        f"Generated **{summary['generated']}** · last run {summary['last_run'] or '—'} · "
        f"{summary['resource_count']} resources · checks every {summary['interval_minutes']} min from GitHub Actions",
        "",
        f"🟢 up **{t['up']}** · 🟡 challenged **{t['challenged']}** · 🔴 down **{t['down']}** · "
        f"⚪ unknown **{t['unknown']}** · URL review **{t['url_review']}**",
        "",
        "Uptime = (up + challenged) / recorded checks. Coverage = recorded / expected checks. "
        "ECD target: 99% over the one-year health check (ECD Process V1 §5). "
        "Definitions: [uptime/README.md](https://github.com/gavinf97/ECD/blob/main/uptime/README.md).",
        "",
    ]

    down = sorted((r for r in rows if r["state"] == "down"), key=lambda r: r["since"] or "")
    out += ["## Currently down", ""]
    if down:
        out += ["| Resource | Since (UTC) | Reason | 30d uptime |", "|---|---|---|---|"]
        out += [f"| {link(r)} | {cell(r['since'])} | {cell(r['reason'])} | {pct(r['windows']['30d']['uptime'])} |"
                for r in down]
    else:
        out.append("None.")
    out.append("")

    review = [r for r in rows if r["url_review"]]
    if review:
        out += ["## URL review needed (404/410 on the check URL)", "",
                "| Resource | Check URL | Reason |", "|---|---|---|"]
        out += [f"| {cell(r['name'])} | {r['url']} | {cell(r['reason'])} |" for r in review]
        out.append("")

    ecd_rows = [r for r in rows if r["ecd"]]
    if ecd_rows:
        out += ["## ECD health checks", "",
                "| Resource | Provisional start | Period end | Status | Uptime | Coverage |",
                "|---|---|---|---|---|---|"]
        out += [f"| {link(r)} | {r['ecd']['provisional_start']} | {r['ecd']['period_end']} | "
                f"**{r['ecd']['status']}** | {pct(r['ecd']['uptime'])} | {pct(r['ecd']['coverage'])} |"
                for r in ecd_rows]
        out.append("")

    below = sorted((r for r in rows if r["windows"]["30d"]["uptime"] is not None
                    and r["windows"]["30d"]["uptime"] < 0.99), key=lambda r: r["windows"]["30d"]["uptime"])
    out += ["## Below 99% over the last 30 days", ""]
    if below:
        out += ["| Resource | Node | 30d uptime | 30d coverage | Down checks |", "|---|---|---|---|---|"]
        out += [f"| {link(r)} | {cell(r['node'])} | {pct(r['windows']['30d']['uptime'])} | "
                f"{pct(r['windows']['30d']['coverage'])} | {r['windows']['30d']['down']} |" for r in below]
    else:
        out.append("None.")
    out.append("")

    out += ["## All resources", "",
            "| Resource | Node | State | Today | 7d | 30d | 90d | 365d | Coverage 30d | p95 30d |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r["name"].lower()):
        w = r["windows"]
        out.append(f"| {link(r)} | {cell(r['node'])} | {STATE_ICON.get(r['state'], r['state'])} | "
                   f"{pct(w['today']['uptime'])} | {pct(w['7d']['uptime'])} | {pct(w['30d']['uptime'])} | "
                   f"{pct(w['90d']['uptime'])} | {pct(w['365d']['uptime'])} | {pct(w['30d']['coverage'])} | "
                   f"{cell(r['latency_30d']['p95'])} |")
    out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    ap.add_argument("--data", type=Path, required=True)
    args = ap.parse_args()

    resources = load_resources(args.config)
    summary = build_summary(resources, args.data, utcnow())
    write_json(args.data / "summary.json", summary)
    (args.data / "STATUS.md").write_text(render_status(summary), encoding="utf-8")
    t = summary["totals"]
    log(f"summary: {summary['resource_count']} resources, up={t['up']} challenged={t['challenged']} "
        f"down={t['down']} unknown={t['unknown']} url_review={t['url_review']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
