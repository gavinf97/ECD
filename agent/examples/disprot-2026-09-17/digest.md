# ECD evidence digest — DisProt

Generated 2026-09-17T16:23:11+00:00 · homepage https://disprot.org/ · website render mode: rendered
Registry matches: bioregistry=found:disprot, identifiers_org=found:disprot, re3data=found:r3d100010561, biotools=found:disprot, fairsharing=found:FAIRsharing.dt9z89, uniprot_xref=found:DB-0017, openebench=found:disprot
Needs confirmation: []
Claude to draft (no proposal or lead): S2.4, S5.5, S6.1, S6.5


## APP.submitter_name — Submitter(s) name
- PROPOSAL [needs_applicant/None]: {}

## APP.submitter_email — Submitter(s) email
- PROPOSAL [needs_applicant/None]: {}
  - hint: Institutional email only.

## APP.node — ELIXIR Node(s)
- PROPOSAL [inferred/medium]: {'text': 'ELIXIR-Italy'}
  - elixir-sdp: https://elixir-europe.org/about-us/who-we-are/nodes/italy — DisProt listed under ELIXIR-Italy
  - elixir-sdp: https://elixir-europe.org/about-us/who-we-are/nodes/italy — IDP ontology listed under ELIXIR-Italy
  - hint: Node of the SDP listing; confirm it is the submitting applicant's Node.

## APP.institute — ELIXIR Institute(s)
- PROPOSAL [needs_applicant/None]: {}
  - hint: re3data institutions: Indiana University School of Medicine, Center for Computational Biology and Bioinformatics; NGP-net; Temple University, College of Science and Technology, Center für Data Analysis and Biomedical Informatics; Universita degli Studi di Padova | recent paper affiliations: Cytocast

## APP.repo_url — Resource software repo (e.g. GitHub)
- PROPOSAL [needs_applicant/None]: {}
  - hint: No repository linked from registries/website. GitHub candidates to confirm: https://github.com/BioComputingUP/idpo, https://github.com/usatpath01/DisProTrack, https://github.com/BioComputingUP/caid-reference, https://github.com/TIGER-AI-Lab/DisProtEdit, https://github.com/disprot/disprot.github.io

## APP.community — ELIXIR Community submitted to
- PROPOSAL [needs_applicant/None]: {}
  - hint: Suggested (keyword/link heuristic): Intrinsically Disordered Proteins, 3D-BioInfo

## S1.1 — The primary applicant is a member of an ELIXIR Node & Node institute (check here).
- PROPOSAL [needs_applicant/None]: {}
  - hint: Resource is on the ELIXIR-Italy SDP; confirm the primary applicant belongs to that Node and a Node institute.

## S1.2 — The applicant is submitting an ELIXIR Node Service as listed on the ELIXIR SDP (check here).
- PROPOSAL [verified/high]: {'choice': 'Met', 'text': "Listed as 'DisProt' under ELIXIR-Italy on the ELIXIR SDP."}
  - elixir-sdp: https://elixir-europe.org/about-us/who-we-are/nodes/italy — DisProt (http://www.disprot.org/)

## S1.3 — The service being submitted contains biological data and is one of the following: a. A deposition database (pu
- LEAD: Type signals: re3data repository type: disciplinary | re3data repository type: institutional | re3data data upload: restricted | bio.tools toolType: Web API, Web application, Database portal | description keywords suggest curated knowledgebase: ['curat', 'literature']
- CLAUDE: decide/draft from leads + evidence files

## S1.4 — The service does not already hold a status of: a. Core Data Resource (CDR) b. ELIXIR Deposition Database (EDD)
- PROPOSAL [verified/high]: {'choice': 'Not met', 'text': 'Resource already holds: ELIXIR Deposition Database (EDD).'}
  - elixir-status-list: https://elixir-europe.org/platforms/data/elixir-deposition-databases — ELIXIR Deposition Database (EDD): MATCH ['DisProt']

## S1.5 — For federated and consortia databases (multi-site, multi-branding, non-ELIXIR Involvement), please contact the
- LEAD: re3data institutions: 5 in ['ITA', 'USA']
- CLAUDE: decide/draft from leads + evidence files

## S1.confirm — I confirm that my biodata resource is eligible under the above criteria:
- PROPOSAL [needs_applicant/None]: {}
  - hint: Pre-check blocks eligibility: ELIXIR Deposition Database (EDD)

## S2.1a — Gap your resource serves:
- LEAD: Descriptions — re3data: The Database of Protein Disorder (DisProt) is a curated database that provides information about proteins that lack fixed 3D structure in their putatively native states, either in their entirety or in part.  DisProt is a community resource annotating protein sequences for intrinsically disorder regi | bioregistry: 
- CLAUDE: decide/draft from leads + evidence files

## S2.1b — Biological data type(s) held & total entries:
- LEAD: Statistics snippets: …e service that helps biocurators efficiently identify and prioritize relevant scientific publications for DisProt curation. Info Version: 9.10 Release: 2026_06 Number of entries: 3337 The DisProt database is part of the ELIXIR infrastructure , service of the IDP Community and ELIXIR deposition database . Integrated resources How to cit… || DisProt Browse Training Ontology Release notes Download Deposition About Help Release notes Statistics GO Annotations Number of annotations for each GO ontology namespace. Main Aspect Proteins Regions Cellular component 43 72 Biological
- CLAUDE: decide/draft from leads + evidence files

## S2.1c — Uniqueness:
- LEAD: Candidate overlapping resources (judge genuinely overlapping ones only): MobiDB [Protein disordered structure], Protein Ensemble Database [Protein disordered structure], ComSin [Protein disordered structure], IDEAL [Protein disordered structure], Cell Image Library [re3data keyword: cell biology], National Infrastructure of Cell line Resources BMCR [re3data keyword: cell biology], National Collection of Authenticated Cell Cultures [re3data keyword: cell biology], The Cell Vision [re3data keyword: cell biology], Cancer Cell Line Encyclopedia [re3data keyword: cell biology], hPSCreg [re3data key
- CLAUDE: decide/draft from leads + evidence files

## S2.1d — Relevance to designated ELIXIR Community:
- LEAD: Community suggestions: ['Intrinsically Disordered Proteins', '3D-BioInfo']; bio.tools topics: ['Protein disordered structure']
- CLAUDE: decide/draft from leads + evidence files

## S2.1e — Peer-reviewed article on your database itself (e.g. NAR Database/+)
- PROPOSAL [verified/high]: {'choice': 'Yes', 'links': ['https://doi.org/10.1093/nar/gkaf1175', 'https://doi.org/10.1093/nar/gkad928', 'https://doi.org/10.1093/database/baae009']}
  - europepmc: https://doi.org/10.1093/nar/gkl893 — DisProt: the Database of Disordered Proteins. — Nucleic acids research 2007
  - europepmc: https://doi.org/10.1093/nar/gkw1056 — DisProt 7.0: a major update of the database of disordered proteins. — Nucleic acids research 2017
  - europepmc: https://doi.org/10.1093/nar/gkz975 — DisProt: intrinsic protein disorder annotation in 2020. — Nucleic acids research 2020

## S2.2 — How long ago did your resource officially go live?
- PROPOSAL [inferred/medium]: {'choice': 'More than 10 years'}
  - europepmc: None — earliest paper about resource: 2005
  - wayback: http://web.archive.org/web/20050304063048/http://www.disprot.org:80/ — first archived capture 20050304063048
  - hint: Earliest public trace 2005; confirm the official go-live year.

## S2.3a — A funded ELIXIR Community Commission Service work plan?
- PROPOSAL [needs_applicant/None]: {}
  - hint: ELIXIR commissioned-service participation is not systematically public; ask the applicant.

## S2.3b — A funded ELIXIR CMR/BFSP/HDTR Science Tier Commission Service work plan?
- PROPOSAL [needs_applicant/None]: {}
  - hint: ELIXIR commissioned-service participation is not systematically public; ask the applicant.

## S2.3c — An ELIXIR BioHackathon project /AHM workshop/ other?
- PROPOSAL [needs_applicant/None]: {}
  - hint: Leads: Added DataSet/DataCatalog and DataRecord examples (https://github.com/elixir-europe/BioHackathon-projects-2019/pull/45); Exploiting Bioschemas Markup to Populate IDPcentral (https://doi.org/10.37044/osf.io/v3jct)
- LEAD: Leads: Added DataSet/DataCatalog and DataRecord examples (https://github.com/elixir-europe/BioHackathon-projects-2019/pull/45); Exploiting Bioschemas Markup to Populate IDPcentral (https://doi.org/10.37044/osf.io/v3jct)

## S2.4 — Is your resource a niche biodata resource of use by a narrower life science subdomain e.g. aligned under one o
- CLAUDE: decide/draft from leads + evidence files

## S2.5 — Do you believe there is scope for your resource to eventually mature into a CDR/EDD scale resource (e.g. ENA/U
- PROPOSAL [needs_applicant/None]: {}

## S2.6 — Have you already applied for CDR/EDD status?
- PROPOSAL [needs_applicant/None]: {}

## S3.1 — Do you have resource monitoring in place? e.g. for uptime & response time metrics.
- PROPOSAL [inferred/low]: {'choice': 'Yes', 'text': 'Uptime and response time are tracked by the OpenEBench monitoring service.'}
  - openebench: https://openebench.bsc.es/observatory/Tool/disprot — OpenEBench monitor: last month uptime 30 d, downtime 0 d, avg access 701 ms
  - hint: External monitoring (OpenEBench) found; confirm whether the team runs its own uptime/response-time monitoring.

## S3.2 — Are you tracking any quantitative resource usage data metrics? e.g. monthly users/+
- PROPOSAL [inferred/medium]: {'choice': 'Yes', 'text': 'Web usage analytics are collected (Google Analytics / Tag Manager).'}
  - website:analytics: https://disprot.org/ — analytics tags detected: ['Google Analytics / Tag Manager']
  - hint: Analytics tags detected; confirm which usage metrics are tracked (do not report numbers).

## S3.3 — Have you considered the possible user base growth of your target domain community?
- LEAD: Citations of resource papers: 1630; domain mentions by year: {'2008': 1, '2014': 1, '2015': 1, '2020': 2, '2021': 2, '2022': 11, '2023': 6, '2024': 8, '2025': 2, '2026': 5}
- CLAUDE: decide/draft from leads + evidence files

## S4.1 — Do you have a resource update strategy or development roadmap?
- LEAD: Roadmap/news snippets: DisProt Browse Training Ontology Release notes Download Deposition About Help Release notes Statistics GO Annotations Number of annotations for each GO ontology || DisProt Browse Training Ontology Release notes Download Deposition About Help Welcome to DisProt , the database of intrinsically disordered proteins DisProt is  || Release notes -> https://disprot.org/release-notes
- CLAUDE: decide/draft from leads + evidence files

## S4.2 — Does your resource collect user base feedback and community input for its development roadmap?
- LEAD: Feedback snippets:  | robots.txt excerpt: User-agent: *
Allow: /

User-agent: *
Disallow: /feedback/

Sitemap: https://disprot.org/sitemap.xml

- CLAUDE: decide/draft from leads + evidence files

## S4.3 — Does your resource have a helpdesk?
- PROPOSAL [verified/high]: {'choice': 'Yes', 'links': ['https://disprot.org/help']}
  - website:helpdesk: https://disprot.org/help — …ormatics Exploring Manually Curated Annotations of Intrinsically Disordered Proteins with DisProt Open access protocol, featuring three basic protocols and two support protocols: 

## S4.4 — Does your resource have details publicly available about who works on your resource?
- LEAD: Team-like pages crawled: ['https://disprot.org/about']; snippets: …del Bouharoua - Web developer (Junior Post-doc) Amirali Motaghedy - Web developer intern (M.Sc. student) Ivan Micetic - System administrator & support Previous || Christine Orengo -> https://www.ucl.ac.uk/orengo-group/people/prof-christine-orengo || …y disordered proteins DisProt is the major manually curated repository of Intrinsically Disordered Proteins, both for structural and functional aspects. Expert
- CLAUDE: decide/draft from leads + evidence files

## S4.5 — How many people (approximate in FTE) work on your resource?
- PROPOSAL [needs_applicant/None]: {}

## S4.6 — Is the resource operated across more than one institution?
- LEAD: re3data institutions: ['Indiana University School of Medicine, Center for Computational Biology and Bioinformatics', 'NGP-net', 'Temple University, College of Science and Technology, Center für Data Analysis and Biomedical Informatics', 'Universita degli Studi di Padova', 'University of Padua, Department of Biomedical Sciences, BioComputing UP Lab']
- CLAUDE: decide/draft from leads + evidence files

## S4.7a — Retain staff to curate data, maintain & update it?
- PROPOSAL [needs_applicant/None]: {}
  - hint: Funders acknowledged in resource papers (not proof of current dedicated funding): [['Horizon 2020', 6], ['Hungarian Academy of Sciences', 4], ['Hungarian Scientific Research Fund', 4], ['European Union', 4], ['NLM NIH HHS', 3], ['National Research, Development and Innovation Fund of the Ministry of 

## S4.7b — Provide dedicated hardware to keep it live & online (at least for next 2 years)?
- PROPOSAL [needs_applicant/None]: {}

## S4.8 — Do you know how many of your team members would have to leave the project for the resource to stop further dev
- PROPOSAL [needs_applicant/None]: {}

## S4.9 — Does your resource have a scientific advisory board (SAB)?
- PROPOSAL [verified/medium]: {'choice': 'Yes', 'links': ['https://disprot.org/about']}
  - website:sab: https://disprot.org/about — …- Web developer András Hatos - Web developer Edoardo Salladini - Senior curator Contact us For enquiries related to the DisProt, please email: info@disprot.org Scientific Advisory

## S4.10 — Does your resource have a privacy statement?
- PROPOSAL [verified/high]: {'choice': 'Yes', 'links': ['https://disprot.org/about']}
  - website:privacy: https://disprot.org/about — … at Khoury College of Computer Sciences, Northwestern University License This work is licensed under a Creative Commons Attribution 4.0 International License . Privacy notice This

## S4.11 — Does your resource have an ethics policy? (e.g. for sensitive data)
- PROPOSAL [needs_applicant/None]: {}
  - hint: No 'ethics' evidence found in the crawled pages (crawl is partial).

## S5.1 — Does your resource use metadata standards for its data?
- PROPOSAL [inferred/medium]: {'choice': 'Yes'}
  - re3data:metadataStandard: http://www.dcc.ac.uk/resources/metadata-standards/repository-developed-metadata-schemas — Repository-Developed Metadata Schemas
  - website:json-ld: https://disprot.org/DP00003 — schema.org/Bioschemas JSON-LD types: ['DataCatalog', 'Dataset', 'Protein']
  - hint: Name the actual standards (e.g. Bioschemas profile, MIAPE) and add FAIRsharing standard links.

## S5.2 — Does your resource use an ontology for its data?
- PROPOSAL [verified/high]: {'choice': 'Yes', 'links': ['https://www.ebi.ac.uk/ols4/ontologies/eco', 'https://www.ebi.ac.uk/ols4/ontologies/go'], 'text': 'Uses Evidence & Conclusion Ontology (ECO) (ECO), Gene Ontology (GO) for annotations.'}
  - website:curie: https://disprot.org/DP00003 — ECO terms found 14x; in OLS: Evidence & Conclusion Ontology (ECO)
  - website:curie: https://disprot.org/DP00003 — GO terms found 3x; in OLS: Gene Ontology
- LEAD: Ontology prefixes used but not in OLS4 (check OBO Foundry/BioPortal): ['IDPO']

## S5.3 — Does your resource expose structured data (e.g. JSON/W3C/DCAT)?
- PROPOSAL [verified/high]: {'choice': 'Yes', 'links': ['https://disprot.org/DP00003'], 'text': 'Pages embed schema.org/Bioschemas JSON-LD (DataCatalog, Dataset, Protein).'}
  - website:json-ld: https://disprot.org/DP00003 — schema.org/Bioschemas JSON-LD types: ['DataCatalog', 'Dataset', 'Protein']

## S5.4 — Does your resource provide an API/FTP/other protocols for exposing and retrieving the data in a machine action
- PROPOSAL [verified/high]: {'choice': 'Yes', 'list': ['REST API: https://disprot.org/api/', 'REST: https://www.disprot.org/help#anchor3']}
  - website:api-endpoint: https://disprot.org/api/ — application/json: "Hello from legacy"
  - re3data:api: https://www.disprot.org/help#anchor3 — re3data API type REST
  - website:api: https://disprot.org/help — …es used in DisProt to describe structural, functional and technique or evidence of IDPs/IDRs. Information about RESTful endpoints and the output format see the API documentation b
  - hint: Add download/FTP and documentation links if available.

## S5.5 — Does your resource pull data from other data resources? (inflow of data)
- CLAUDE: decide/draft from leads + evidence files

## S5.6 — Do other resources pull data from your resource? (outflow of data)
- PROPOSAL [verified/high]: {'choice': 'Yes', 'list': ['UniProtKB cross-references (DB-0017)']}
  - uniprot: https://www.uniprot.org/database/DB-0017 — Database of protein disorder is a UniProt cross-referenced database (Family and domain databases)
  - hint: Add other known consumers (e.g. InterPro, MobiDB) if the applicant knows them.

## S5.7 — Have you identified/roadmapped existing (ELIXIR) biodata resources that could augment their database entries b
- PROPOSAL [needs_applicant/None]: {}

## S6.1 — Do you have a publicly available data management plan?
- CLAUDE: decide/draft from leads + evidence files

## S6.2 — What is the license for use of the data in your resource?
- PROPOSAL [pending/None]: {}
  - website:license: https://disprot.org/ — …Tompa, Damiano Piovesan, Silvio C E Tosatto, Maria Cristina Aspromonte (2025) Nucleic Acids Research, Database Issue. PubMed:41249866 , DOI:10.1093/nar/gkad928 License This work i
  - website:license-link: http://creativecommons.org/licenses/by/4.0/ — (no text) -> http://creativecommons.org/licenses/by/4.0/
  - website:license: https://disprot.org/training — …hannel Zenodo Community Other Recorded tutorials Materials For Curators And Users Datasets Crediting Contact BioComputing UP, 2021 - University of Padua, Italy License and disclai
  - hint: Claude: state the exact data licence named on the website (prefer the site over registries).
- LEAD: Licence evidence: website:license: …Tompa, Damiano Piovesan, Silvio C E Tosatto, Maria Cristina Aspromonte (2025) Nucleic Acids Research, Database Issue. PubMed:41249866 , DOI:10.1093/nar/gkad928 || website:license-link: (no text) -> http://creativecommons.org/licenses/by/4.0/ || website:license: …hannel Zenodo Community Other Recorded tutorials Materials For Curators And Users Datasets Crediting Contact BioComputing UP, 2021 - University of Padua, Italy
- CLAUDE: decide/draft from leads + evidence files

## S6.3 — Do you have a clear plan for long-term storage and off-site backups?
- PROPOSAL [needs_applicant/None]: {}

## S6.4 — Do you maintain version archives of the database contents?
- PROPOSAL [inferred/medium]: {'choice': 'Yes'}
  - website:versions: https://disprot.org/release-notes — … The amino acid frequency is calculated considering only disordered residues. The enrichment is calculated and normalized over the TrEMBL database frequencies (release 2021_03). A
  - website:versions-link: https://biocomputingup.github.io/2021/12/15/release-2021_12/ — narrative blogpost -> https://biocomputingup.github.io/2021/12/15/release-2021_12/
  - website:roadmap: https://disprot.org/release-notes — DisProt Browse Training Ontology Release notes Download Deposition About Help Release notes Statistics GO Annotations Number of annotations for each GO ontology namespace. Main Asp
  - hint: Describe release cadence and where previous releases are archived.

## S6.5 — Do you have a publicly available software management plan?
- CLAUDE: decide/draft from leads + evidence files

## S6.6 — What is the license for use of the software of your resource?
- PROPOSAL [needs_applicant/None]: {}
  - hint: No confirmed code repository.

## S6.7 — Is your data resource's software available in containerised format for reuse? (eg: Docker image/Podman/Singula
- PROPOSAL [needs_applicant/None]: {}
  - hint: No confirmed code repository.

## S6.8 — Is your data resource's software open source? (i.e. the code base is reusable and available to redeploy?)
- PROPOSAL [needs_applicant/None]: {}
  - hint: No confirmed code repository.

## S7.1 — Is your resource listed in a database registry such as FAIRsharing?
- PROPOSAL [verified/high]: {'choice': 'Yes', 'links': ['https://fairsharing.org/FAIRsharing.dt9z89', 'https://www.re3data.org/repository/r3d100010561']}
  - fairsharing: https://fairsharing.org/FAIRsharing.dt9z89 — FAIRsharing record FAIRsharing.dt9z89 (via ['bioregistry_mapping'])

## S7.2 — Does your resource have its identifiers registered in identifiers.org?
- PROPOSAL [verified/high]: {'choice': 'Yes', 'links': ['https://registry.identifiers.org/registry/disprot']}
  - identifiers.org: https://registry.identifiers.org/registry/disprot — prefix disprot (MIR:00000199)

## S7.3 — Are any analysis tools & workflows provided by your resource registered in relevant registries such as bio.too
- PROPOSAL [verified/medium]: {'choice': 'Yes', 'links': ['https://bio.tools/disprot']}
  - bio.tools: https://bio.tools/disprot — bio.tools entry disprot (['Web API', 'Web application', 'Database portal'])
  - hint: bio.tools entry found; add any separate tools/workflows the resource provides.

## S7.4 — Are any training materials for your resource registered in TeSS?
- PROPOSAL [verified/high]: {'choice': 'Yes', 'links': ['https://tess.elixir-europe.org/materials/an-introduction-to-disprot-03344576-ed76-48c7-ac18-ec18365060c9', 'https://tess.elixir-europe.org/materials/exploring-structural-and-functional-annotations-of-idps-with-disprot-a2647e13-bfac-4320-b319-695e51f68573', 'https://tess.elixir-europe.org/materials/experimental-techniques-for-the-characterization-of-intrinsically-disordered-proteins']}
  - tess: https://tess.elixir-europe.org/materials/an-introduction-to-disprot-03344576-ed76-48c7-ac18-ec18365060c9 — An introduction to DisProt
  - tess: https://tess.elixir-europe.org/materials/exploring-structural-and-functional-annotations-of-idps-with-disprot-a2647e13-bfac-4320-b319-695e51f68573 — Exploring structural and functional annotations of IDPs with DisProt
  - tess: https://tess.elixir-europe.org/materials/experimental-techniques-for-the-characterization-of-intrinsically-disordered-proteins — Experimental techniques for the characterization of Intrinsically Disordered Proteins

## S7.5 — If reliant on data curation does your resource use APICURON for curator credit and recognition?
- PROPOSAL [inferred/medium]: {'choice': 'Yes', 'links': ['https://apicuron.org/']}
  - website:apicuron-link: https://apicuron.org/ — resource website links to APICURON
  - hint: Website links to APICURON; confirm curator credit is actually submitted and add the APICURON resource page link.

## S7.6 — If reliant on a user authentication and authorisation infrastructure (AAI) service, do you use LS-AAI?
- PROPOSAL [needs_applicant/None]: {}
  - hint: No LS Login detected. Login-related links: ['(no text) -> https://disprot.org/login']

## S7.7 — Do you use any resource monitoring supports such as OpenEBench's observatory?
- PROPOSAL [inferred/medium]: {'choice': 'Yes', 'links': ['https://openebench.bsc.es/observatory/Tool/disprot']}
  - openebench: https://openebench.bsc.es/monitor/metrics/disprot — last check 2026-08-31T02:00:47.537805285Z
  - hint: Resource is monitored in OpenEBench (auto-imported from bio.tools); confirm the team uses it.

## S7.8 — Please provide a screenshot from the FAIRchecker result for your resource:
- PROPOSAL [inferred/high]: {'image': '/tmp/claude-1000/-home-gavinfarrell-PhD-Code-agent-ECD/b5713f14-d1c1-42a8-b6bb-e186705d1c8c/scratchpad/runs/disprot/fairchecker.png', 'links': ['https://fair-checker.france-bioinformatique.fr/assessment/6aac141d0f765af231e7373f']}
  - fair-checker: https://fair-checker.france-bioinformatique.fr/assessment/6aac141d0f765af231e7373f — scores: F1A=2, F1B=2, F2A=1, F2B=2, A11=2, A12=2, I1=1, I2=2, I3=2, R11=2, R12=2, R13=2
  - hint: Claude must view the PNG to confirm it shows completed results before marking verified.

## S7.9 — Are you aware of and developing your resource in alignment with RDMkit guidance?
- PROPOSAL [needs_applicant/None]: {}

## S7.10 — Are you aware of and developing your resource in alignment with RSQkit guidance?
- PROPOSAL [needs_applicant/None]: {}

## S8.declaration — By submitting this application form, I [To choose] that: 1. Our resource is subject to a one year health check
- PROPOSAL [needs_applicant/None]: {}
