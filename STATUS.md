# ECD uptime status

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/monitoring.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml) [![up](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/up.json)](#all-resources) [![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/down.json)](#needs-attention) [![last check](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/last-check.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml)

## 🟢 Monitoring is ACTIVE

| | |
|---|---|
| **Resources monitored** | 163 — every one, every 20 minutes, continuously |
| **Last check** | 2026-10-17T23:50:29Z (2 min ago) |
| **Runs in the last 24 h** | 98 of a target 72 |
| **Checks recorded** | 2065 runs since monitoring began |
| **Runs on** | [GitHub Actions → uptime-check](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml) |
| **Visual dashboard** | https://gavinf97.github.io/ECD/ |

### Right now

🟢 up **130** · 🟡 challenged **11** · 🔴 down **22** · ⚪ never checked **0** · 🔗 check URL to review **6**

Uptime = (up + challenged) ÷ recorded checks. Coverage = recorded ÷ expected checks. 99.00% is the ECD reference target (ECD Process V1 §5); it sorts the list below and carries no deadline — monitoring simply continues. Full definitions: [uptime/README.md](https://github.com/gavinf97/ECD/blob/main/uptime/README.md).

---

## Needs attention

### 🔴 Currently down

**22** of 163 resources are not responding.

| Resource | Node | Since (UTC) | Reason | 30d uptime |
|---|---|---|---|---|
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 2026-09-17T16:07:30Z | `tls_error` | 0.00% |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 2026-09-17T16:07:30Z | `connection_refused` | 0.00% |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `connect_timeout` | 0.00% |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `connect_timeout` | 0.00% |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_502` | 0.00% |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 2026-09-17T16:07:30Z | `tls_error` | 0.00% |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 2026-09-17T16:07:30Z | `connect_timeout` | 0.00% |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 2026-09-17T16:07:30Z | `connect_timeout` | 0.00% |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 2026-09-17T16:07:30Z | `dns_error` | 0.00% |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 2026-09-17T16:07:30Z | `dns_error` | 0.00% |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 2026-09-17T16:07:30Z | `read_timeout` | 0.00% |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 2026-09-22T14:58:18Z | `tls_error` | 1.26% |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 2026-10-05T17:50:32Z | `http_502` | 46.21% |
| [2Dprots](https://2dprots.ncbr.muni.cz/) | ELIXIR Czech Republic | 2026-10-15T12:10:32Z | `connection_refused` | 83.40% |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 2026-10-17T23:30:43Z | `connect_timeout` | 40.87% |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 2026-10-17T23:30:43Z | `connect_timeout` | 40.00% |

🔗 = the check URL returns 404/410; see below.

### 🔗 Check URL needs review

**6** return 404/410, so the resource has moved or been retired. They are counted as down until the URL is corrected: set `check.url` for the resource in [uptime/resources.yml](https://github.com/gavinf97/ECD/blob/main/uptime/resources.yml), or `enabled: false` if it is genuinely gone.

| Resource | Node | Check URL | Code |
|---|---|---|---|
| AspicDB | ELIXIR Italy | https://rediportal.cloud.ba.infn.it/ASPicDB/ | `http_404` |
| DEEP data portal | ELIXIR Germany | https://deep.dkfz.de/#/home | `http_404` |
| MitoZoa | ELIXIR Italy | https://rediportal.cloud.ba.infn.it/mitozoa/ | `http_404` |
| PMDB | ELIXIR Italy | https://rediportal.cloud.ba.infn.it/PMDB/help.php | `http_404` |
| REDIdb | ELIXIR Italy | https://rediportal.cloud.ba.infn.it/redidb/ | `http_404` |
| SpliceAid-F | ELIXIR Italy | https://rediportal.cloud.ba.infn.it/SpliceAidF/ | `http_404` |

### 📉 Below 99.00% over the last 30 days

**56** resources, worst first.

| Resource | Node | 30d uptime | 30d coverage | Down checks |
|---|---|---|---|---|
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 0.00% | 100.00% | 2060 |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 0.00% | 100.00% | 2060 |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 0.00% | 100.00% | 2060 |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 0.00% | 100.00% | 2060 |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 0.00% | 100.00% | 2060 |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 0.00% | 100.00% | 2060 |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 0.00% | 100.00% | 2060 |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 0.00% | 100.00% | 2060 |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 0.00% | 100.00% | 2060 |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 0.00% | 100.00% | 2060 |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 0.00% | 100.00% | 2060 |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 0.00% | 100.00% | 2060 |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 0.00% | 100.00% | 2060 |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 0.00% | 100.00% | 2060 |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 0.00% | 100.00% | 2060 |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 0.00% | 100.00% | 2060 |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 0.00% | 100.00% | 2060 |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 1.26% | 100.00% | 2034 |
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 32.67% | 100.00% | 1387 |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 40.00% | 100.00% | 1236 |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 40.87% | 100.00% | 1218 |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 46.21% | 100.00% | 1108 |
| [iPtgxDBs](https://iptgxdb.expasy.org/) | ELIXIR Switzerland | 64.32% | 100.00% | 735 |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 71.36% | 100.00% | 590 |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 75.63% | 100.00% | 502 |
| [MetaPhOrs](https://orthology.phylomedb.org/) | ELIXIR Spain | 78.16% | 100.00% | 450 |
| [PhylomeDB](https://phylomedb.org/) | ELIXIR Spain | 78.16% | 100.00% | 450 |
| [PICKLE](http://www.pickle.gr) | ELIXIR Greece | 79.47% | 100.00% | 423 |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 81.07% | 100.00% | 390 |
| [2Dprots](https://2dprots.ncbr.muni.cz/) | ELIXIR Czech Republic | 83.40% | 100.00% | 342 |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 85.10% | 100.00% | 307 |
| [Unilectin](https://unilectin.unige.ch/) | ELIXIR Switzerland | 87.14% | 100.00% | 265 |
| [MobiDB](http://mobidb.bio.unipd.it/) | ELIXIR Italy | 88.01% | 100.00% | 247 |
| [Expression Atlas](https://www.ebi.ac.uk/gxa/home) | EMBL-EBI | 91.50% | 100.00% | 175 |
| [CATH/Gene3D](https://www.cathdb.info/) | ELIXIR UK | 95.10% | 100.00% | 101 |
| [WatAA](https://watlas.datmos.org/wataa/) | ELIXIR Czech Republic | 95.53% | 100.00% | 92 |
| [MetaNetX](https://www.metanetx.org/) | ELIXIR Switzerland | 96.36% | 100.00% | 75 |
| [DisProt](https://www.disprot.org/) | ELIXIR Italy | 96.70% | 100.00% | 68 |
| [Nextstrain](https://nextstrain.org/) | ELIXIR Switzerland | 96.99% | 100.00% | 62 |
| [PED](https://proteinensemble.org/) | ELIXIR Italy | 97.14% | 100.00% | 59 |
| [RepeatsDB](https://repeatsdb.org/) | ELIXIR Italy | 97.14% | 100.00% | 59 |
| [DOME-ML](https://dome-ml.org) | ELIXIR Italy | 97.18% | 100.00% | 58 |
| [DOME Registry](https://registry.dome-ml.org) | ELIXIR Italy | 97.23% | 100.00% | 57 |
| [PanDrugs](https://www.pandrugs.org) | ELIXIR Spain | 97.62% | 100.00% | 49 |
| [Dolbico](https://dolbico.org/) | ELIXIR Czech Republic | 97.67% | 100.00% | 48 |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 97.77% | 100.00% | 46 |
| [Omics Discovery Index (OmicsDI)](https://www.omicsdi.org/) | EMBL-EBI | 98.35% | 100.00% | 34 |
| [OMA](https://omabrowser.org/oma/home/) | ELIXIR Switzerland | 98.54% | 100.00% | 30 |
| [RNA Central](https://rnacentral.org/) | EMBL-EBI | 98.64% | 100.00% | 28 |
| [PAXdb](https://pax-db.org/) | ELIXIR Switzerland | 98.69% | 100.00% | 27 |
| [GlobalFungi](https://globalfungi.com/) | ELIXIR Czech Republic | 98.74% | 100.00% | 26 |
| [BRENDA](https://www.brenda-enzymes.org/index.php) | ELIXIR Germany | 98.93% | 100.00% | 22 |
| [FINDbase](https://findbase.org/#/) | ELIXIR Greece | 98.93% | 100.00% | 22 |
| [AlphaFold DB](https://alphafold.ebi.ac.uk/) | EMBL-EBI | 98.98% | 100.00% | 21 |
| [BacDive](https://bacdive.dsmz.de/) | ELIXIR Germany | 98.98% | 100.00% | 21 |
| [YEASTRACT](https://yeastract-plus.org/) | ELIXIR Portugal | 98.98% | 100.00% | 21 |

---

## All resources

All 163 resources, sorted by name. Sortable and searchable on the [dashboard](https://gavinf97.github.io/ECD/).

| Resource | Node | State | Today | 7d | 30d | 90d | 365d | Coverage 30d | p95 30d |
|---|---|---|---|---|---|---|---|---|---|
| [2Dprots](https://2dprots.ncbr.muni.cz/) | ELIXIR Czech Republic | 🔴 down | 0.00% | 52.72% | 83.40% | 83.44% | 83.44% | 100.00% | ≤2000 ms |
| [3D interacting domains (3Did)](https://3did.irbbarcelona.org/) | ELIXIR Spain | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [AgroLD (Agronomic Linked Data)](https://agrold.southgreen.fr/agrold) | ELIXIR France | 🟢 up | 97.96% | 99.22% | 99.17% | 99.18% | 99.18% | 100.00% | ≤1000 ms |
| [AlphaFold DB](https://alphafold.ebi.ac.uk/) | EMBL-EBI | 🟢 up | 100.00% | 99.07% | 98.98% | 98.98% | 98.98% | 100.00% | ≤5000 ms |
| [AmtDB](https://amtdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 99.69% | 99.90% | 99.90% | 99.90% | 100.00% | ≤2000 ms |
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [Annotating PRincpial splice ISoforms (APPRIS)](https://appris.bioinfo.cnio.es/) | ELIXIR Spain | 🟢 up | 98.98% | 99.84% | 99.90% | 99.90% | 99.90% | 100.00% | ≤1000 ms |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [BacDive](https://bacdive.dsmz.de/) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 98.98% | 98.93% | 98.93% | 100.00% | ≤2000 ms |
| [BEGDB](http://www.begdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 99.84% | 99.95% | 99.95% | 99.95% | 100.00% | ≤5000 ms |
| [Bgee](https://www.bgee.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [BioImage Informatics Index (BISE)](https://biii.eu/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [biomaRt](https://bioconductor.org/packages/release/bioc/html/biomaRt.html) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.66% | 99.66% | 99.66% | 100.00% | ≤1000 ms |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 97.77% | 97.77% | 97.77% | 100.00% | ≤1000 ms |
| [BioSurfDB](https://www.biosurfdb.org) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [BRENDA](https://www.brenda-enzymes.org/index.php) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 98.93% | 98.89% | 98.89% | 100.00% | ≤2000 ms |
| [CATH/Gene3D](https://www.cathdb.info/) | ELIXIR UK | 🟢 up | 100.00% | 99.84% | 95.10% | 95.11% | 95.11% | 100.00% | ≤1000 ms |
| [Cellosaurus](https://www.cellosaurus.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 99.95% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [ChannelsDB](https://channelsdb2.biodata.ceitec.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 99.84% | 99.95% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [ChEBI](https://www.ebi.ac.uk/chebi) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ChEMBL](https://www.ebi.ac.uk/chembl/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [Collections and registries from the Finnish population: SISU data resource](https://www.sisuproject.fi/) | ELIXIR Finland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [CorkOakDB](https://corkoakdb.org/) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 99.22% | 99.18% | 99.18% | 100.00% | ≤2000 ms |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [DGP](https://pmc.ncbi.nlm.nih.gov/articles/PMC434425/) | ELIXIR Greece | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [DisProt](https://www.disprot.org/) | ELIXIR Italy | 🟢 up | 100.00% | 98.91% | 96.70% | 96.71% | 96.71% | 100.00% | ≤2000 ms |
| [DMPortal](https://dmportal.biodata.pt) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 99.22% | 99.18% | 99.18% | 100.00% | ≤5000 ms |
| [Dolbico](https://dolbico.org/) | ELIXIR Czech Republic | 🟢 up | 98.98% | 92.85% | 97.67% | 97.68% | 97.68% | 100.00% | ≤5000 ms |
| [DOME Registry](https://registry.dome-ml.org) | ELIXIR Italy | 🟢 up | 100.00% | 98.91% | 97.23% | 97.24% | 97.24% | 100.00% | ≤2000 ms |
| [DOME-ML](https://dome-ml.org) | ELIXIR Italy | 🟢 up | 100.00% | 98.91% | 97.18% | 97.19% | 97.19% | 100.00% | ≤2000 ms |
| [Ensembl](https://www.ensembl.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ENZYME](https://enzyme.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Evolutionary genealogy of genes: Non-supervised Orthologous Groups (eggNOG)](https://eggnogdb.org/) | ELIXIR Germany, ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [EvoPPI](http://evoppi.i3s.up.pt/) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Expression Atlas](https://www.ebi.ac.uk/gxa/home) | EMBL-EBI | 🟢 up | 98.98% | 73.87% | 91.50% | 91.53% | 91.53% | 100.00% | ≤2000 ms |
| [FAIDARE](https://urgi.versailles.inrae.fr/faidare/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [FINDbase](https://findbase.org/#/) | ELIXIR Greece | 🟢 up | 98.98% | 99.53% | 98.93% | 98.93% | 98.93% | 100.00% | ≤1000 ms |
| [FireProtDB](https://loschmidt.chemi.muni.cz/fireprotdb/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.71% | 99.71% | 99.71% | 100.00% | ≤2000 ms |
| [Flybase](https://flybase.org/) | ELIXIR UK | 🟢 up | 100.00% | 99.53% | 99.85% | 99.85% | 99.85% | 100.00% | ≤500 ms |
| [Galactosemia Proteins Database](https://www.elixir-italy.org/services/galactosemia-proteins-database/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 46.21% | 46.34% | 46.34% | 100.00% | ≤2000 ms |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 🟢 up | 88.78% | 90.98% | 85.10% | 85.04% | 85.04% | 100.00% | ≤2000 ms |
| [GenomeRNAi](https://genomernai.dkfz.de) | ELIXIR Germany | 🟢 up | 100.00% | 99.84% | 99.95% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [GENOMICUS](https://www.genomicus.bio.ens.psl.eu/genomicus-110.01/cgi-bin/search.pl) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 99.22% | 99.13% | 99.13% | 100.00% | ≤5000 ms |
| [GlobalFungi](https://globalfungi.com/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 95.96% | 98.74% | 98.74% | 98.74% | 100.00% | ≤2000 ms |
| [GnpIS](https://urgi.versailles.inrae.fr/gnpis/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [GO annotation (GOA)](https://www.ebi.ac.uk/GOA/index) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [GWAS Central](https://help.gwascentral.org/about/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [HAMAP](https://hamap.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [HCVIVdb](http://www.hcvivdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 99.84% | 99.90% | 99.90% | 99.90% | 100.00% | ≤2000 ms |
| [HERVd](https://herv.img.cas.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.47% | 99.47% | 99.47% | 100.00% | ≤2000 ms |
| [HGNC](https://www.genenames.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 🟢 up | 88.78% | 85.23% | 81.07% | 80.92% | 80.92% | 100.00% | >10000 ms |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [HTP](https://htp.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.90% | 99.90% | 99.90% | 100.00% | ≤2000 ms |
| [Human Protein Atlas (HPA)](https://www.proteinatlas.org/) | ELIXIR Sweden | 🟢 up | 100.00% | 98.91% | 99.61% | 99.61% | 99.61% | 100.00% | ≤2000 ms |
| [IDSM](https://idsm.elixir-czech.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 99.38% | 99.71% | 99.71% | 99.71% | 100.00% | ≤2000 ms |
| [IMGT](https://www.imgt.org) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [InterMine](http://intermine.org) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [InterPro](https://www.ebi.ac.uk/interpro/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [iPtgxDBs](https://iptgxdb.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 64.32% | 64.41% | 64.41% | 100.00% | ≤2000 ms |
| [IreSite](http://iresite.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 99.69% | 99.85% | 99.85% | 99.85% | 100.00% | ≤2000 ms |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [IUPHAR/BPS Guide to PHARMACOLOGY](https://www.guidetopharmacology.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [JASPAR](https://jaspar.elixir.no/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [LiceBase](https://licebase.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [MaCPepDB](https://macpepdb.cubimed.rub.de) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.95% | 99.95% | 99.95% | 100.00% | ≤1000 ms |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [MassBank](https://massbank.eu/MassBank//) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 🔴 down | 0.00% | 0.00% | 1.26% | 1.50% | 1.50% | 100.00% | ≤2000 ms |
| [MediaDive](https://mediadive.dsmz.de/) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.08% | 99.03% | 99.03% | 100.00% | ≤2000 ms |
| [MeltDB](https://meltdb.cebitec.uni-bielefeld.de/cgi-bin/login.cgi) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [MEM](https://biit.cs.ut.ee/mem/) | ELIXIR Estonia | 🟢 up | 100.00% | 99.53% | 99.66% | 99.66% | 99.66% | 100.00% | >10000 ms |
| [Metabolic Atlas](https://metabolicatlas.org/) | ELIXIR Sweden | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [MetaNetX](https://www.metanetx.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 99.38% | 96.36% | 96.37% | 96.37% | 100.00% | ≤5000 ms |
| [MetaPhOrs](https://orthology.phylomedb.org/) | ELIXIR Spain | 🟢 up | 98.98% | 99.69% | 78.16% | 78.21% | 78.21% | 100.00% | ≤10000 ms |
| [MGnify](https://www.ebi.ac.uk/metagenomics/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MHC Motif Atlas](http://mhcmotifatlas.org/home) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 🟢 up | 100.00% | 77.45% | 71.36% | 71.43% | 71.43% | 100.00% | >10000 ms |
| [Microbe Atlas](https://microbeatlas.org/landing) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 32.67% | 32.59% | 32.59% | 100.00% | ≤5000 ms |
| [MirGeneDB](https://mirgenedb.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [MobiDB](http://mobidb.bio.unipd.it/) | ELIXIR Italy | 🟢 up | 100.00% | 98.91% | 88.01% | 87.80% | 87.80% | 100.00% | ≤5000 ms |
| [MOLGENIS](https://molgenis.github.io/) | ELIXIR Netherlands | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [MolMeDB](https://molmedb.upol.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Nextstrain](https://nextstrain.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 98.44% | 96.99% | 97.00% | 97.00% | 100.00% | ≤1000 ms |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 🔴 down | 34.69% | 44.01% | 40.87% | 40.77% | 40.77% | 100.00% | ≤5000 ms |
| [OLIDA](https://olida.ibsquare.be/) | ELIXIR Belgium | 🟢 up | 100.00% | 99.84% | 99.90% | 99.90% | 99.90% | 100.00% | ≤1000 ms |
| [OMA](https://omabrowser.org/oma/home/) | ELIXIR Switzerland | 🟢 up | 100.00% | 99.69% | 98.54% | 98.55% | 98.55% | 100.00% | ≤5000 ms |
| [Omics Discovery Index (OmicsDI)](https://www.omicsdi.org/) | EMBL-EBI | 🟢 up | 100.00% | 99.84% | 98.35% | 98.35% | 98.35% | 100.00% | ≤10000 ms |
| [OmniPath](https://omnipathdb.org/) | ELIXIR Germany | 🟢 up | 100.00% | 99.69% | 99.90% | 99.90% | 99.90% | 100.00% | ≤1000 ms |
| [OMPdb](http://www.ompdb.org/) | ELIXIR Greece | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [OpenTargets Platform](https://platform.opentargets.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Orphadata](https://www.orphadata.com/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [Orphanet](https://www.orpha.net/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [OrthoDB](https://www.orthodb.org) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [PanDrugs](https://www.pandrugs.org) | ELIXIR Spain | 🟢 up | 93.88% | 96.89% | 97.62% | 97.63% | 97.63% | 100.00% | ≤1000 ms |
| [ParameciumDB](https://paramecium.i2bc.paris-saclay.fr) | ELIXIR France | 🟢 up | 100.00% | 99.84% | 99.90% | 99.90% | 99.90% | 100.00% | ≤5000 ms |
| [PAXdb](https://pax-db.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 98.69% | 98.69% | 98.69% | 100.00% | ≤2000 ms |
| [PDBTM](https://pdbtm.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.90% | 99.90% | 99.90% | 100.00% | ≤5000 ms |
| [PED](https://proteinensemble.org/) | ELIXIR Italy | 🟢 up | 100.00% | 98.91% | 97.14% | 97.14% | 97.14% | 100.00% | ≤2000 ms |
| [PHI-base](http://www.phi-base.org) | ELIXIR UK | 🟢 up | 98.98% | 99.38% | 99.71% | 99.71% | 99.71% | 100.00% | ≤5000 ms |
| [PhylomeDB](https://phylomedb.org/) | ELIXIR Spain | 🟢 up | 98.98% | 99.69% | 78.16% | 78.21% | 78.21% | 100.00% | ≤5000 ms |
| [PICKLE](http://www.pickle.gr) | ELIXIR Greece | 🟢 up | 73.47% | 84.45% | 79.47% | 79.27% | 79.27% | 100.00% | >10000 ms |
| [PIPPA](https://pippa.psb.ugent.be/pippa_nav/home/) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [PolarProtDb](https://polarprotdb.ttk.hu/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.90% | 99.90% | 99.90% | 100.00% | ≤5000 ms |
| [PomBase](https://www.pombase.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Progenetix](https://progenetix.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [PROSITE](https://prosite.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Reactome](https://reactome.org/) | EMBL-EBI | 🟢 up | 100.00% | 99.84% | 99.81% | 99.81% | 99.81% | 100.00% | ≤1000 ms |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [REDIportal](https://rediportal.cloud.ba.infn.it/atlas/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 🔴 down | 34.69% | 40.59% | 40.00% | 39.90% | 39.90% | 100.00% | ≤5000 ms |
| [RepeatsDB](https://repeatsdb.org/) | ELIXIR Italy | 🟢 up | 100.00% | 98.91% | 97.14% | 97.14% | 97.14% | 100.00% | ≤2000 ms |
| [REXdb](http://repeatexplorer.org/?page_id=918) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Rfam](https://rfam.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 99.95% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [Rhea](https://www.rhea-db.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [Riboseq.org](https://riboseq.org/) | ELIXIR Ireland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [RNA Central](https://rnacentral.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 98.64% | 98.64% | 98.64% | 100.00% | ≤2000 ms |
| [SABIO-RK](https://sabio.h-its.org/ui/search) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.95% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [SalmoBase](https://salmobase.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [SIBiLS](https://sibils.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 99.95% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [SIDER](https://sideeffects.embl.de/) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.71% | 99.71% | 99.71% | 100.00% | ≤2000 ms |
| [SIGNOR](http://signor.uniroma2.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 99.95% | 99.95% | 99.95% | 100.00% | ≤5000 ms |
| [SILVA](https://www.arb-silva.de/) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.08% | 99.03% | 99.03% | 100.00% | ≤1000 ms |
| [SMART](https://smart.embl.de/smart/change_mode.cgi) | ELIXIR Germany | 🟢 up | 100.00% | 98.76% | 99.03% | 99.03% | 99.03% | 100.00% | ≤2000 ms |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [sRNA Portal workflow](https://github.com/forestbiotech-lab/sRNA-Portal-workflow) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [STRING](https://string-db.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [SulfAtlas](https://sulfatlas.sb-roscoff.fr/sulfatlas/) | ELIXIR France | 🟢 up | 100.00% | 98.60% | 99.47% | 99.47% | 99.47% | 100.00% | ≤5000 ms |
| [SWICZ](http://proteom.biomed.cas.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [SWISS-MODEL Repository](https://swissmodel.expasy.org/repository) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [SwissLipids](https://www.swisslipids.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 99.95% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [SwissRegulon](https://swissregulon.unibas.ch/sr/swissregulon) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Tabloid Proteome](https://iomics.ugent.be/tabloidproteome/information.xhtml#about) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 99.76% | 99.76% | 99.76% | 100.00% | ≤1000 ms |
| [TFLink](https://tflink.net/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 75.63% | 75.45% | 75.45% | 100.00% | ≤5000 ms |
| [TmAlphaFold](https://tmalphafold.ttk.hu/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.90% | 99.90% | 99.90% | 100.00% | ≤5000 ms |
| [TOPDB](https://topdb.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.90% | 99.90% | 99.90% | 100.00% | ≤2000 ms |
| [Training Metrics Database](https://tmd.elixir-europe.org./world-map) | ELIXIR Sweden | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Translational Medicine Data Catalog (TMDC)](https://datacatalogue.elixir-luxembourg.org/) | ELIXIR Luxembourg | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [UniCatDB](https://www.unicatdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Unilectin](https://unilectin.unige.ch/) | ELIXIR Switzerland | 🟢 up | 100.00% | 99.69% | 87.14% | 87.17% | 87.17% | 100.00% | ≤1000 ms |
| [UniProtKB](https://www.uniprot.org/) | ELIXIR Switzerland, EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [UniTmp](https://www.unitmp.org/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.90% | 99.90% | 99.90% | 100.00% | ≤2000 ms |
| [UTRdb / UTRSite](http://utrdb.ba.itb.cnr.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [ValidatorDB](https://webchem.ncbr.muni.cz/Platform/ValidatorDb) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ValTrendsDB](https://valtrendsdb.biodata.ceitec.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [VEuPathDB](https://veupathdb.org/veupathdb/app) | ELIXIR UK | 🟢 up | 98.98% | 99.84% | 99.90% | 99.90% | 99.90% | 100.00% | ≤1000 ms |
| [ViralZone](https://viralzone.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 99.95% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [WatAA](https://watlas.datmos.org/wataa/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 85.69% | 95.53% | 95.54% | 95.54% | 100.00% | ≤2000 ms |
| [WheatIS](https://urgi.versailles.inrae.fr/wheatis/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [WikiPathways](https://www.wikipathways.org/index.php/WikiPathways) | ELIXIR Netherlands | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [YEASTRACT](https://yeastract-plus.org/) | ELIXIR Portugal | 🟢 up | 100.00% | 99.38% | 98.98% | 98.93% | 98.93% | 100.00% | ≤2000 ms |

---

## Recent state changes

The newest entries from `events.jsonl`, the full audit trail of every state change.

| When (UTC) | Resource | Change | Detail |
|---|---|---|---|
| 2026-10-17T23:30:43Z | ReMap | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T23:30:43Z | Ocean Gene Atlas | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T23:10:35Z | VEuPathDB | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T23:10:35Z | ReMap | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T23:10:35Z | PhylomeDB | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T23:10:35Z | PanDrugs | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T23:10:35Z | Ocean Gene Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T23:10:35Z | MetaPhOrs | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T23:10:35Z | HLA Ligand Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T23:10:35Z | GenomeHubs | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T23:10:35Z | Annotating PRincpial splice ISoforms (APPRIS) | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T22:50:28Z | VEuPathDB | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:50:28Z | PhylomeDB | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:50:28Z | PanDrugs | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:50:28Z | MetaPhOrs | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:50:28Z | HLA Ligand Atlas | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:50:28Z | GenomeHubs | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:50:28Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-10-17T22:50:28Z | Annotating PRincpial splice ISoforms (APPRIS) | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:32:30Z | ReMap | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:32:30Z | PanDrugs | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T22:32:30Z | Ocean Gene Atlas | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:30:41Z | ReMap | 🔴 down → 🟢 up | `ok` |
| 2026-10-17T22:30:41Z | PanDrugs | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-17T22:30:41Z | Ocean Gene Atlas | 🔴 down → 🟢 up | `ok` |

---

Generated by [uptime/scripts/summarize.py](https://github.com/gavinf97/ECD/blob/main/uptime/scripts/summarize.py) at **2026-10-17T23:52:02Z**, and rewritten after every check. Machine-readable: [summary.json](https://github.com/gavinf97/ECD/blob/uptime-data/summary.json).
