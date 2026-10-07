# ECD uptime status

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/monitoring.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml) [![up](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/up.json)](#all-resources) [![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/down.json)](#needs-attention) [![last check](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/last-check.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml)

## 🟢 Monitoring is ACTIVE

| | |
|---|---|
| **Resources monitored** | 163 — every one, every 20 minutes, continuously |
| **Last check** | 2026-10-07T23:50:28Z (2 min ago) |
| **Runs in the last 24 h** | 87 of a target 72 |
| **Checks recorded** | 1154 runs since monitoring began |
| **Runs on** | [GitHub Actions → uptime-check](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml) |
| **Visual dashboard** | https://gavinf97.github.io/ECD/ |

### Right now

🟢 up **131** · 🟡 challenged **11** · 🔴 down **21** · ⚪ never checked **0** · 🔗 check URL to review **6**

Uptime = (up + challenged) ÷ recorded checks. Coverage = recorded ÷ expected checks. 99.00% is the ECD reference target (ECD Process V1 §5); it sorts the list below and carries no deadline — monitoring simply continues. Full definitions: [uptime/README.md](https://github.com/gavinf97/ECD/blob/main/uptime/README.md).

---

## Needs attention

### 🔴 Currently down

**21** of 163 resources are not responding.

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
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `connect_timeout` | 0.00% |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 2026-09-17T16:07:30Z | `connect_timeout` | 0.00% |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 2026-09-17T16:07:30Z | `connect_timeout` | 0.00% |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 2026-09-17T16:07:30Z | `dns_error` | 0.00% |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 2026-09-17T16:07:30Z | `dns_error` | 0.00% |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 2026-09-17T16:07:30Z | `read_timeout` | 0.00% |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 2026-09-22T14:58:18Z | `tls_error` | 2.69% |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 2026-10-05T17:50:32Z | `http_502` | 82.93% |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 2026-10-07T20:10:35Z | `connect_timeout` | 98.53% |

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

**55** resources, worst first.

| Resource | Node | 30d uptime | 30d coverage | Down checks |
|---|---|---|---|---|
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 0.00% | 100.00% | 1154 |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 0.00% | 100.00% | 1154 |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 0.00% | 100.00% | 1154 |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 0.00% | 100.00% | 1154 |
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 0.00% | 100.00% | 1154 |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 0.00% | 100.00% | 1154 |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 0.00% | 100.00% | 1154 |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 0.00% | 100.00% | 1154 |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 0.00% | 100.00% | 1154 |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 0.00% | 100.00% | 1154 |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 2.69% | 100.00% | 1123 |
| [iPtgxDBs](https://iptgxdb.expasy.org/) | ELIXIR Switzerland | 36.31% | 100.00% | 735 |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 37.18% | 100.00% | 725 |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 37.52% | 100.00% | 721 |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 56.24% | 100.00% | 505 |
| [MetaPhOrs](https://orthology.phylomedb.org/) | ELIXIR Spain | 61.35% | 100.00% | 446 |
| [PhylomeDB](https://phylomedb.org/) | ELIXIR Spain | 61.35% | 100.00% | 446 |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 67.33% | 100.00% | 377 |
| [PICKLE](http://www.pickle.gr) | ELIXIR Greece | 75.39% | 100.00% | 284 |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 76.17% | 100.00% | 275 |
| [Unilectin](https://unilectin.unige.ch/) | ELIXIR Switzerland | 77.38% | 100.00% | 261 |
| [MobiDB](http://mobidb.bio.unipd.it/) | ELIXIR Italy | 79.03% | 100.00% | 242 |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 81.37% | 100.00% | 215 |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 82.93% | 100.00% | 197 |
| [CATH/Gene3D](https://www.cathdb.info/) | ELIXIR UK | 91.42% | 100.00% | 99 |
| [MetaNetX](https://www.metanetx.org/) | ELIXIR Switzerland | 93.85% | 100.00% | 71 |
| [DisProt](https://www.disprot.org/) | ELIXIR Italy | 94.97% | 100.00% | 58 |
| [RepeatsDB](https://repeatsdb.org/) | ELIXIR Italy | 95.75% | 100.00% | 49 |
| [DOME-ML](https://dome-ml.org) | ELIXIR Italy | 95.84% | 100.00% | 48 |
| [Nextstrain](https://nextstrain.org/) | ELIXIR Switzerland | 95.84% | 100.00% | 48 |
| [PED](https://proteinensemble.org/) | ELIXIR Italy | 95.84% | 100.00% | 48 |
| [DOME Registry](https://registry.dome-ml.org) | ELIXIR Italy | 95.93% | 100.00% | 47 |
| [Omics Discovery Index (OmicsDI)](https://www.omicsdi.org/) | EMBL-EBI | 97.23% | 100.00% | 32 |
| [PAXdb](https://pax-db.org/) | ELIXIR Switzerland | 97.66% | 100.00% | 27 |
| [OMA](https://omabrowser.org/oma/home/) | ELIXIR Switzerland | 97.92% | 100.00% | 24 |
| [BRENDA](https://www.brenda-enzymes.org/index.php) | ELIXIR Germany | 98.01% | 100.00% | 23 |
| [BacDive](https://bacdive.dsmz.de/) | ELIXIR Germany | 98.09% | 100.00% | 22 |
| [PanDrugs](https://www.pandrugs.org) | ELIXIR Spain | 98.09% | 100.00% | 22 |
| [MediaDive](https://mediadive.dsmz.de/) | ELIXIR Germany | 98.27% | 100.00% | 20 |
| [SILVA](https://www.arb-silva.de/) | ELIXIR Germany | 98.27% | 100.00% | 20 |
| [YEASTRACT](https://yeastract-plus.org/) | ELIXIR Portugal | 98.44% | 100.00% | 18 |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 98.53% | 100.00% | 17 |
| [CorkOakDB](https://corkoakdb.org/) | ELIXIR Portugal | 98.53% | 100.00% | 17 |
| [DMPortal](https://dmportal.biodata.pt) | ELIXIR Portugal | 98.53% | 100.00% | 17 |
| [FINDbase](https://findbase.org/#/) | ELIXIR Greece | 98.53% | 100.00% | 17 |
| [AlphaFold DB](https://alphafold.ebi.ac.uk/) | EMBL-EBI | 98.87% | 100.00% | 13 |
| [AgroLD (Agronomic Linked Data)](https://agrold.southgreen.fr/agrold) | ELIXIR France | 98.96% | 100.00% | 12 |

---

## All resources

All 163 resources, sorted by name. Sortable and searchable on the [dashboard](https://gavinf97.github.io/ECD/).

| Resource | Node | State | Today | 7d | 30d | 90d | 365d | Coverage 30d | p95 30d |
|---|---|---|---|---|---|---|---|---|---|
| [2Dprots](https://2dprots.ncbr.muni.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [3D interacting domains (3Did)](https://3did.irbbarcelona.org/) | ELIXIR Spain | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [AgroLD (Agronomic Linked Data)](https://agrold.southgreen.fr/agrold) | ELIXIR France | 🟢 up | 100.00% | 99.04% | 98.96% | 98.96% | 98.96% | 100.00% | ≤1000 ms |
| [AlphaFold DB](https://alphafold.ebi.ac.uk/) | EMBL-EBI | 🟢 up | 100.00% | 98.72% | 98.87% | 98.87% | 98.87% | 100.00% | ≤5000 ms |
| [AmtDB](https://amtdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [Annotating PRincpial splice ISoforms (APPRIS)](https://appris.bioinfo.cnio.es/) | ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤1000 ms |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [BacDive](https://bacdive.dsmz.de/) | ELIXIR Germany | 🟢 up | 98.85% | 98.88% | 98.09% | 98.09% | 98.09% | 100.00% | ≤2000 ms |
| [BEGDB](http://www.begdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [Bgee](https://www.bgee.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [BioImage Informatics Index (BISE)](https://biii.eu/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [biomaRt](https://bioconductor.org/packages/release/bioc/html/biomaRt.html) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.39% | 99.39% | 99.39% | 100.00% | ≤1000 ms |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 🔴 down | 81.61% | 97.43% | 98.53% | 98.53% | 98.53% | 100.00% | ≤1000 ms |
| [BioSurfDB](https://www.biosurfdb.org) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [BRENDA](https://www.brenda-enzymes.org/index.php) | ELIXIR Germany | 🟢 up | 98.85% | 98.88% | 98.01% | 98.01% | 98.01% | 100.00% | ≤2000 ms |
| [CATH/Gene3D](https://www.cathdb.info/) | ELIXIR UK | 🟢 up | 95.40% | 91.01% | 91.42% | 91.42% | 91.42% | 100.00% | ≤1000 ms |
| [Cellosaurus](https://www.cellosaurus.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 99.84% | 99.91% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [ChannelsDB](https://channelsdb2.biodata.ceitec.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ChEBI](https://www.ebi.ac.uk/chebi) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ChEMBL](https://www.ebi.ac.uk/chembl/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [Collections and registries from the Finnish population: SISU data resource](https://www.sisuproject.fi/) | ELIXIR Finland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [CorkOakDB](https://corkoakdb.org/) | ELIXIR Portugal | 🟢 up | 98.85% | 99.04% | 98.53% | 98.53% | 98.53% | 100.00% | ≤2000 ms |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [DGP](https://pmc.ncbi.nlm.nih.gov/articles/PMC434425/) | ELIXIR Greece | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [DisProt](https://www.disprot.org/) | ELIXIR Italy | 🟢 up | 100.00% | 99.52% | 94.97% | 94.97% | 94.97% | 100.00% | ≤2000 ms |
| [DMPortal](https://dmportal.biodata.pt) | ELIXIR Portugal | 🟢 up | 98.85% | 99.04% | 98.53% | 98.53% | 98.53% | 100.00% | ≤5000 ms |
| [Dolbico](https://dolbico.org/) | ELIXIR Czech Republic | 🟢 up | 98.85% | 99.84% | 99.83% | 99.83% | 99.83% | 100.00% | ≤5000 ms |
| [DOME Registry](https://registry.dome-ml.org) | ELIXIR Italy | 🟢 up | 100.00% | 99.52% | 95.93% | 95.93% | 95.93% | 100.00% | ≤2000 ms |
| [DOME-ML](https://dome-ml.org) | ELIXIR Italy | 🟢 up | 100.00% | 99.52% | 95.84% | 95.84% | 95.84% | 100.00% | ≤2000 ms |
| [Ensembl](https://www.ensembl.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ENZYME](https://enzyme.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Evolutionary genealogy of genes: Non-supervised Orthologous Groups (eggNOG)](https://eggnogdb.org/) | ELIXIR Germany, ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [EvoPPI](http://evoppi.i3s.up.pt/) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Expression Atlas](https://www.ebi.ac.uk/gxa/home) | EMBL-EBI | 🟢 up | 100.00% | 99.84% | 99.39% | 99.39% | 99.39% | 100.00% | ≤2000 ms |
| [FAIDARE](https://urgi.versailles.inrae.fr/faidare/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [FINDbase](https://findbase.org/#/) | ELIXIR Greece | 🟢 up | 98.85% | 99.04% | 98.53% | 98.53% | 98.53% | 100.00% | ≤500 ms |
| [FireProtDB](https://loschmidt.chemi.muni.cz/fireprotdb/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.48% | 99.48% | 99.48% | 100.00% | ≤2000 ms |
| [Flybase](https://flybase.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [Galactosemia Proteins Database](https://www.elixir-italy.org/services/galactosemia-proteins-database/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 🔴 down | 0.00% | 68.38% | 82.93% | 82.93% | 82.93% | 100.00% | ≤2000 ms |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 🟢 up | 83.91% | 84.27% | 81.37% | 81.37% | 81.37% | 100.00% | ≤2000 ms |
| [GenomeRNAi](https://genomernai.dkfz.de) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [GENOMICUS](https://www.genomicus.bio.ens.psl.eu/genomicus-110.01/cgi-bin/search.pl) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 99.22% | 99.22% | 99.22% | 100.00% | ≤5000 ms |
| [GlobalFungi](https://globalfungi.com/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [GnpIS](https://urgi.versailles.inrae.fr/gnpis/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [GO annotation (GOA)](https://www.ebi.ac.uk/GOA/index) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [GWAS Central](https://help.gwascentral.org/about/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [HAMAP](https://hamap.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [HCVIVdb](http://www.hcvivdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [HERVd](https://herv.img.cas.cz/) | ELIXIR Czech Republic | 🟢 up | 98.85% | 99.52% | 99.22% | 99.22% | 99.22% | 100.00% | ≤2000 ms |
| [HGNC](https://www.genenames.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 🟢 up | 93.10% | 79.45% | 76.17% | 76.17% | 76.17% | 100.00% | >10000 ms |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [HTP](https://htp.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.83% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [Human Protein Atlas (HPA)](https://www.proteinatlas.org/) | ELIXIR Sweden | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [IDSM](https://idsm.elixir-czech.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.83% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [IMGT](https://www.imgt.org) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [InterMine](http://intermine.org) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [InterPro](https://www.ebi.ac.uk/interpro/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [iPtgxDBs](https://iptgxdb.expasy.org/) | ELIXIR Switzerland | 🟢 up | 35.63% | 4.98% | 36.31% | 36.31% | 36.31% | 100.00% | ≤2000 ms |
| [IreSite](http://iresite.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 99.84% | 99.91% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [IUPHAR/BPS Guide to PHARMACOLOGY](https://www.guidetopharmacology.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [JASPAR](https://jaspar.elixir.no/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [LiceBase](https://licebase.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [MaCPepDB](https://macpepdb.cubimed.rub.de) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [MassBank](https://massbank.eu/MassBank//) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 🔴 down | 0.00% | 0.00% | 2.69% | 2.69% | 2.69% | 100.00% | ≤2000 ms |
| [MediaDive](https://mediadive.dsmz.de/) | ELIXIR Germany | 🟢 up | 98.85% | 98.88% | 98.27% | 98.27% | 98.27% | 100.00% | ≤2000 ms |
| [MeltDB](https://meltdb.cebitec.uni-bielefeld.de/cgi-bin/login.cgi) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [MEM](https://biit.cs.ut.ee/mem/) | ELIXIR Estonia | 🟢 up | 100.00% | 99.52% | 99.65% | 99.65% | 99.65% | 100.00% | >10000 ms |
| [Metabolic Atlas](https://metabolicatlas.org/) | ELIXIR Sweden | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [MetaNetX](https://www.metanetx.org/) | ELIXIR Switzerland | 🟢 up | 97.70% | 96.15% | 93.85% | 93.85% | 93.85% | 100.00% | ≤5000 ms |
| [MetaPhOrs](https://orthology.phylomedb.org/) | ELIXIR Spain | 🟢 up | 100.00% | 29.05% | 61.35% | 61.35% | 61.35% | 100.00% | ≤5000 ms |
| [MGnify](https://www.ebi.ac.uk/metagenomics/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MHC Motif Atlas](http://mhcmotifatlas.org/home) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 🟢 up | 70.11% | 69.50% | 67.33% | 67.33% | 67.33% | 100.00% | >10000 ms |
| [Microbe Atlas](https://microbeatlas.org/landing) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [MirGeneDB](https://mirgenedb.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [MobiDB](http://mobidb.bio.unipd.it/) | ELIXIR Italy | 🟢 up | 100.00% | 94.38% | 79.03% | 79.03% | 79.03% | 100.00% | ≤5000 ms |
| [MOLGENIS](https://molgenis.github.io/) | ELIXIR Netherlands | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [MolMeDB](https://molmedb.upol.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Nextstrain](https://nextstrain.org/) | ELIXIR Switzerland | 🟢 up | 98.85% | 98.07% | 95.84% | 95.84% | 95.84% | 100.00% | ≤1000 ms |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 🟢 up | 47.13% | 39.49% | 37.18% | 37.18% | 37.18% | 100.00% | ≤2000 ms |
| [OLIDA](https://olida.ibsquare.be/) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤1000 ms |
| [OMA](https://omabrowser.org/oma/home/) | ELIXIR Switzerland | 🟢 up | 100.00% | 97.75% | 97.92% | 97.92% | 97.92% | 100.00% | ≤5000 ms |
| [Omics Discovery Index (OmicsDI)](https://www.omicsdi.org/) | EMBL-EBI | 🟢 up | 88.51% | 96.31% | 97.23% | 97.23% | 97.23% | 100.00% | ≤10000 ms |
| [OmniPath](https://omnipathdb.org/) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [OMPdb](http://www.ompdb.org/) | ELIXIR Greece | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [OpenTargets Platform](https://platform.opentargets.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [Orphadata](https://www.orphadata.com/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [Orphanet](https://www.orpha.net/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [OrthoDB](https://www.orthodb.org) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [PanDrugs](https://www.pandrugs.org) | ELIXIR Spain | 🟢 up | 96.55% | 98.72% | 98.09% | 98.09% | 98.09% | 100.00% | ≤1000 ms |
| [ParameciumDB](https://paramecium.i2bc.paris-saclay.fr) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤5000 ms |
| [PAXdb](https://pax-db.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 97.66% | 97.66% | 97.66% | 100.00% | ≤1000 ms |
| [PDBTM](https://pdbtm.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.83% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [PED](https://proteinensemble.org/) | ELIXIR Italy | 🟢 up | 100.00% | 99.52% | 95.84% | 95.84% | 95.84% | 100.00% | ≤2000 ms |
| [PHI-base](http://www.phi-base.org) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [PhylomeDB](https://phylomedb.org/) | ELIXIR Spain | 🟢 up | 100.00% | 29.05% | 61.35% | 61.35% | 61.35% | 100.00% | ≤2000 ms |
| [PICKLE](http://www.pickle.gr) | ELIXIR Greece | 🟢 up | 56.32% | 67.09% | 75.39% | 75.39% | 75.39% | 100.00% | >10000 ms |
| [PIPPA](https://pippa.psb.ugent.be/pippa_nav/home/) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [PolarProtDb](https://polarprotdb.ttk.hu/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.83% | 99.83% | 99.83% | 100.00% | ≤5000 ms |
| [PomBase](https://www.pombase.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Progenetix](https://progenetix.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [PROSITE](https://prosite.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Reactome](https://reactome.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [REDIportal](https://rediportal.cloud.ba.infn.it/atlas/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 🟢 up | 47.13% | 40.13% | 37.52% | 37.52% | 37.52% | 100.00% | ≤5000 ms |
| [RepeatsDB](https://repeatsdb.org/) | ELIXIR Italy | 🟢 up | 100.00% | 99.52% | 95.75% | 95.75% | 95.75% | 100.00% | ≤2000 ms |
| [REXdb](http://repeatexplorer.org/?page_id=918) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Rfam](https://rfam.org/) | EMBL-EBI | 🟢 up | 100.00% | 99.84% | 99.91% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [Rhea](https://www.rhea-db.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [Riboseq.org](https://riboseq.org/) | ELIXIR Ireland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [RNA Central](https://rnacentral.org/) | EMBL-EBI | 🟢 up | 100.00% | 99.52% | 99.74% | 99.74% | 99.74% | 100.00% | ≤1000 ms |
| [SABIO-RK](https://sabio.h-its.org/ui/search) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤1000 ms |
| [SalmoBase](https://salmobase.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [SIBiLS](https://sibils.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [SIDER](https://sideeffects.embl.de/) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.48% | 99.48% | 99.48% | 100.00% | ≤2000 ms |
| [SIGNOR](http://signor.uniroma2.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤5000 ms |
| [SILVA](https://www.arb-silva.de/) | ELIXIR Germany | 🟢 up | 98.85% | 98.88% | 98.27% | 98.27% | 98.27% | 100.00% | ≤1000 ms |
| [SMART](https://smart.embl.de/smart/change_mode.cgi) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.48% | 99.48% | 99.48% | 100.00% | ≤2000 ms |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [sRNA Portal workflow](https://github.com/forestbiotech-lab/sRNA-Portal-workflow) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [STRING](https://string-db.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [SulfAtlas](https://sulfatlas.sb-roscoff.fr/sulfatlas/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 99.83% | 99.83% | 99.83% | 100.00% | ≤5000 ms |
| [SWICZ](http://proteom.biomed.cas.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [SWISS-MODEL Repository](https://swissmodel.expasy.org/repository) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [SwissLipids](https://www.swisslipids.org/) | ELIXIR Switzerland | 🟢 up | 98.85% | 99.84% | 99.91% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [SwissRegulon](https://swissregulon.unibas.ch/sr/swissregulon) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Tabloid Proteome](https://iomics.ugent.be/tabloidproteome/information.xhtml#about) | ELIXIR Belgium | 🟢 up | 100.00% | 99.68% | 99.57% | 99.57% | 99.57% | 100.00% | ≤1000 ms |
| [TFLink](https://tflink.net/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 56.24% | 56.24% | 56.24% | 100.00% | ≤5000 ms |
| [TmAlphaFold](https://tmalphafold.ttk.hu/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.83% | 99.83% | 99.83% | 100.00% | ≤5000 ms |
| [TOPDB](https://topdb.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.83% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [Training Metrics Database](https://tmd.elixir-europe.org./world-map) | ELIXIR Sweden | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Translational Medicine Data Catalog (TMDC)](https://datacatalogue.elixir-luxembourg.org/) | ELIXIR Luxembourg | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [UniCatDB](https://www.unicatdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Unilectin](https://unilectin.unige.ch/) | ELIXIR Switzerland | 🟢 up | 100.00% | 99.84% | 77.38% | 77.38% | 77.38% | 100.00% | ≤1000 ms |
| [UniProtKB](https://www.uniprot.org/) | ELIXIR Switzerland, EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [UniTmp](https://www.unitmp.org/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 99.83% | 99.83% | 99.83% | 100.00% | ≤2000 ms |
| [UTRdb / UTRSite](http://utrdb.ba.itb.cnr.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [ValidatorDB](https://webchem.ncbr.muni.cz/Platform/ValidatorDb) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ValTrendsDB](https://valtrendsdb.biodata.ceitec.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [VEuPathDB](https://veupathdb.org/veupathdb/app) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤500 ms |
| [ViralZone](https://viralzone.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 99.91% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [WatAA](https://watlas.datmos.org/wataa/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [WheatIS](https://urgi.versailles.inrae.fr/wheatis/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [WikiPathways](https://www.wikipathways.org/index.php/WikiPathways) | ELIXIR Netherlands | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [YEASTRACT](https://yeastract-plus.org/) | ELIXIR Portugal | 🟢 up | 98.85% | 98.88% | 98.44% | 98.44% | 98.44% | 100.00% | ≤2000 ms |

---

## Recent state changes

The newest entries from `events.jsonl`, the full audit trail of every state change.

| When (UTC) | Resource | Change | Detail |
|---|---|---|---|
| 2026-10-07T23:50:28Z | SwissLipids | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T23:50:28Z | PICKLE | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T23:50:28Z | MetaNetX | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T23:50:28Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-10-07T23:30:41Z | SwissLipids | 🟢 up → 🔴 down | `dns_error` |
| 2026-10-07T23:30:41Z | ReMap | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T23:30:41Z | PICKLE | 🟢 up → 🔴 down | `read_timeout` |
| 2026-10-07T23:30:41Z | Ocean Gene Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T23:30:41Z | Micro-CTvlab | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T23:30:41Z | MetaNetX | 🟢 up → 🔴 down | `dns_error` |
| 2026-10-07T23:10:31Z | ReMap | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-07T23:10:31Z | PICKLE | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T23:10:31Z | Ocean Gene Atlas | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-07T23:10:31Z | Micro-CTvlab | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-10-07T23:10:31Z | DGP | 🟡 challenged → 🟢 up | `ok` |
| 2026-10-07T22:50:28Z | Micro-CTvlab | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T22:50:28Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-10-07T22:50:28Z | CATH/Gene3D | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T22:30:41Z | Micro-CTvlab | 🟢 up → 🔴 down | `read_timeout` |
| 2026-10-07T22:30:41Z | CATH/Gene3D | 🟢 up → 🔴 down | `read_timeout` |
| 2026-10-07T22:18:01Z | HLA Ligand Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T22:18:01Z | GenomeHubs | 🔴 down → 🟢 up | `ok` |
| 2026-10-07T22:18:01Z | DGP | 🟡 challenged → 🟢 up | `ok` |
| 2026-10-07T22:12:26Z | PICKLE | 🟢 up → 🔴 down | `read_timeout` |
| 2026-10-07T22:12:26Z | Micro-CTvlab | 🔴 down → 🟢 up | `ok` |

---

Generated by [uptime/scripts/summarize.py](https://github.com/gavinf97/ECD/blob/main/uptime/scripts/summarize.py) at **2026-10-07T23:52:07Z**, and rewritten after every check. Machine-readable: [summary.json](https://github.com/gavinf97/ECD/blob/uptime-data/summary.json).
