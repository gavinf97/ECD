# ECD uptime tracker

Continuous uptime monitoring of ELIXIR biodata resources for the
**ELIXIR Community Database (ECD)**.

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/monitoring.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml)
[![resources monitored](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/resources.json)](https://gavinf97.github.io/ECD/)
[![responding](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/up.json)](https://gavinf97.github.io/ECD/)
[![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/down.json)](https://github.com/gavinf97/ECD/blob/uptime-data/STATUS.md#needs-attention)
[![last check](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/last-check.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml)

## 1. Where to see the status

| Where | What you get |
|---|---|
| **🖥️ [Dashboard → gavinf97.github.io/ECD](https://gavinf97.github.io/ECD/)** | Status tiles, a "needs attention" list, per-resource 30-day uptime strips, search, and filters by node and state. |
| **📄 [STATUS.md](https://github.com/gavinf97/ECD/blob/uptime-data/STATUS.md)** | The same status as a GitHub-rendered page: what is down, which URLs need review, every resource, recent state changes. |
| **⚙️ [Actions → uptime-check](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml)** | Every run, each with a status summary attached. This is where you confirm monitoring is alive. |
| **🔢 [summary.json](https://github.com/gavinf97/ECD/blob/uptime-data/summary.json)** | All of it, machine-readable. |

Every surface leads with whether monitoring is **ACTIVE** or **STALE**. Stale means no check
has landed for more than 3 intervals — the usual cause is GitHub disabling the schedule after
60 days of repository inactivity; re-enable it in the Actions tab.

## 2. Where the results are deposited

On the **[`uptime-data`](https://github.com/gavinf97/ECD/tree/uptime-data) branch**, never on
`main`. Hourly result commits would otherwise bury the code history. The branch is also the
GitHub Pages source, so pushing to it republishes the dashboard.

```
branch uptime-data
├── index.html      the dashboard (copied from uptime/dashboard/ by the workflow)
├── STATUS.md       the status page
├── summary.json    current status of every resource
├── history.json    per-resource daily uptime, last 90 days
├── state.json      current state per resource: since, first_seen, consecutive downs, last code
├── events.jsonl    append-only audit trail of state changes and changes of failure reason
├── badges/*.json   shields.io endpoints behind the badges
└── daily/YYYY/YYYY-MM-DD.json    per resource: checks, up, challenged, down, latency histogram
```

`STATUS.md`, `summary.json`, `history.json`, `badges/` and the branch's own `README.md` are all
rewritten by [`scripts/summarize.py`](scripts/summarize.py) after every check — never edit them
by hand. Commits are squashed to one per UTC day and force-pushed. Raw per-check rows are not
kept, so the branch grows by about 10 MB a year.

## 3. What is monitored

[`resources.yml`](resources.yml) lists **163 resources**, all enabled:

- **161** rows from the *Databases & knowledgebases* division of the ELIXIR services audit,
  [`sources/ELIXIR_services_enriched_2026-09-14.xlsx`](sources/). The check URL is the resolved
  `url` column, or the ELIXIR-listed `URL` column when that is empty.
- **2** manual entries in [`resources_manual.yml`](resources_manual.yml): the DOME Registry and
  DOME-ML.

Every one is checked on every run. There are no per-resource timers, periods or deadlines:
monitoring runs indefinitely. 99% — the ECD health-check target in
[ECD Process V1](https://doi.org/10.5281/zenodo.17288943) §5 — is reported as a reference line
only, to sort the "below target" list.

This folder does not depend on the ECD Agent Skill in `../agent`, and the agent does not depend
on it.

## 4. How it works

The [`uptime-check`](../.github/workflows/uptime-check.yml) workflow targets **once an hour**,
with four crons an hour to make up for runs that GitHub drops (see [Check interval](#check-interval)):

1. [`scripts/check.py`](scripts/check.py) sends a `GET` to each URL. Redirects are followed; only
   the first 64 KB of the body is read, with a 10 s connect and 20 s read timeout. The User-Agent
   is `ECD-Uptime-Monitor/0.1 (+https://github.com/gavinf97/ECD)`.
2. Each failure is checked again 30 s later. A check is recorded as down only if it fails both times.
3. [`scripts/summarize.py`](scripts/summarize.py) rebuilds every report listed in §2.
4. The workflow copies `dashboard/index.html` to the data branch and commits, one commit per UTC
   day. It never commits to `main`.

### Classification

| State | When | Counts as available |
|---|---|---|
| `up` | Final response is 2xx/3xx, or a 4xx other than 404/410 (e.g. 401/403/429: the server is responding but restricting access) | yes |
| `challenged` | A bot-challenge page is served (Cloudflare "Just a moment…", Anubis, DDoS-Guard, "Checking your browser") | yes; counted separately |
| `down` | 5xx, timeout, DNS error, connection refused/reset, redirect loop, or a TLS error a browser would also reject (expired certificate, hostname mismatch, self-signed certificate) | no |
| `down` + `url_review` | 404/410 on the check URL. The resource has moved or been retired, so the URL needs fixing — see below | no |

If TLS verification fails only because the certificate chain is incomplete, the resource is
checked again without verification. When that works, it is recorded as `up` with a `tls_warning`,
because browsers repair incomplete chains.

### Metrics

- **Uptime** = (up + challenged) ÷ recorded checks, over each window: today (UTC), 7, 30, 90 and
  365 days.
- **Coverage** = recorded checks ÷ expected checks (one per interval since the resource was first
  seen). GitHub sometimes skips or delays scheduled runs. Missed runs lower coverage and are
  **never** counted as up. Each daily file records the interval in force that day, so changing the
  schedule does not distort earlier coverage.
- **Latency**: p50/p95 over 30 days, from a histogram with buckets at ≤250, 500, 1k, 2k, 5k and
  10k ms and >10k. Only successful checks are included.

### Check interval

The target interval is **1 hour** (`INTERVAL_MINUTES` in [`scripts/common.py`](scripts/common.py)).
The workflow schedules **four** crons an hour, at :03, :17, :33 and :49, because GitHub's
scheduler is best-effort.

From 2026-09-18 to 2026-09-24, the single hourly cron `17 * * * *` delivered only **5–7 runs a
day**, with gaps of 2.5–6 hours. Every run succeeded and the repository is public, so this was
scheduler throttling, not a cost or minutes limit. With four ticks an hour, hourly coverage
survives even if about 75% of them are dropped.

Extra runs do no harm. Coverage is capped at 100%, a run takes about a minute, and the
concurrency group stops runs from overlapping.

Every surface now shows **runs in the last 24 h**, so under-delivery is visible. The dashboard
also works out staleness against the viewer's clock, so it shows **STALE** even though no run
has happened to report it. If runs stay below about 18 a day for a week, use the escalation below.

It is hourly because GitHub's scheduler would not deliver a 5-minute cadence for this repository.
When it was set up on 2026-09-17, the first scheduled run appeared 5.5 hours after the repository
was created, and only one scheduled run arrived in the hour that followed, though manual runs
worked throughout. GitHub
[documents](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule)
that scheduled workflows can be delayed under load, and 5-minute schedules on free public
repositories are throttled heavily in practice.

What this costs: downtime is detected to the nearest hour, and a year gives about 8,760 samples
per resource. A resource that is down for 20 minutes may be missed entirely.

**Escalation**, for when runs stay irregular or finer resolution is needed: trigger runs from
outside GitHub's scheduler.

1. Create a fine-grained token scoped to this repository only, with *Actions: read and write*.
2. Register a free external cron job, for example on cron-job.org, to run
   `POST https://api.github.com/repos/gavinf97/ECD/actions/workflows/uptime-check.yml/dispatches`
   with the body `{"ref":"main"}`.
3. Set a reminder for when the token expires.

For multi-location checks, use a commercial monitor such as updown.io, as the ECD Process
suggests.

## 5. Common tasks

**Fix a resource flagged "check URL needs review".** It returns 404/410, so it has moved or been
retired. `url` is owned by the spreadsheet import and would be overwritten, so put the corrected
address in `check.url`, which survives re-import:
```yaml
  check:
    url: https://the-new-address.example.org/
```
If the resource is genuinely gone, set `enabled: false` instead. Its history is kept either way.

**Add a resource that is not in the spreadsheet.** Add it to `resources_manual.yml`, then re-import.

**Re-import after the spreadsheet changes.** Your edits to `enabled` and `check` are kept:
```bash
pip install -r uptime/requirements.txt -r uptime/requirements-dev.txt
python uptime/scripts/import_resources.py              # rewrites uptime/resources.yml
python uptime/scripts/import_resources.py --baseline   # also runs one live pass and lists URLs to review
```

**Run locally:**
```bash
python uptime/scripts/check.py --only disprot,dome-registry --dry-run   # print results, write nothing
python uptime/scripts/check.py --data /tmp/ecd-data && python uptime/scripts/summarize.py --data /tmp/ecd-data
python -m pytest uptime/tests
```

**Preview the dashboard locally** (it reads `summary.json` and `history.json` beside itself):
```bash
cp uptime/dashboard/index.html /tmp/ecd-data/ && python -m http.server -d /tmp/ecd-data 8000
```

## 6. Limitations

- **One vantage point.** Checks run from GitHub-hosted runners, mostly in US Azure regions. A
  resource that blocks those IP ranges, or is unreachable only from there, will look down.
  Commercial monitors such as updown.io confirm from several locations. Before acting on a
  sustained outage, check the `events.jsonl` entries for it.
- **Homepage only.** The tracker checks one URL per resource. It does not test APIs or search.
- **Challenge pages** show that the server is responding, but not that the content behind the
  challenge works.
- **Hourly sampling.** Outages shorter than an hour can be missed entirely; see
  [Check interval](#check-interval).
- **Inactivity.** GitHub may disable scheduled workflows in a repository with no activity for 60
  days. Every report says so when it happens: monitoring is reported as **STALE** and the
  dashboard shows a banner.
