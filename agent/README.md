# ECD Agent Skill

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](./LICENSE.md)

A [Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) that pre-fills the
**ELIXIR Community Database (ECD) Checklist**
([doi:10.5281/zenodo.17289009](https://doi.org/10.5281/zenodo.17289009)) for a biodata resource. It
works from just the resource's **name and URL**, following the **ECD Process**
([doi:10.5281/zenodo.17288943](https://doi.org/10.5281/zenodo.17288943)).

It checks the registries and services the Checklist asks about, crawls the resource website,
answers each question with evidence, asks the applicant only what cannot be verified publicly,
and renders the completed form.

---

## What it does

Given `name + URL`, the skill:

1. **Resolves the resource's identity** across Bioregistry, identifiers.org, re3data, bio.tools, FAIRsharing, UniProt cross-reference databases and OpenEBench. Matching uses the homepage domain and name.
2. **Gathers evidence:**
   - Europe PMC database papers, grants and affiliations
   - TeSS training materials; WorkflowHub; APICURON; OpenEBench uptime metrics
   - Wayback Machine first capture; overlapping resources; BioHackathon leads
   - a polite crawl of the website, with single-page apps rendered via Playwright: team, helpdesk, SAB, privacy, licence, API, JSON-LD/Bioschemas, ontology CURIEs checked against OLS, LS-AAI, analytics
   - code repository licence, containers and releases
   - a **FAIR-Checker** run, with a screenshot for Checklist S7.8
3. **Checks Section 1 eligibility** against dated snapshots of ELIXIR Node SDP services, Communities, CDR, EDD, RIR and GCBR lists.
4. **Proposes answers** for the 75 Checklist items. Each gets a status (`verified` / `inferred` / `needs_applicant` / `not_found` / …), a confidence level and evidence URLs. Claude then reviews them and drafts the short free-text answers.
5. **Runs a short Q&A** with the applicant for items only they can answer: FTE, funding, backups, declarations.
6. **Renders** the checklist as **JSON, Markdown, HTML, DOCX and PDF**, mirroring the official form, with an evidence appendix. A clean *submission copy* is also available.

The skill never submits anything; the applicant emails the PDF to
`elixir-community-databases@elixir-europe.org`.

## Installation

```bash
git clone <this repo> ~/.claude/skills/ecd-agent-skill      # personal skill
# or symlink an existing checkout:
ln -s /path/to/ECD/agent ~/.claude/skills/ecd-agent-skill

pip install -r ~/.claude/skills/ecd-agent-skill/requirements.txt
# recommended: headless browser for SPA websites + FAIR-Checker screenshot
pip install playwright && playwright install chromium
```

PDF output uses LibreOffice (`soffice`) if installed, otherwise reportlab.

### Configuration

| Variable | Required | Purpose |
|---|---|---|
| `ECD_PLAYWRIGHT_PYTHON` | no | Python interpreter that has Playwright, if the main one does not |
| `GITHUB_TOKEN` | no | GitHub API rate limits; a logged-in `gh` CLI is used automatically otherwise |
| `FAIRSHARING_USERNAME`, `FAIRSHARING_PASSWORD` | no | Richer FAIRsharing record detail |
| `ECD_CACHE_DIR` | no | Cache for the Bioregistry dump (default `~/.cache/ecd-agent-skill`) |

## Usage

In Claude Code:

```
Fill in the ECD checklist for MobiDB https://mobidb.org, applying to the Intrinsically Disordered Proteins Community
```

or `/ecd-agent-skill`. See [SKILL.md](./SKILL.md) for the full agent workflow.

### Running the tooling standalone

```bash
# evidence pipeline (identity -> registries + website -> repo, FAIR-Checker, eligibility -> proposals + digest)
python scripts/run_pipeline.py --name MobiDB --url https://mobidb.org --workdir runs/mobidb

# answers document
python scripts/answers.py patch    --answers runs/mobidb/answers.json --patch runs/mobidb/proposals.json
python scripts/answers.py pending  --answers runs/mobidb/answers.json
python scripts/answers.py set      --answers runs/mobidb/answers.json --id S4.5 --choice "2-5 FTE" --status applicant_provided
python scripts/answers.py validate --answers runs/mobidb/answers.json [--strict]

# outputs
python scripts/render_outputs.py --answers runs/mobidb/answers.json --outdir runs/mobidb/output [--submission-copy]

# refresh ELIXIR reference lists (Nodes/SDP, Communities, CDR, EDD, RIR, GCBR)
python scripts/refresh_reference_lists.py
```

| Script | Role |
|---|---|
| `run_pipeline.py` | Orchestrates the evidence phases (parallel where possible) and logs each step |
| `resolve_resource.py` | Cross-registry identity: Bioregistry, identifiers.org, re3data, bio.tools, FAIRsharing, UniProt, OpenEBench, repo discovery |
| `query_registries.py` | Europe PMC, TeSS, WorkflowHub, APICURON, OpenEBench metrics, Wayback, similar resources, BioHackathon, registry summary |
| `probe_website.py` | Bounded, robots-respecting crawl with SPA rendering and evidence snippets per topic |
| `render_pages.py` | Playwright helper (rendered DOM, form-driven screenshots) |
| `inspect_repo.py` | GitHub metadata: licence, containers, releases, contributors, Software Heritage; candidate search |
| `fair_check.py` | FAIR-Checker API + UI screenshot + local FAIR signals |
| `check_eligibility.py` | Section 1 matching against the ELIXIR reference lists (+ optional services spreadsheet) |
| `propose_answers.py` | Conservative, evidence-backed answer proposals + compact per-question digest |
| `answers.py` | init / set / patch / pending / validate the answers document |
| `render_outputs.py` | JSON, Markdown, HTML, DOCX, PDF (+ submission copy) |
| `refresh_reference_lists.py` | Rebuilds `references/elixir_reference_lists.json` (live site, Wayback fallback) |

### Design notes

- **Conservative "No" answers.** A "No" needs a conclusive lookup. A failed query or a partial crawl leads to a question for the applicant, never a negative answer.
- **Editable dropdown options.** The Checklist PDF shows the dropdowns only as "To choose". The inferred option sets live in one place, `references/ecd_checklist_schema_v1.json → option_sets`.
- **Blocked ELIXIR pages.** elixir-europe.org blocks non-browser clients, so the reference lists are fetched with a browser user agent and fall back to Wayback Machine snapshots. Every list records its source and retrieval date.
- **Known API quirks (2026-09):**
  - APICURON's documented `/api/partner-resources` returns 404, so the skill falls back to website links.
  - FAIR-Checker's API sometimes emits metric IDs as `None`, so scores are mapped by the UI's fixed metric order and flagged as such.

## Tests

```bash
pytest tests/
```

Offline tests cover:
- the schema against the Checklist source text
- the answers validator
- rendering of all formats from a fixture

## Repository structure

```
SKILL.md                 agent workflow
scripts/                 deterministic tooling (see table above)
references/              checklist schema, question guide, process summary, source texts, ELIXIR reference lists
templates/               Markdown + HTML report templates
tests/                   pytest suite + fixtures
examples/                worked example (DisProt, 2026-09-17): digest, rendered checklist, FAIR-Checker screenshot
```

## Related resources

- ECD Checklist V1: https://doi.org/10.5281/zenodo.17289009
- ECD Process V1: https://doi.org/10.5281/zenodo.17288943
- [DOME Agent Skill](https://github.com/gavinf97/dome-agent-skill): sister skill whose conventions this follows

## Citation

See [CITATION.cff](./CITATION.cff). Please also cite the ECD Checklist and Process documents.

## License

[CC BY 4.0](./LICENSE.md). The Checklist and Process texts under `references/` are © ELIXIR and their
authors, CC BY 4.0.
