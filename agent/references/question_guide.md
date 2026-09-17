# ECD Checklist — per-question answering guide

Use this in Phase 4b, together with `WORKDIR/digest.md`. The digest shows the machine
proposals and leads for each question. This guide tells you what counts as an answer and
where the traps are. Option values come from `ecd_checklist_schema_v1.json → option_sets`.

**Voice.** Write free text as the applicant: "DisProt provides…", "We maintain…". Keep it
factual and within the word limit. The Checklist says "Keep text short and succinct". Aim for
40–80 words even when the limit is 100.

**Status rules.** These apply to every question:

| Situation | status | confidence |
|---|---|---|
| Evidence shows the fact directly (a registry record, a page stating it) | `verified` | high/medium |
| Answer rests on indirect signals, or is drafted prose the applicant must own | `inferred` | medium/low |
| Only the applicant can know it | `needs_applicant` (add a `hint`) | – |
| A conclusive lookup succeeded and found nothing | `not_found`, choice `No` | medium |
| A lookup errored, or the crawl was partial | `query_failed` / `needs_applicant`, **never `No`** | – |

Every `Yes`/`Met` needs at least one evidence record with a URL. `answers.py validate` enforces this.

---

## Applicant details

| ID | Guidance |
|---|---|
| `APP.submitter_name`, `APP.submitter_email` | Always ask the applicant. Registry contacts are only hints. Never guess personal details. |
| `APP.node` | Label style `ELIXIR-Italy`, `EMBL-EBI`. Evidence is the Node whose SDP lists the resource (`eligibility.json → sdp_match`). The applicant confirms. |
| `APP.institute` | The hosting institute, e.g. "University of Padua, Department of Biomedical Sciences". Hints come from re3data institutions and recent database-paper affiliations. Mark `inferred` only if the website footer or about page names the host. |
| `APP.resource_name`, `APP.resource_url` | Set by `answers.py init`. |
| `APP.repo_url` | Use it only if it came from input, registries or a homepage link, or the user confirmed a GitHub candidate. A repo for a *related* artefact (e.g. an ontology) is not the resource's software repo. |
| `APP.community` | Must be exactly one name from the Communities reference list. Suggest the top 1–2 with reasons; the applicant picks. |
| `APP.date_submitted` | Format `dd-mm-yyyy`. It defaults to today with status `inferred`. |

## Section 1 — Eligibility

S1.1–S1.5 are **criteria pre-checks** (`in_form: false`). Only `S1.confirm` is a form field.

- **S1.1 (Node member).** Only the applicant can confirm membership. If the resource is on a Node's SDP, give that as the hint.
- **S1.2 (on the SDP).**
  - Answer `Met` + `verified` when `sdp_match.listed` holds with a homepage-domain or name match. Cite the Node page.
  - If the resource isn't matched, don't answer `Not met`. The snapshot may be stale or the name may differ, so use `needs_applicant`.
- **S1.3 (resource type).** Choose from `resource_type`, using the type signals:

  | Choice | Signals |
  |---|---|
  | Curated knowledgebase | "curated", "literature", "manually annotated" |
  | Deposition database | open data upload, "submit your data", accession numbers issued on deposit |
  | Biodata registry | a catalogue of other resources or entities |
  | Aggregation database | mainly integrates other databases |

  Status `inferred`. Explain the choice in ≤50 words in `text`.
- **S1.4 (existing status).**
  - `Not met` if `holds_existing_status` is non-empty. This is a **hard Hub rejection** (Process Appendix 3), so say it clearly in the final report.
  - `Met` if the lists were checked and found no match.
  - If the lists are more than 180 days old, lower confidence to medium.
- **S1.5 (federated/consortium).** Choice `yes_no`. Answer `Yes` only with evidence of multi-site deployment, joint branding or a consortium.
  - Several institutions in re3data is not enough on its own.
  - If `Yes`, add a hint that the applicant must contact the support email.
- **S1.confirm.** Always `needs_applicant`. If S1.4 is `Not met`, the hint must say the application would be rejected at the Hub check.

## Section 2 — Resource background

- **S2.1a (gap, 100 words).**
  - Draft from the registry descriptions and the latest database paper abstract (`registry_europepmc.json → database_papers[].abstract_excerpt`).
  - Say which scientific need is unmet without the resource, not just what it contains. Status `inferred`.
- **S2.1b (data types & entries).** Put one list item per data type, as `Type (N entries)`.
  - Take counts only from the website's statistics or release notes, or an API count. Quote the release and version in the evidence.
  - Never estimate counts. If you have types but no counts, write `Type (count: applicant to confirm)` and use `needs_applicant`.
- **S2.1c (uniqueness).**
  - **Choice:** the `uniqueness` option set.
  - **List:** only resources that genuinely serve the same gap. Judge from the candidate descriptions, and drop keyword-only matches (e.g. cell-line repositories for a protein database).
  - **Text:** what the resource does better — manual curation depth, evidence ontology, deposition route, and so on. Status `inferred`.
- **S2.1d (relevance to Community).** Use the `relevance` choice plus ≤100 words linking the resource's scope to the chosen Community's focus. Evidence can be a Community page link from the resource website. `inferred`.
- **S2.1e (database paper).** `Yes` + `verified` with links to the 1–3 most recent database papers (NAR Database issue, *Database*, *Bioinformatics*…).
- **S2.2 (go-live).**
  - Take the band from the earliest public trace: first database paper, first Wayback capture, or re3data startDate.
  - `inferred`: the official go-live date can differ, and a resource renamed or relaunched may count differently.
- **S2.3a/b (commissioned services).** `needs_applicant`. Commissioning isn't systematically public; include any lead found.
- **S2.3c (BioHackathon/AHM/other).**
  - `Yes` + `inferred` only if a lead clearly shows a project *about or using this resource*: a BioHackathon-projects issue, a BioHackrXiv report, or an AHM session.
  - Otherwise `needs_applicant`.
- **S2.4 (niche resource).** `Yes` + `inferred` when it serves one Community-scale subdomain. `No` would suggest a CDR/EDD-scale remit, so ask if in doubt.
- **S2.5, S2.6.** Applicant only.

## Section 3 — User base monitoring

- **S3.1 (uptime/response monitoring).**
  - OpenEBench monitoring shows the resource *is* monitored externally. Answer `Yes` + `inferred`, low confidence, and ask whether the team runs its own.
  - A public status page (updown.io, UptimeRobot) → `verified`.
- **S3.2 (usage metrics).** Analytics tags (Google Analytics, Matomo…) → `Yes` + `inferred`. Describe the kind of metrics only, **never numbers**; the Checklist says not to give metrics.
- **S3.3 (user base growth, 150 words).**
  - Draft from the citation trend of the resource papers, growth in literature mentions, Community size or conferences, and ingestible publications.
  - Status `inferred`. Leave it `needs_applicant` if there is nothing to go on.

## Section 4 — Development, staff & governance

- **S4.1 (roadmap/update strategy).**
  - Answer `Yes` from regular dated releases (release notes, the repo's releases), a public roadmap, or a stated update cycle. Describe the cadence, e.g. "biannual releases since 2020".
  - A news page alone → `inferred`.
- **S4.2 (feedback).** Answer `Yes` from any of:
  - a feedback form (a robots.txt `Disallow: /feedback/` is a hint only)
  - a public issue tracker
  - user surveys
  - curator or community calls

  `verified` if a page or link is shown.
- **S4.3 (helpdesk).** A help page with a contact email or ticket system → `verified`. A mailto on its own still counts ("contact email helpdesk").
- **S4.4 (who works on it).** `Yes` + `verified` when a team or about page lists names or roles; cite that page.
- **S4.5 (FTE).** Applicant only. You may hint the team-page headcount and active committers, but never pick a band yourself.
- **S4.6 (more than one institution).** `Yes` + `inferred` if the team page or recent papers show staff at several institutions working *on the resource*. Mere co-authors don't count.
- **S4.7a/b (dedicated funding).** Applicant only. Funders named in papers or site footers are hints, not proof of *current dedicated* funding. Old grants such as Horizon 2020 have often ended.
- **S4.8 (bus factor).** Applicant only. Contributor concentration is a hint.
- **S4.9 (SAB).** `Yes` + `verified` only if the site explicitly names a scientific advisory board.
- **S4.10 (privacy).** `Yes` + `verified` with a link to the privacy notice or policy.
- **S4.11 (ethics policy).**
  - `Yes` only with a real ethics or sensitive-data policy.
  - For resources holding no personal data, the applicant may answer `No` and explain; propose `needs_applicant` with that hint.

## Section 5 — Interoperability, standards & data flow

- **S5.1 (metadata standards).**
  - Name them: Bioschemas profiles (DataCatalog, Dataset, Protein…), MIAPE, MIxS, re3data-listed schemas.
  - Add FAIRsharing standard links where known.
  - Bioschemas JSON-LD on pages → `verified`.
- **S5.2 (ontologies).**
  - Choose ontologies whose CURIEs appear in entry pages or data. Check `in_ols`, and give OLS links (`https://www.ebi.ac.uk/ols4/ontologies/<id>`).
  - Resource-specific ontologies not in OLS (e.g. IDPO) still count; link their own page or repo.
- **S5.3 (structured data).** JSON-LD, JSON/XML API responses, RDF or DCAT → `Yes` + `verified`, linking an example.
- **S5.4 (API/FTP).** List the concrete access routes: REST API docs URL, bulk download or FTP, SPARQL. The API endpoint probe and API docs link together make this `verified`.
- **S5.5 (inflow).** Answer `Yes` if the resource imports or maps data from other resources (UniProt sequences, PDB structures, PubMed literature, GO terms…). The evidence is a "data sources" or "integrated resources" page, or help text. `inferred` or `verified`.
- **S5.6 (outflow).** `Yes` from:
  - UniProt cross-reference DB (DB-xxxx)
  - resources that link to or import it (InterPro, MobiDB…)
  - Bioregistry `appears_in`

  Keep the list short.
- **S5.7 (roadmapped consumers).** Applicant only. You may suggest candidates, e.g. topically related CDRs.

## Section 6 — Data & software management

- **S6.1 (public DMP).**
  - `Yes` only with a published data management plan (Zenodo, DMPonline, the website). Deposition or curation guidelines are not a DMP.
  - If nothing is found, use `needs_applicant`.
- **S6.2 (data licence).**
  - State the licence exactly as the website declares it, e.g. "CC BY 4.0", and link the licence page. The website overrides registry metadata.
  - Note any conflict in `notes`; e.g. bio.tools says CC-BY-NC but the site says CC BY 4.0.
- **S6.3 (storage/backups).** Applicant only.
- **S6.4 (version archives).** `Yes` when previous releases are downloadable or archived: release-notes history, versioned FTP folders, Zenodo snapshots, versioned API. Describe the cadence.
- **S6.5 (software management plan).**
  - `Yes` only with an explicit SMP document.
  - CONTRIBUTING/CODE_OF_CONDUCT files are good practice but not an SMP. Mention them in a hint.
- **S6.6 (software licence).**
  - Take the licence from the *confirmed* repo (SPDX name).
  - If there's no public repo, `needs_applicant`. Frontend and backend repos may differ, so list both.
- **S6.7 (containers).** `Yes` with a Dockerfile/compose in the confirmed repo, a ghcr/Docker Hub/quay image owned by the team, or BioContainers.
- **S6.8 (open source).** `Yes` when the code is public under an open licence and redeployable. A public repo with no licence → `No`/`inferred`, with a hint to add a licence.

## Section 7 — Use of ELIXIR biodatabase supports

- **S7.1 (FAIRsharing or similar registry).** A FAIRsharing record (via the Bioregistry mapping) → `Yes` + `verified` with the FAIRsharing URL. Add re3data as a second link.
- **S7.2 (identifiers.org).** Registry prefix found → `Yes` + `verified`, linking `https://registry.identifiers.org/registry/<prefix>`. Not found (the conclusive registry API) → `No` + `not_found`.
- **S7.3 (bio.tools / WorkflowHub).** The resource's own bio.tools entry counts as `Yes` (link it). WorkflowHub workflows count only if they are about or provided by the resource.
- **S7.4 (TeSS).** `Yes` + `verified` with links to TeSS materials or events titled with the resource name.
- **S7.5 (APICURON).**
  - Conditional ("if reliant on data curation"). `Not applicable` if the resource does no curation.
  - A link to APICURON on the site → `inferred` Yes. The APICURON partner page → `verified`.
- **S7.6 (LS-AAI).**
  - `Not applicable` if there is no user login at all.
  - Google, ORCID or local login without LS Login → `No`, but only after the applicant confirms (`needs_applicant` with a hint).
- **S7.7 (OpenEBench observatory).** A monitor entry exists → `Yes` + `inferred`, with the observatory link. It may have been auto-imported from bio.tools; the hint asks the applicant.
- **S7.8 (FAIR-Checker screenshot).**
  - **View the PNG** (Read tool) before accepting it. It must show the resource URL and completed "Detailed results".
  - If it does, set `image` and `links` (assessment URL) with status `verified`. Otherwise `needs_applicant`, with the manual instructions from `fairchecker.json`.
- **S7.9 (RDMkit), S7.10 (RSQkit).** Applicant only. Mentions on the site are hints.

## Section 8 — Final declaration

`S8.declaration` is always the applicant's choice. Never pre-select "agree".

## Appendix 1 — Reapplication

Only when `meta.reapplication` is true. For each section, ask the applicant for bullets on what
changed since the rejection feedback. Never invent improvements. You may suggest what to
mention by comparing the current evidence with the gaps.
