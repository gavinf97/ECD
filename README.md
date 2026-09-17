# ECD

This repository holds tooling for the **ELIXIR Community Database (ECD)**. It follows the [ECD Process V1](https://doi.org/10.5281/zenodo.17288943) and the [ECD Checklist V1](https://doi.org/10.5281/zenodo.17289009).

There are two independent components. Each has its own folder, dependencies, tests and README, and neither imports from the other.

| Folder | Component | What it does |
|---|---|---|
| [`agent/`](agent/) | **ECD Agent Skill** | A Claude Agent Skill that takes a resource's name and URL, pre-fills the ECD Checklist with evidence, and renders it as JSON, Markdown, DOCX, PDF and HTML. |
| [`uptime/`](uptime/) | **ECD uptime tracker** | Checks 163 ELIXIR data resources every 5 minutes with GitHub Actions and reports their uptime against the ECD 99% health-check target. **[Live status →](https://github.com/gavinf97/ECD/blob/uptime-data/STATUS.md)** |

## Repository layout

```
agent/                     ECD Agent Skill (SKILL.md, scripts/, references/, templates/, tests/, examples/)
uptime/                    uptime tracker (resources.yml, scripts/, tests/, sources/)
.github/workflows/
  uptime-check.yml         scheduled checks; commits results to the uptime-data branch
  uptime-tests.yml         uptime/ tests, run on changes to uptime/**
branch uptime-data         check results only (STATUS.md, summary.json, daily/, events.jsonl)
```

`main` holds the code for both components. The uptime tracker's results go only to the `uptime-data` branch, so its frequent commits never touch `main`.

## Install the agent skill

```bash
ln -s "$(pwd)/agent" ~/.claude/skills/ecd-agent-skill
pip install -r agent/requirements.txt
```

For usage, see [`agent/README.md`](agent/README.md). For the tracker, see [`uptime/README.md`](uptime/README.md).
