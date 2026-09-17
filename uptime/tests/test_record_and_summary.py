from datetime import datetime, timedelta, timezone

import pytest

import check
from check import record
from common import daily_path, events_path, load_json, state_path
from summarize import build_summary, expected_checks, render_status

T0 = datetime(2026, 9, 10, 0, 0, tzinfo=timezone.utc)
RESOURCES = [
    {"id": "alpha", "name": "Alpha DB", "url": "https://alpha.example.org", "node": "ELIXIR Italy",
     "ecd": {"provisional_start": "2026-09-10", "period_days": 365, "target": 0.99}},
    {"id": "beta", "name": "Beta DB", "url": "https://beta.example.org", "node": "ELIXIR UK",
     "ecd": {"provisional_start": None}},
]


@pytest.fixture(autouse=True)
def five_minute_interval(monkeypatch):
    """These tests synthesise a check every 5 minutes; record() stamps each daily file
    with the interval in force, and the summary measures coverage against that."""
    monkeypatch.setattr(check, "INTERVAL_MINUTES", 5)


def result(rid, state, code=200, latency=300, reason=None):
    return {"id": rid, "url": f"https://{rid}.example.org", "checked_at": "x", "state": state,
            "reason": reason or ("ok" if state == "up" else f"http_{code}"), "code": code,
            "latency_ms": latency, "final_url": None, "error": None, "url_review": code in (404, 410),
            "tls_warning": None}


def run(data, when, alpha="up", beta="up", beta_code=200):
    record(data, {"alpha": result("alpha", alpha), "beta": result("beta", beta, code=beta_code)}, when)


def test_record_counts_state_and_events(tmp_path):
    run(tmp_path, T0)
    run(tmp_path, T0 + timedelta(minutes=5), beta="down", beta_code=502)
    run(tmp_path, T0 + timedelta(minutes=10), beta="down", beta_code=502)
    run(tmp_path, T0 + timedelta(minutes=15), beta="down", beta_code=503)
    run(tmp_path, T0 + timedelta(minutes=20))

    daily = load_json(daily_path(tmp_path, T0.date()))
    assert daily["runs"] == 5
    assert daily["resources"]["beta"]["checks"] == 5
    assert daily["resources"]["beta"]["down"] == 3
    assert daily["resources"]["alpha"]["latency_hist"][1] == 5  # 300 ms -> <=500 bucket
    assert daily["resources"]["beta"]["latency_sum_ms"] == 600  # down checks excluded from latency

    state = load_json(state_path(tmp_path))["resources"]
    assert state["beta"]["state"] == "up"
    assert state["beta"]["since"] == "2026-09-10T00:20:00Z"
    assert state["beta"]["consecutive_down"] == 0
    assert state["beta"]["first_seen"] == "2026-09-10T00:00:00Z"

    events = [line for line in events_path(tmp_path).read_text().splitlines()]
    # 2 initial state_change + beta up->down + reason 502->503 + beta down->up; repeated identical downs not logged
    assert len(events) == 5
    assert '"down_reason_changed"' in events[3]


def test_expected_checks_respects_first_seen_and_now():
    day = T0.date()
    assert expected_checks(day, T0 + timedelta(days=2), None, 5) == 288
    assert expected_checks(day, T0 + timedelta(hours=1), None, 5) == 12
    assert expected_checks(day, T0 + timedelta(days=2), T0 + timedelta(hours=12), 5) == 144
    assert expected_checks(day, T0, None, 5) == 0
    assert expected_checks(day, T0 + timedelta(days=2), None, 60) == 24


def test_summary_uptime_coverage_and_ecd(tmp_path):
    # Two days, one check every 5 minutes, except a 2-hour gap on day 2 (missed cron runs).
    # beta is down for 6 checks (30 min) on day 1.
    t = T0
    end = T0 + timedelta(days=2)
    gap = (T0 + timedelta(days=1, hours=6), T0 + timedelta(days=1, hours=8))
    i = 0
    while t < end:
        if not (gap[0] <= t < gap[1]):
            run(tmp_path, t, beta="down" if 100 <= i < 106 else "up", beta_code=502 if 100 <= i < 106 else 200)
        t += timedelta(minutes=5)
        i += 1

    now = end - timedelta(minutes=1)  # still on day 2
    summary = build_summary(RESOURCES, tmp_path, now)
    rows = {r["id"]: r for r in summary["resources"]}

    beta7 = rows["beta"]["windows"]["7d"]
    assert beta7["checks"] == 576 - 24
    assert beta7["down"] == 6
    assert abs(beta7["uptime"] - (546 / 552)) < 1e-9
    assert abs(beta7["coverage"] - (552 / 576)) < 1e-9
    assert rows["alpha"]["windows"]["7d"]["uptime"] == 1.0

    assert rows["alpha"]["ecd"]["status"] == "ON TRACK"
    assert rows["beta"]["ecd"] is None
    assert rows["alpha"]["latency_30d"]["p95"] == "≤500 ms"

    md = render_status(summary)
    assert "## ECD health checks" in md
    assert "Beta DB" in md and "Alpha DB" in md


def test_ecd_verdict_at_risk_pass_and_insufficient(tmp_path):
    # alpha down 2% of checks on its only day of data
    t = T0
    for i in range(288):
        run(tmp_path, t, alpha="down" if i < 6 else "up")
        t += timedelta(minutes=5)

    res = [dict(RESOURCES[0])]
    mid = build_summary(res, tmp_path, T0 + timedelta(hours=23, minutes=59))
    assert mid["resources"][0]["ecd"]["status"] == "AT RISK"

    res[0]["ecd"] = {"provisional_start": "2026-09-10", "period_days": 1, "target": 0.97}
    after = build_summary(res, tmp_path, T0 + timedelta(days=3))
    assert after["resources"][0]["ecd"]["status"] == "PASS"

    res[0]["ecd"] = {"provisional_start": "2026-09-10", "period_days": 30, "target": 0.97}
    ended_sparse = build_summary(res, tmp_path, T0 + timedelta(days=40))
    assert ended_sparse["resources"][0]["ecd"]["status"] == "INSUFFICIENT DATA"


def test_unchecked_resource_is_unknown(tmp_path):
    summary = build_summary(RESOURCES, tmp_path, T0)
    assert summary["totals"]["unknown"] == 2
    assert all(r["windows"]["30d"]["uptime"] is None for r in summary["resources"])
