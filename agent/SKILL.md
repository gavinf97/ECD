---
name: ecd-agent-skill
description: >
  Use this skill whenever the user wants to assess a biodata resource (database, knowledgebase,
  registry) for ELIXIR Community Database (ECD) status, or to complete / pre-fill the ELIXIR
  Community Database (ECD) Checklist (application form, Zenodo 10.5281/zenodo.17289009) from a
  resource name and URL. Trigger on requests like "fill in the ECD checklist for <url>", "assess
  <database> for ECD", "ELIXIR Community Database application for <resource>", "is <resource>
  eligible for ECD status", "complete the ECD self-assessment for this database", "check <db>
  against the ECD process", or "/ecd-agent-skill". Also trigger when the user asks which ELIXIR
  registries (FAIRsharing, identifiers.org, bio.tools, TeSS, APICURON, OpenEBench, FAIR-Checker)
  a resource is registered in, as part of an ECD application.
---

# ECD Agent Skill

Pre-fills the **ELIXIR Community Database (ECD) Checklist V1**
([doi:10.5281/zenodo.17289009](https://doi.org/10.5281/zenodo.17289009)) for one biodata resource.
It works from the applicant's side, following the **ECD Process V1**
([doi:10.5281/zenodo.17288943](https://doi.org/10.5281/zenodo.17288943)). The input is a resource
**name + URL**. The output is the completed checklist as JSON, Markdown, HTML, DOCX and PDF, with
evidence behind every answer.

Division of labour:
- **Scripts** (`scripts/`) do the deterministic work: registry and API lookups, website crawl, FAIR-Checker, eligibility lists, proposals, validation and rendering.
- **You (Claude)** judge the evidence, draft short free-text answers, run the applicant Q&A and report.

Run every script from this skill's directory: `python scripts/<name>.py …`. Paths below are
relative to it. Install dependencies once with `pip install -r requirements.txt`. Playwright is
optional but strongly recommended; see Environment.

Phases: **Input → Evidence pipeline → Confirm identity → Answer → Validate → Applicant Q&A → Render → Report**.

---

## Phase 1: Input

Ask only for what is missing:
1. **Resource name** and **resource URL** (required).
2. Optional:
   - code repository URL
   - target **ELIXIR Community**: one only, from `references/elixir_reference_lists.json → communities`
   - whether this is a **reapplication** after rejection, which enables Appendix 1
3. Where to write outputs. The default is `./ecd-assessments/<slug>-<YYYYMMDD>/`.

## Phase 2: Evidence pipeline (one command, run in background)

```bash
python scripts/run_pipeline.py --name "<name>" --url "<url>" [--repo URL] [--community "<Community>"] \
       [--reapplication] [--workdir DIR] [--services-xlsx PATH]
```

It takes about 5–15 minutes; FAIR-Checker alone can take several. Run it with `run_in_background`.
It writes to `WORKDIR/`:

| File | Content |
|---|---|
| `identity.json` | Resource matched in Bioregistry, identifiers.org, re3data, bio.tools, FAIRsharing, UniProt xref DBs, OpenEBench; repo discovery |
| `evidence/registry_*.json` | Europe PMC database papers and grants, TeSS, WorkflowHub, APICURON, OpenEBench metrics, Wayback first capture, similar resources, BioHackathon leads, registry summary |
| `evidence/website.json` | Bounded, robots-respecting crawl (SPA-rendered): topic snippets (team, help, privacy, SAB, licence, API…), JSON-LD, ontology CURIEs checked against OLS, LS-AAI, analytics |
| `evidence/repo.json` | Confirmed repo licence, containers, releases, contributors, or GitHub *candidates* if none is linked |
| `evidence/fairchecker.json` + `fairchecker.png` | FAIR-Checker API scores, UI screenshot, assessment URL, local FAIR signals |
| `evidence/eligibility.json` | SDP listing and Node, CDR/EDD/RIR/GCBR matches, resource-type and federation signals, Community suggestions |
| `answers.json` | The answers document (75 question records) |
| `proposals.json` | Deterministic answer proposals |
| `digest.md` | **Compact per-question digest: read this first** |

`--services-xlsx` optionally adds an enriched ELIXIR services spreadsheet (sheet "Services") as a
second SDP source.

If `evidence/eligibility.json → reference_lists_stale` is true (lists more than 180 days old), run
`python scripts/refresh_reference_lists.py` and then re-run `check_eligibility.py` and `propose_answers.py`.

## Phase 3: Confirm identity

Read `identity.json → needs_confirmation` and the top of `digest.md`.

- **Code repository.** If no repo was linked and `evidence/repo.json` lists candidates, ask the user which one (if any) is the resource's code. Then re-run `python scripts/inspect_repo.py --identity WORKDIR/identity.json --repo <url> --out WORKDIR/evidence/repo.json` and `propose_answers.py`.
- **Ambiguous registry match.** If Bioregistry or bio.tools matched more than one plausible entry, confirm with the user before relying on it.

Never treat an unconfirmed candidate repo as the resource's software.

## Phase 4: Answer

1. Read `WORKDIR/digest.md` and `references/question_guide.md`.
2. Open specific `evidence/*.json` files only where a digest line points to them.
3. Start from `proposals.json`. For every question, write a patch entry into `WORKDIR/answers_patch.json` (object `{qid: {…}}`):
   - **Proposals:** accept, correct or downgrade each one. A proposal is a starting point, not a verdict.
   - **"CLAUDE: decide/draft" items:** draft these from the leads and evidence (S1.3, S1.5, S2.1a–d, S2.4, S3.3, S4.1, S4.2, S4.4, S4.6, S5.5, S6.1, S6.2, S6.5…).
   - **Crawl gaps:** where the crawl missed a page you need (statistics, data sources, team, privacy), you may `WebFetch` the specific page URL. Add it as an evidence record `{"source": "webfetch", "url": …, "snippet": …}`.
   - **S7.8 screenshot:** **view `fairchecker.png` with the Read tool** before accepting it.
4. Apply the patch:
   ```bash
   python scripts/answers.py patch --answers WORKDIR/answers.json --patch WORKDIR/proposals.json
   python scripts/answers.py patch --answers WORKDIR/answers.json --patch WORKDIR/answers_patch.json
   ```

Record fields are `choice`, `text`, `list`, `links`, `image`, `status`, `confidence`, `evidence` (list of
`{source,url,snippet}`), `hint` and `notes`. Status meanings and rules are in `scripts/answers.py`
and the guide.

## Phase 5: Validate

```bash
python scripts/answers.py validate --answers WORKDIR/answers.json
```

Fix every error: word limits, invalid options, Yes without evidence, No resting on a failed query.
Warnings are advisory.

## Phase 6: Applicant Q&A (flag + ask)

```bash
python scripts/answers.py pending --answers WORKDIR/answers.json
```

1. Briefly tell the user how many items need their input. Offer to go through them now, or to leave them flagged as `[Applicant to complete]`.
2. **Choice items:** batch them into `AskUserQuestion` calls, at most 4 questions per call, grouped by section.
   - Use the schema option values as options.
   - When a set has more than 4 values, offer the 3 most plausible plus the automatic "Other".
   - Put the evidence hint in the option description, e.g. "Team page lists 9 people".
3. **Free-text, list or link items:** ask in one consolidated message listing the question ids and word limits. The user may answer any subset.
4. Apply the answers with `answers.py set` or `patch`, using `status: applicant_provided`. Unanswered items stay `needs_applicant`.
5. **Declarations:** `S1.confirm` and `S8.declaration` are only ever set from an explicit user answer.
6. **Inferred items:** offer (don't force) a quick review pass over them (`pending --include-inferred`), because the applicant owns the drafted prose.

## Phase 7: Render

```bash
python scripts/render_outputs.py --answers WORKDIR/answers.json --outdir WORKDIR/output
```

This produces `ECD_<slug>_checklist.{json,md,html,docx,pdf}`:
- The **DOCX/PDF** mirror the official Checklist layout. Unresolved items are highlighted, and an evidence appendix is appended.
- The **HTML** is a self-contained report with status chips and collapsible evidence.

Once `answers.py validate --strict` passes (nothing unresolved, declarations made), offer
`--submission-copy`. It renders a clean DOCX/PDF with no statuses or appendix. The HTML report can
be offered as a published artifact.

## Phase 8: Report

Reply briefly with:
- **Resource identity:** the registries it is found in.
- **Status counts:** verified, inferred, applicant-provided, still-needed.
- **Hub-blocking issues first**, e.g. S1.4 already an EDD/CDR, not on the SDP, or incomplete fields. Cite Process Appendix 3.
- **Weak points reviewers look for:** the Appendix 3 scientific/service criteria. Examples: no API *and* no ontologies (data silo), unclear licence, single-person dependency, no roadmap/SAB/feedback.
- **Paths** to the output files.
- **Where to submit:** the PDF goes to `elixir-community-databases@elixir-europe.org`, **by the applicant**. Never send email yourself.

---

## Environment

| Variable / tool | Purpose |
|---|---|
| Playwright (`pip install playwright && playwright install chromium`) or `ECD_PLAYWRIGHT_PYTHON=/path/to/python-with-playwright` | Renders single-page-app websites and takes the FAIR-Checker screenshot. Without it the crawl reports `render_mode: spa_unrendered` and S7.8 falls back to manual instructions. |
| `GITHUB_TOKEN` or a logged-in `gh` CLI | Higher GitHub API rate limits (repo inspection, BioHackathon search) |
| `FAIRSHARING_USERNAME` / `FAIRSHARING_PASSWORD` | Optional. Richer FAIRsharing record detail; presence is detected via Bioregistry without it |
| `ECD_CACHE_DIR` | Cache for the Bioregistry dump (default `~/.cache/ecd-agent-skill`) |

## Reference files

| File | When to read |
|---|---|
| `references/question_guide.md` | Phase 4: what counts as an answer per question, status rules, traps |
| `references/ecd_checklist_schema_v1.json` | Exact question ids, verbatim prompts, parts, word limits, **option sets (edit here)** |
| `references/ecd_process_summary.md` | Process steps and Appendix 3 rejection criteria (Phase 8 report) |
| `references/ecd_checklist_v1_text.txt`, `references/ecd_process_v1_text.txt` | Full source texts when wording matters |
| `references/elixir_reference_lists.json` | Nodes + SDP services, Communities, CDR/EDD/RIR/GCBR snapshot (dated) |

## Anti-hallucination rules

- **No invented facts.** Never invent entry counts, FTE, funding, dates, licences, registry IDs or URLs. If no API response, page snippet or user answer supports a value, it stays empty with `needs_applicant`.
- **Absence is not a No.** A failed lookup or a partial crawl is never a "No". Only conclusive registry lookups (identifiers.org, TeSS search) can give `not_found` → "No".
- **Evidence for every positive.** Every `Yes`/`Met` carries at least one evidence record with a URL. Drafted prose is `inferred` until the applicant accepts it.
- **Declarations are the applicant's.** Never pre-select the eligibility confirmation or the final declaration.
- **Confirm the repo.** Candidate repositories, container images and "similar resources" are leads that need confirmation or judgement, not answers.
- **Screenshots must be viewed.** Never use a FAIR-Checker screenshot you have not looked at. Never present local FAIR signals as FAIR-Checker results.
- **The applicant submits.** Never send the application, email anyone, or register the resource anywhere.
