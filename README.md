# uptime-data

This branch holds the uptime check results of the ECD uptime tracker. Commits to it come only from the `uptime-check` GitHub Actions workflow, squashed to one commit per UTC day. Don't commit to it by hand; the workflow force-pushes.

- **[STATUS.md](STATUS.md)**: the current human-readable status.
- `summary.json`: the same data, machine-readable.
- `daily/YYYY/YYYY-MM-DD.json`: daily counters for each resource.
- `state.json`: the current state of each resource.
- `events.jsonl`: the audit trail of state changes.

Code, definitions and configuration are in [`uptime/` on main](https://github.com/gavinf97/ECD/tree/main/uptime).
