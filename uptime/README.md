# ECD uptime tracker

This tracks the uptime of ELIXIR biodata resources for the **ELIXIR Community Database (ECD)**.

[ECD Process V1](https://doi.org/10.5281/zenodo.17288943) §5 sets a one-year health check after a resource gets provisional ECD status. The resource needs **99% uptime** during that year to get full ECD status (see also Appendix 3, "Uptime Failure"). This folder is the tracker that records that uptime.

**Live status:** [`STATUS.md` on the `uptime-data` branch](https://github.com/gavinf97/ECD/blob/uptime-data/STATUS.md). Machine-readable results are in [`summary.json`](https://github.com/gavinf97/ECD/blob/uptime-data/summary.json).

This folder does not depend on the ECD Agent Skill in `../agent`, and the agent does not depend on it.

## What is monitored

[`resources.yml`](resources.yml) lists **163 resources**:

- **161** rows from the *Databases & knowledgebases* division of the ELIXIR services audit, [`sources/ELIXIR_services_enriched_2026-09-14.xlsx`](sources/). The check URL is the resolved `url` column, or the ELIXIR-listed `URL` column when that is empty.
- **2** manual entries in [`resources_manual.yml`](resources_manual.yml): the DOME Registry and DOME-ML.

## How it works

The [`uptime-check`](../.github/workflows/uptime-check.yml) GitHub Actions workflow runs every 5 minutes:

1. [`scripts/check.py`](scripts/check.py) sends a `GET` to each URL. Redirects are followed; only the first 64 KB of the body is read, with a 10 s connect and 20 s read timeout. The User-Agent is `ECD-Uptime-Monitor/0.1 (+https://github.com/gavinf97/ECD)`.
2. Each failure is checked again 30 s later. A check is recorded as down only if it fails both times.
3. [`scripts/summarize.py`](scripts/summarize.py) rebuilds `summary.json` and `STATUS.md`.
4. The results are committed to the **`uptime-data`** branch, one commit per UTC day. The tracker never commits to `main`.

### Classification

| State | When | Counts as available |
|---|---|---|
| `up` | Final response is 2xx/3xx, or a 4xx other than 404/410 (e.g. 401/403/429: the server is responding but restricting access) | yes |
| `challenged` | A bot-challenge page is served (Cloudflare "Just a moment…", Anubis, DDoS-Guard, "Checking your browser") | yes; counted separately |
| `down` | 5xx, timeout, DNS error, connection refused/reset, redirect loop, or a TLS error a browser would also reject (expired certificate, hostname mismatch, self-signed certificate) | no |
| `down` + `url_review` | 404/410 on the check URL. The resource has probably moved, so fix the URL | no |

If TLS verification fails only because the certificate chain is incomplete, the resource is checked again without verification. When that works, it is recorded as `up` with a `tls_warning`, because browsers repair incomplete chains.

### Metrics

- **Uptime** = (up + challenged) ÷ recorded checks, over each window: today (UTC), 7, 30, 90 and 365 days.
- **Coverage** = recorded checks ÷ expected checks (one every 5 min since the resource was first seen). GitHub sometimes skips or delays scheduled runs. Missed runs lower coverage and are **never** counted as up.
- **Latency**: p50/p95 over 30 days, from a histogram with buckets at ≤250, 500, 1k, 2k, 5k and 10k ms and >10k. Only successful checks are included.
- **ECD verdict**: only shown for resources with `ecd.provisional_start` set.
  - During the period: `ON TRACK` or `AT RISK` (below target).
  - After the period: `PASS`, `FAIL`, or `INSUFFICIENT DATA` when coverage is under 90%.

### Data layout (`uptime-data` branch)

```
daily/YYYY/YYYY-MM-DD.json   per resource: checks, up, challenged, down, latency histogram
state.json                   current state, since, first_seen, consecutive downs, last code/error
events.jsonl                 state changes, and changes of failure reason while down (audit trail)
summary.json  STATUS.md      derived; rebuilt every run
```

Raw per-check rows are not kept, so the branch grows by about 10 MB a year.

## Common tasks

**Start an ECD health check for a resource.** In `resources.yml`, set
```yaml
  ecd:
    provisional_start: 2026-10-01   # date provisional ECD status was granted
    period_days: 365
    target: 0.99
```

**Add a resource that is not in the spreadsheet.** Add it to `resources_manual.yml`, then re-import.

**Disable a resource.** Set `enabled: false`. Its history is kept.

**Re-import after the spreadsheet changes.** Your edits to `enabled`, `ecd` and `check` are kept:
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

## Limitations

- **One vantage point.** Checks run from GitHub-hosted runners, mostly in US Azure regions. A resource that blocks those IP ranges, or is unreachable only from there, will look down. Commercial monitors such as updown.io confirm from several locations. Before acting on a `FAIL`, check the `events.jsonl` entries for it.
- **Homepage only.** The tracker checks one URL per resource. It does not test APIs or search.
- **Challenge pages** show that the server is responding, but not that the content behind the challenge works.
- **Inactivity.** GitHub may disable scheduled workflows in a repository with no activity for 60 days. If `STATUS.md` stops updating, re-enable the workflow in the Actions tab.
