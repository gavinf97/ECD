# ELIXIR Community Database (ECD) Checklist — DisProt

*Checklist Version 1 - July, 2025 ([doi:10.5281/zenodo.17289009](https://doi.org/10.5281/zenodo.17289009)) · Process [doi:10.5281/zenodo.17288943](https://doi.org/10.5281/zenodo.17288943)*
*Pre-filled by the ECD Agent Skill on 2026-09-17T16:25:40+00:00 for <https://disprot.org>. Review every answer before submission.*

**Status:** needs_applicant: 28 · inferred: 17 · verified: 23**Still needs applicant input (28):** APP.community, APP.repo_url, APP.submitter_email, APP.submitter_name, S1.1, S1.confirm, S2.3a, S2.3b, S2.5, S2.6, S4.11, S4.2, S4.5, S4.6, S4.7a, S4.7b, S4.8, S5.7, S6.1, S6.3, S6.5, S6.6, S6.7, S6.8, S7.10, S7.6, S7.9, S8.declaration

## Applicant details

| Field | Value | Status |
|---|---|---|
| Submitter(s) name | [Applicant to complete] | Applicant input needed |
| Submitter(s) email | [Applicant to complete] | Applicant input needed |
| ELIXIR Node(s) | ELIXIR-Italy | Inferred – review |
| ELIXIR Institute(s) | University of Padua, Department of Biomedical Sciences (BioComputing UP) | Inferred – review |
| Resource name | DisProt | Verified |
| Resource weblink | https://disprot.org | Verified |
| Resource software repo (e.g. GitHub) | [Applicant to complete] | Applicant input needed |
| ELIXIR Community submitted to | [Applicant to complete] | Applicant input needed |
| Date submitted | 17-09-2026 | Inferred – review |
## Section 1: Eligibility check

> Please read the following eligibility requirements before completing this application. For any questions or uncertainties please contact: elixir-community-databases@elixir-europe.org.


**1. The primary applicant is a member of an ELIXIR Node & Node institute (check here).** *(eligibility criterion — pre-check)*
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* Resource is on the ELIXIR-Italy SDP; confirm the primary applicant belongs to that Node and a Node institute.


**2. The applicant is submitting an ELIXIR Node Service as listed on the ELIXIR SDP (check here).** *(eligibility criterion — pre-check)*
- Answer: **Met**
- Response [50 words]: Listed as 'DisProt' under ELIXIR-Italy on the ELIXIR SDP.
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - elixir-sdp: <https://elixir-europe.org/about-us/who-we-are/nodes/italy> — “DisProt (http://www.disprot.org/)”


**3. The service being submitted contains biological data and is one of the following: a. A deposition database (public store of biodata) b. A curated knowledgebase (curated biodata information extracted from literature) c. A biodata registry d. An aggregation database** *(eligibility criterion — pre-check)*
- Answer: **Curated knowledgebase**
- Response [50 words]: Manually curated repository of experimentally validated disorder annotations extracted from literature; also offers a deposition route (ELIXIR EDD).
- *Status:* Inferred – review · *confidence:* medium
- *Evidence:*
    - rendered-page: <https://disprot.org/> — “DisProt is the major manually curated repository of Intrinsically Disordered Proteins ... Expert curators are involved in collecting experimentally confirmed biological data”
    - re3data: <https://www.re3data.org/repository/r3d100010561> — “curated database ... annotating protein sequences for intrinsically disorder regions from the literature”


**4. The service does not already hold a status of: a. Core Data Resource (CDR) b. ELIXIR Deposition Database (EDD) c. Global Core Biodata Resource (GCBR) d. Recommended Interoperability Resource (RIR)** *(eligibility criterion — pre-check)*
- Answer: **Not met**
- Response [50 words]: Resource already holds: ELIXIR Deposition Database (EDD).
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - elixir-status-list: <https://elixir-europe.org/platforms/data/elixir-deposition-databases> — “ELIXIR Deposition Database (EDD): MATCH ['DisProt']”


**5. For federated and consortia databases (multi-site, multi-branding, non-ELIXIR Involvement), please contact the support email to determine eligibility.** *(eligibility criterion — pre-check)*
- Is the resource a federated/consortium database?: **No**
- Response [50 words]: Single deployment operated by BioComputing UP (University of Padua) with an international curator consortium; no multi-site or multi-branded instance found.
- *Status:* Inferred – review · *confidence:* medium
- *Evidence:*
    - rendered-page: <https://disprot.org/download> — “BioComputing UP, 2021 - University of Padua, Italy”
    - re3data: <https://www.re3data.org/repository/r3d100010561> — “5 institutions listed (ITA, USA), historical”


** I confirm that my biodata resource is eligible under the above criteria:**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* Pre-check blocks eligibility: ELIXIR Deposition Database (EDD)

## Section 2: Resource Background

**1. Biodata resource key info:**

**1.a Gap your resource serves:**
- Response [100 words]: Intrinsically disordered proteins and regions lack a fixed 3D structure, so they are poorly captured by structure-centred resources and cannot be characterised reliably by prediction alone. DisProt fills this gap as the reference, manually curated collection of experimentally validated disorder, linking each region to its detection method (ECO), structural state, function and transitions (IDPO, GO) and supporting publication. These gold-standard annotations underpin disorder predictor benchmarking (e.g. CAID) and are cross-referenced from UniProtKB.
- *Status:* Inferred – review · *confidence:* medium
- *Evidence:*
    - rendered-page: <https://disprot.org/> — “major manually curated repository of Intrinsically Disordered Proteins, both for structural and functional aspects”
    - rendered-page: <https://disprot.org/download> — “Release 2018_11 (CAID)”
    - uniprot: <https://www.uniprot.org/database/DB-0017> — “UniProt cross-referenced database”


**1.b Biological data type(s) held & total entries:**
- List:
    - Intrinsically disordered proteins (3,337 entries; release 2026_06)
    - Disordered region annotations by lineage: Eukaryota (10,568), Bacteria (1,788), Viruses (1,527), Archaea (100)
    - GO function/process/component region annotations (4,329 / 712 / 72)
    - Thematic datasets, e.g. NDDs-related (357), RNA-binding (221), Condensates-related (189) proteins
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - rendered-page: <https://disprot.org/> — “Version: 9.10 Release: 2026_06 Number of entries: 3337”
    - rendered-page: <https://disprot.org/release-notes> — “Taxonomy ... Viruses 235 1,527 Eukaryota 2,580 10,568 Bacteria 498 1,788 Archaea 23 100; GO Molecular function 1296 4329”
    - rendered-page: <https://disprot.org/> — “Datasets ... RNA-binding proteins 221 Condensates-related proteins 189 NDDs-related proteins 357”


**1.c Uniqueness:**
- Answer: **Partially overlapping with other resources**
- List overlapping resources serving the same gap:
    - MobiDB (aggregated curated and predicted disorder annotations)
    - Protein Ensemble Database (PED; conformational ensembles of IDPs)
    - IDEAL (curated IDP database)
- State what your resource does better than resources serving the same gap [100 words]: DisProt is dedicated to manual, literature-based curation of experimentally validated disorder at region level, with every annotation tied to an ECO evidence code, IDPO/GO terms, MIADE information and a curator-review workflow, released twice a year with archived versions. MobiDB aggregates curated and predicted disorder, and PED stores structural ensembles rather than curated evidence.
- *Status:* Inferred – review · *confidence:* medium
- *Evidence:*
    - registry:similar: <https://bio.tools/api/tool/?topicID=%22topic_3542%22> — “bio.tools databases sharing topic 'Protein disordered structure': MobiDB, Protein Ensemble Database, ComSin, IDEAL”
    - rendered-page: <https://disprot.org/release-notes> — “430 annotations have MIADE information ... Enhanced curation review workflow”


**1.d Relevance to designated ELIXIR Community:**
- Answer: **High**
- Response [100 words]: DisProt is the reference curated database for intrinsically disordered proteins, the exact focus of the ELIXIR Intrinsically Disordered Proteins Community, and describes itself as a service of the IDP Community. It provides the community's shared annotation standard (IDPO, MIADE-compliant curation), training materials and benchmark data for disorder prediction.
- *Status:* Inferred – review · *confidence:* high
- *Hint:* Assumes the application goes to the Intrinsically Disordered Proteins Community.
- *Evidence:*
    - rendered-page: <https://disprot.org/> — “The DisProt database is part of the ELIXIR infrastructure, service of the IDP Community and ELIXIR deposition database”
    - website:elixir-link: <https://elixir-europe.org/communities/intrinsically-disordered-proteins> — “linked from the DisProt website”


**1.e Peer-reviewed article on your database itself (e.g. NAR Database/+)**
- Answer: **Yes**
- If yes: provide link: <https://doi.org/10.1093/nar/gkaf1175>, <https://doi.org/10.1093/nar/gkad928>, <https://doi.org/10.1093/database/baae009>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - europepmc: <https://doi.org/10.1093/nar/gkl893> — “DisProt: the Database of Disordered Proteins. — Nucleic acids research 2007”
    - europepmc: <https://doi.org/10.1093/nar/gkw1056> — “DisProt 7.0: a major update of the database of disordered proteins. — Nucleic acids research 2017”
    - europepmc: <https://doi.org/10.1093/nar/gkz975> — “DisProt: intrinsic protein disorder annotation in 2020. — Nucleic acids research 2020”
    - europepmc: <https://doi.org/10.1093/bioinformatics/bth476> — “DisProt: a database of protein disorder. — Bioinformatics (Oxford, England) 2005”


**2. How long ago did your resource officially go live?**
- Answer: **More than 10 years**
- *Status:* Inferred – review · *confidence:* medium
- *Hint:* Earliest public trace 2005; confirm the official go-live year.
- *Evidence:*
    - europepmc — “earliest paper about resource: 2005”
    - wayback: <http://web.archive.org/web/20050304063048/http://www.disprot.org:80/> — “first archived capture 20050304063048”

**3. Has your resource been part of:**

**3.a A funded ELIXIR Community Commission Service work plan?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* ELIXIR commissioned-service participation is not systematically public; ask the applicant.


**3.b A funded ELIXIR CMR/BFSP/HDTR Science Tier Commission Service work plan?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* ELIXIR commissioned-service participation is not systematically public; ask the applicant.


**3.c An ELIXIR BioHackathon project /AHM workshop/ other?**
- Answer: **Yes**
- If yes: provide short description/link [100 words]: DisProt data and Bioschemas markup featured in ELIXIR BioHackathon work, e.g. 'Exploiting Bioschemas Markup to Populate IDPcentral' and Bioschemas DataCatalog/Dataset examples (BioHackathon-projects-2019).
- Link(s): <https://doi.org/10.37044/osf.io/v3jct>, <https://github.com/elixir-europe/BioHackathon-projects-2019/pull/45>
- *Status:* Inferred – review · *confidence:* medium
- *Hint:* Confirm the DisProt team took part and add any AHM workshops.
- *Evidence:*
    - europepmc: <https://doi.org/10.37044/osf.io/v3jct> — “Exploiting Bioschemas Markup to Populate IDPcentral”
    - github: <https://github.com/elixir-europe/BioHackathon-projects-2019/pull/45> — “Added DataSet/DataCatalog and DataRecord examples”


**4. Is your resource a niche biodata resource of use by a narrower life science subdomain e.g. aligned under one of the ELIXIR Community focus areas?**
- Answer: **Yes**
- *Status:* Inferred – review · *confidence:* high
- *Evidence:*
    - rendered-page: <https://disprot.org/> — “database of intrinsically disordered proteins ... service of the IDP Community”


**5. Do you believe there is scope for your resource to eventually mature into a CDR/EDD scale resource (e.g. ENA/UniProt/+)?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed


**6. Have you already applied for CDR/EDD status?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed

## Section 3: User base monitoring


**1. Do you have resource monitoring in place? e.g. for uptime & response time metrics.**
- Answer: **Yes**
- If yes: provide short description [100 words]: Uptime and response time are tracked by the OpenEBench monitoring service.
- *Status:* Inferred – review · *confidence:* low
- *Hint:* External monitoring (OpenEBench) found; confirm whether the team runs its own uptime/response-time monitoring.
- *Evidence:*
    - openebench: <https://openebench.bsc.es/observatory/Tool/disprot> — “OpenEBench monitor: last month uptime 30 d, downtime 0 d, avg access 701 ms”


**2. Are you tracking any quantitative resource usage data metrics? e.g. monthly users/+**
- Answer: **Yes**
- If yes: provide short description (do not provide any metrics) [100 words]: Web usage analytics are collected (Google Analytics / Tag Manager).
- *Status:* Inferred – review · *confidence:* medium
- *Hint:* Analytics tags detected; confirm which usage metrics are tracked (do not report numbers).
- *Evidence:*
    - website:analytics: <https://disprot.org/> — “analytics tags detected: ['Google Analytics / Tag Manager']”


**3. Have you considered the possible user base growth of your target domain community?**
- Answer: **Yes**
- If yes: provide short description, e.g. i. Active user growth trends ii. Conference sizes iii. Publications & possible ingestible data iv. Other... [150 words]: Papers describing DisProt have been cited over 1,600 times (Europe PMC) and literature mentions of disprot.org have risen since 2020. Interest in disorder is growing with research on biomolecular condensates and phase separation and with protein language model predictors that need curated reference data (CAID rounds). Each release still adds substantial new literature: release 2026_06 added 151 proteins, 796 pieces of evidence and 208 newly curated publications, showing a continuing supply of ingestible data.
- *Status:* Inferred – review · *confidence:* medium
- *Evidence:*
    - europepmc: <https://europepmc.org/search?query=TITLE%3A%22DisProt%22> — “total citations of resource papers: 1630; domain mentions/year 2020:2 ... 2022:11, 2024:8, 2026:5”
    - rendered-page: <https://disprot.org/release-notes> — “Version 9.10 - June 2026 ... New pieces of evidence: 796 New proteins: 151 ... New publications: 208”
    - rendered-page: <https://disprot.org/> — “Condensates-related proteins 189”

## Section 4: Development, Staff & Governance


**1. Do you have a resource update strategy or development roadmap?**
- Answer: **Yes**
- If yes: provide short description [100 words]: Twice-yearly data releases (June and December) with public release notes and changelog. Each release adds curated proteins and evidence plus planned improvements, e.g. 9.10 (June 2026): a new thematic dataset, a GAF 2.2 export rewrite and a new download page.
- Link(s): <https://disprot.org/release-notes>, <https://disprot.org/download>
- *Status:* Verified · *confidence:* medium
- *Hint:* No public forward-looking roadmap found; add it if one exists.
- *Evidence:*
    - rendered-page: <https://disprot.org/download> — “Release: 2026_06 (Current) 2025_12 2025_06 2024_12 2024_06 2023_12 2023_06 2022_12 2022_06 ...”
    - rendered-page: <https://disprot.org/release-notes> — “Changelog Version 9.10 - June 2026 ... GAF export was rewritten ... New Download page”


**2. Does your resource collect user base feedback and community input for its development roadmap?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* robots.txt disallows /feedback/ (suggests a feedback page); curator consortium and training events may also collect community input.


**3. Does your resource have a helpdesk?**
- Answer: **Yes**
- If yes: provide short description [100 words]: Help pages document search, downloads and the REST API; enquiries are handled through the info@disprot.org contact address.
- Link(s): <https://disprot.org/help>, <https://disprot.org/about>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - rendered-page: <https://disprot.org/help> — “This section describes how to use the DisProt website ... RESTful endpoints”
    - website:helpdesk: <https://disprot.org/about> — “Contact us For enquiries related to the DisProt, please email: info@disprot.org”


**4. Does your resource have details publicly available about who works on your resource?**
- Answer: **Yes**
- Response [100 words]: The About page lists current team members with roles (curators, web developers, system administrator) and the Scientific Advisory Board.
- Link(s): <https://disprot.org/about>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - website:team: <https://disprot.org/about> — “Web developer (Junior Post-doc) ... Web developer intern ... System administrator & support”


**5. How many people (approximate in FTE) work on your resource?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed


**6. Is the resource operated across more than one institution?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* re3data lists University of Padua plus historical US institutions (Indiana, Temple); recent papers include HUN-REN (Hungary) co-authors of the DisProt Consortium. Confirm whether operation (not just curation) spans institutions.

**7. Does your resource have dedicated funding to:**

**7.a Retain staff to curate data, maintain & update it?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* Funders acknowledged in resource papers (not proof of current dedicated funding): [['Horizon 2020', 6], ['Hungarian Academy of Sciences', 4], ['Hungarian Scientific Research Fund', 4], ['European Union', 4], ['NLM NIH HHS', 3], ['National Research, Development and Innovation Fund of the Ministry of Culture and Innovation', 3]] | website: … our upcoming training sessions. BioComputing UP, 2021 - University of Padua, Italy License and disclaimer This database is part of a project that has received funding from the European Union’s Horiz


**7.b Provide dedicated hardware to keep it live & online (at least for next 2 years)?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed


**8. Do you know how many of your team members would have to leave the project for the resource to stop further development/new data ingestion?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed


**9. Does your resource have a scientific advisory board (SAB)?**
- Answer: **Yes**
- If yes: provide short description/link [100 words]: DisProt operates with an international, independent Scientific Advisory Board, described on the About page.
- Link(s): <https://disprot.org/about>
- *Status:* Verified · *confidence:* medium
- *Evidence:*
    - website:sab: <https://disprot.org/about> — “…- Web developer András Hatos - Web developer Edoardo Salladini - Senior curator Contact us For enquiries related to the DisProt, please email: info@disprot.org Scientific Advisory Board (SAB) DisProt is an organization that operates with a”


**10. Does your resource have a privacy statement?**
- Answer: **Yes**
- If yes: provide short description/link [100 words]: A privacy notice on the About page explains what personal data DisProt collects, for what purposes, and how it is processed and secured.
- Link(s): <https://disprot.org/about>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - website:privacy: <https://disprot.org/about> — “… at Khoury College of Computer Sciences, Northwestern University License This work is licensed under a Creative Commons Attribution 4.0 International License . Privacy notice This privacy notice explains what personal data is collected by ”


**11. Does your resource have an ethics policy? (e.g. for sensitive data)**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* No ethics policy found; DisProt holds no personal or sensitive data, so the applicant may answer No and explain.

## Section 5: Interoperability, Standards & Data flow


**1. Does your resource use metadata standards for its data?**
- Answer: **Yes**
- If yes: provide short description/link(s) (FAIRsharing standard link if available) [100 words]: Entry pages carry schema.org/Bioschemas markup (DataCatalog, Dataset, Protein). GO annotations are exported in GAF 2.2, and curation follows the MIADE minimum information guidelines for disorder experiments.
- Link(s): <https://disprot.org/DP00003>, <https://doi.org/10.1038/s41592-023-01915-x>
- *Status:* Verified · *confidence:* high
- *Hint:* Name the actual standards (e.g. Bioschemas profile, MIAPE) and add FAIRsharing standard links.
- *Evidence:*
    - website:json-ld: <https://disprot.org/DP00003> — “JSON-LD types: DataCatalog, Dataset, Protein”
    - rendered-page: <https://disprot.org/release-notes> — “GAF export was rewritten ... according to the GAF 2.2 specification ... 430 annotations have MIADE information”
    - rendered-page: <https://disprot.org/about> — “Minimum information guidelines for experiments structurally characterizing intrinsically disordered protein regions (2023) Nature Methods”


**2. Does your resource use an ontology for its data?**
- Answer: **Yes**
- If yes: provide short description/link(s) (Ontology Lookup Service link if available) [100 words]: Annotations use the IDP Ontology (IDPO) for structural state, function and transitions, the Evidence & Conclusion Ontology (ECO) for detection methods, and the Gene Ontology (GO); organisms follow NCBI Taxonomy.
- Link(s): <https://disprot.org/ontology>, <https://github.com/BioComputingUP/idpo>, <https://www.ebi.ac.uk/ols4/ontologies/eco>, <https://www.ebi.ac.uk/ols4/ontologies/go>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - website:curie: <https://disprot.org/DP00003> — “ECO terms found 14x; in OLS: Evidence & Conclusion Ontology (ECO)”
    - website:curie: <https://disprot.org/DP00003> — “GO terms found 3x; in OLS: Gene Ontology”
    - rendered-page: <https://disprot.org/download> — “The IDP ontology (IDPO) is available to download on its dedicated GitHub repository”
    - rendered-page: <https://disprot.org/release-notes> — “The taxonomic classification of DisProt relies on the NCBI Taxonomy service”


**3. Does your resource expose structured data (e.g. JSON/W3C/DCAT)?**
- Answer: **Yes**
- If yes: provide short description/link(s) [100 words]: Entry pages embed schema.org/Bioschemas JSON-LD; the REST API and bulk downloads provide JSON, TSV, FASTA and GAF.
- Link(s): <https://disprot.org/DP00003>, <https://disprot.org/download>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - website:json-ld: <https://disprot.org/DP00003> — “schema.org/Bioschemas JSON-LD types: ['DataCatalog', 'Dataset', 'Protein']”
    - rendered-page: <https://disprot.org/download> — “Format: TSV FASTA JSON GAF”


**4. Does your resource provide an API/FTP/other protocols for exposing and retrieving the data in a machine actionable manner?**
- Answer: **Yes**
- If yes: provide short list:
    - REST API (documented under Help): https://disprot.org/help
    - Bulk downloads of current and archived releases (TSV, FASTA, JSON, GAF): https://disprot.org/download
    - Resolvable identifiers via identifiers.org (disprot:DPxxxxx)
- *Status:* Verified · *confidence:* high
- *Hint:* Add download/FTP and documentation links if available.
- *Evidence:*
    - website:api-endpoint: <https://disprot.org/api/> — “application/json: "Hello from legacy"”
    - re3data:api: <https://www.disprot.org/help#anchor3> — “re3data API type REST”
    - website:api: <https://disprot.org/help> — “…es used in DisProt to describe structural, functional and technique or evidence of IDPs/IDRs. Information about RESTful endpoints and the output format see the API documentation below. Training materials for DisProt users DisProt webinars ”
    - website:api-link: <https://disprot.org/api> — “API documentation page -> https://disprot.org/api”
    - website:download: <https://disprot.org/download> — “DisProt Browse Training Ontology Release notes Download Deposition About Help Annotated Proteins Release: 2026_06 (Current) 2025_12 2025_06 2024_12 2024_06 2023_12 2023_06 2022_12 2022_06 2022_03 2021_12 2021_08 202…”
    - bio.tools: <https://bio.tools/disprot> — “bio.tools toolType includes 'Web API'”


**5. Does your resource pull data from other data resources? (inflow of data)**
- Answer: **Yes**
- If yes: provide short list:
    - UniProtKB (protein accessions and sequences)
    - NCBI Taxonomy (organism classification)
    - PubMed (literature references for curated evidence)
    - AlphaFold DB (predicted-structure confidence content)
    - GO and ECO ontologies
- *Status:* Inferred – review · *confidence:* medium
- *Evidence:*
    - rendered-page: <https://disprot.org/download> — “Columns: UniProt ACC ... NCBI Taxon ID ... Term ID ... ECO Term ID ... PMID ... Alphafold Very Low confidence content”
    - rendered-page: <https://disprot.org/release-notes> — “The taxonomic classification of DisProt relies on the NCBI Taxonomy service”


**6. Do other resources pull data from your resource? (outflow of data)**
- Answer: **Yes**
- If yes: provide short list:
    - UniProtKB cross-references (DB-0017)
    - Gene Ontology knowledgebase (GO annotations exported as GAF)
- *Status:* Verified · *confidence:* medium
- *Hint:* Add other consumers (e.g. MobiDB, InterPro) if confirmed.
- *Evidence:*
    - uniprot: <https://www.uniprot.org/database/DB-0017> — “Database of protein disorder is a UniProt cross-referenced database (Family and domain databases)”
    - rendered-page: <https://disprot.org/release-notes> — “The GAF export was rewritten to ensure correct release of GO annotations”
    - rendered-page: <https://disprot.org/about> — “DisProt & Collaborative publications: The Gene Ontology knowledgebase in 2026”


**7. Have you identified/roadmapped existing (ELIXIR) biodata resources that could augment their database entries by pulling in your data?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed

## Section 6: Data & Software Management

### Data

**1. Do you have a publicly available data management plan?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* No public data management plan found on the website or Zenodo.


**2. What is the license for use of the data in your resource?**
- Provide short description [100 words]: DisProt data are licensed under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
- Link(s): <https://creativecommons.org/licenses/by/4.0/>, <https://disprot.org/about>
- *Status:* Verified · *confidence:* high
- *Hint:* Claude: state the exact data licence named on the website (prefer the site over registries).
- *Evidence:*
    - website:license: <https://disprot.org/> — “…Tompa, Damiano Piovesan, Silvio C E Tosatto, Maria Cristina Aspromonte (2025) Nucleic Acids Research, Database Issue. PubMed:41249866 , DOI:10.1093/nar/gkad928 License This work is licensed under a Creative Commons Attribution 4.0 Internat”
    - website:license-link: <http://creativecommons.org/licenses/by/4.0/> — “(no text) -> http://creativecommons.org/licenses/by/4.0/”
    - website:license: <https://disprot.org/training> — “…hannel Zenodo Community Other Recorded tutorials Materials For Curators And Users Datasets Crediting Contact BioComputing UP, 2021 - University of Padua, Italy License and disclaimer This database is part of a project that has received fun”


**3. Do you have a clear plan for long-term storage and off-site backups?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed


**4. Do you maintain version archives of the database contents?**
- Answer: **Yes**
- If yes: provide short description [100 words]: Every release is archived and downloadable from the Download page, from 2016_10 (DisProt 7) to the current 2026_06, in TSV, FASTA, JSON and GAF, with release notes for each version.
- Link(s): <https://disprot.org/download>, <https://disprot.org/release-notes>
- *Status:* Verified · *confidence:* high
- *Hint:* Describe release cadence and where previous releases are archived.
- *Evidence:*
    - rendered-page: <https://disprot.org/download> — “Release: 2026_06 (Current) 2025_12 ... 2019_09 2018_11 (CAID) 2016_10 (DisProt 7) ... Format: TSV FASTA JSON GAF”

### Software

**5. Do you have a publicly available software management plan?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* No software management plan found; IDPO repo has CONTRIBUTING/CODE_OF_CONDUCT only.


**6. What is the license for use of the software of your resource?**
- Provide short description [100 words]: [Applicant to complete]
- *Status:* Applicant input needed
- *Hint:* No confirmed code repository.


**7. Is your data resource's software available in containerised format for reuse? (eg: Docker image/Podman/Singularity)**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* No confirmed code repository.


**8. Is your data resource's software open source? (i.e. the code base is reusable and available to redeploy?)**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* No confirmed code repository.

## Section 7: Use of ELIXIR Biodatabase Supports


**1. Is your resource listed in a database registry such as FAIRsharing?**
- Answer: **Yes**
- If yes: provide link: <https://fairsharing.org/FAIRsharing.dt9z89>, <https://www.re3data.org/repository/r3d100010561>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - fairsharing: <https://fairsharing.org/FAIRsharing.dt9z89> — “FAIRsharing record FAIRsharing.dt9z89 (via ['bioregistry_mapping'])”


**2. Does your resource have its identifiers registered in identifiers.org?**
- Answer: **Yes**
- If yes: provide link: <https://registry.identifiers.org/registry/disprot>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - identifiers.org: <https://registry.identifiers.org/registry/disprot> — “prefix disprot (MIR:00000199)”


**3. Are any analysis tools & workflows provided by your resource registered in relevant registries such as bio.tools and WorkflowHub?**
- Answer: **Yes**
- If yes: provide link: <https://bio.tools/disprot>
- *Status:* Verified · *confidence:* medium
- *Hint:* bio.tools entry found; add any separate tools/workflows the resource provides.
- *Evidence:*
    - bio.tools: <https://bio.tools/disprot> — “bio.tools entry disprot (['Web API', 'Web application', 'Database portal'])”


**4. Are any training materials for your resource registered in TeSS?**
- Answer: **Yes**
- If yes: provide link: <https://tess.elixir-europe.org/materials/an-introduction-to-disprot-03344576-ed76-48c7-ac18-ec18365060c9>, <https://tess.elixir-europe.org/materials/exploring-structural-and-functional-annotations-of-idps-with-disprot-a2647e13-bfac-4320-b319-695e51f68573>, <https://tess.elixir-europe.org/materials/experimental-techniques-for-the-characterization-of-intrinsically-disordered-proteins>
- *Status:* Verified · *confidence:* high
- *Evidence:*
    - tess: <https://tess.elixir-europe.org/materials/an-introduction-to-disprot-03344576-ed76-48c7-ac18-ec18365060c9> — “An introduction to DisProt”
    - tess: <https://tess.elixir-europe.org/materials/exploring-structural-and-functional-annotations-of-idps-with-disprot-a2647e13-bfac-4320-b319-695e51f68573> — “Exploring structural and functional annotations of IDPs with DisProt”
    - tess: <https://tess.elixir-europe.org/materials/experimental-techniques-for-the-characterization-of-intrinsically-disordered-proteins> — “Experimental techniques for the characterization of Intrinsically Disordered Proteins”
    - tess: <https://tess.elixir-europe.org/materials/biocuration-in-disprot> — “Biocuration in DisProt”


**5. If reliant on data curation does your resource use APICURON for curator credit and recognition?**
- Answer: **Yes**
- If yes: provide link: <https://apicuron.org/>
- *Status:* Inferred – review · *confidence:* medium
- *Hint:* Website links to APICURON; confirm curator credit is actually submitted and add the APICURON resource page link.
- *Evidence:*
    - website:apicuron-link: <https://apicuron.org/> — “resource website links to APICURON”


**6. If reliant on a user authentication and authorisation infrastructure (AAI) service, do you use LS-AAI?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed
- *Hint:* No LS Login detected. Login-related links: ['(no text) -> https://disprot.org/login']


**7. Do you use any resource monitoring supports such as OpenEBench's observatory?**
- Answer: **Yes**
- If yes: provide link: <https://openebench.bsc.es/observatory/Tool/disprot>
- *Status:* Inferred – review · *confidence:* medium
- *Hint:* Resource is monitored in OpenEBench (auto-imported from bio.tools); confirm the team uses it.
- *Evidence:*
    - openebench: <https://openebench.bsc.es/monitor/metrics/disprot> — “last check 2026-08-31T02:00:47.537805285Z”


**8. Please provide a screenshot from the FAIRchecker result for your resource:**
- Screenshot: `/tmp/claude-1000/-home-gavinfarrell-PhD-Code-agent-ECD/b5713f14-d1c1-42a8-b6bb-e186705d1c8c/scratchpad/runs/disprot/fairchecker.png`
  | FAIR-Checker metric | Score (0–2) |
  |---|---|
  | F1A Unique IDs | 2 |
  | F1B Persistent IDs | 2 |
  | F2A Structured metadata | 1 |
  | F2B Shared vocabularies for metadata | 2 |
  | A11 Open resolution protocol | 2 |
  | A12 Authorisation procedure or access rights | 2 |
  | I1 Machine readable format | 1 |
  | I2 Use shared ontologies | 2 |
  | I3 External links | 2 |
  | R11 Metadata includes license | 2 |
  | R12 Metadata includes provenance | 2 |
  | R13 Community standards | 2 |
  Assessment: <https://fair-checker.france-bioinformatique.fr/assessment/6aac141d0f765af231e7373f>
- *Status:* Verified · *confidence:* high
- *Hint:* Claude must view the PNG to confirm it shows completed results before marking verified.
- *Evidence:*
    - fair-checker: <https://fair-checker.france-bioinformatique.fr/assessment/6aac141d0f765af231e7373f> — “scores: F1A=2, F1B=2, F2A=1, F2B=2, A11=2, A12=2, I1=1, I2=2, I3=2, R11=2, R12=2, R13=2”
    - claude-review: <https://fair-checker.france-bioinformatique.fr/assessment/6aac141d0f765af231e7373f> — “Screenshot viewed: completed results for https://disprot.org/, FAIR assessment 91.67 %”


**9. Are you aware of and developing your resource in alignment with RDMkit guidance?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed


**10. Are you aware of and developing your resource in alignment with RSQkit guidance?**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed

## Section 8: Final Declaration


** By submitting this application form, I [To choose] that: 1. Our resource is subject to a one year health check period following a successful ECD application. 2. We agree to actively engage with the ELIXIR Community accrediting our ECD to identify and address achievable checklist gaps where development resources allow.**
- Answer: **[Applicant to complete]**
- *Status:* Applicant input needed

