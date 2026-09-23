# ECD uptime status

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/monitoring.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml) [![up](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/up.json)](#all-resources) [![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/down.json)](#needs-attention) [![last check](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/last-check.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml)

## 🟢 Monitoring is ACTIVE

| | |
|---|---|
| **Resources monitored** | 163 — every one, every hour, continuously |
| **Last check** | 2026-09-23T23:44:36Z (2 min ago) |
| **Checks recorded** | 40 runs since monitoring began |
| **Runs on** | [GitHub Actions → uptime-check](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml) |
| **Visual dashboard** | https://gavinf97.github.io/ECD/ |

### Right now

🟢 up **129** · 🟡 challenged **11** · 🔴 down **23** · ⚪ never checked **0** · 🔗 check URL to review **6**

Uptime = (up + challenged) ÷ recorded checks. Coverage = recorded ÷ expected checks. 99.00% is the ECD reference target (ECD Process V1 §5); it sorts the list below and carries no deadline — monitoring simply continues. Full definitions: [uptime/README.md](https://github.com/gavinf97/ECD/blob/main/uptime/README.md).

---

## Needs attention

### 🔴 Currently down

**23** of 163 resources are not responding.

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
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_503` | 0.00% |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 2026-09-17T16:07:30Z | `read_timeout` | 0.00% |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 2026-09-22T14:58:18Z | `tls_error` | 77.50% |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 2026-09-22T14:58:18Z | `read_timeout` | 32.50% |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 2026-09-23T06:01:32Z | `connect_timeout` | 55.00% |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 2026-09-23T23:44:36Z | `read_timeout` | 40.00% |

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

**50** resources, worst first.

| Resource | Node | 30d uptime | 30d coverage | Down checks |
|---|---|---|---|---|
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 0.00% | 16.74% | 40 |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 0.00% | 16.74% | 40 |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 0.00% | 16.74% | 40 |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 0.00% | 16.74% | 40 |
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 0.00% | 16.74% | 40 |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 0.00% | 16.74% | 40 |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 0.00% | 16.74% | 40 |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 0.00% | 16.74% | 40 |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 0.00% | 16.74% | 40 |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 0.00% | 16.74% | 40 |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 32.50% | 16.74% | 27 |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 32.50% | 16.74% | 27 |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 32.50% | 16.74% | 27 |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 40.00% | 16.74% | 24 |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 55.00% | 16.74% | 18 |
| [MobiDB](http://mobidb.bio.unipd.it/) | ELIXIR Italy | 65.00% | 16.74% | 14 |
| [PICKLE](http://www.pickle.gr) | ELIXIR Greece | 65.00% | 16.74% | 14 |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 77.50% | 16.74% | 9 |
| [GENOMICUS](https://www.genomicus.bio.ens.psl.eu/genomicus-110.01/cgi-bin/search.pl) | ELIXIR France | 85.00% | 16.74% | 6 |
| [CATH/Gene3D](https://www.cathdb.info/) | ELIXIR UK | 87.50% | 16.74% | 5 |
| [IDSM](https://idsm.elixir-czech.cz/) | ELIXIR Czech Republic | 95.00% | 16.74% | 2 |
| [AgroLD (Agronomic Linked Data)](https://agrold.southgreen.fr/agrold) | ELIXIR France | 97.50% | 16.74% | 1 |
| [BacDive](https://bacdive.dsmz.de/) | ELIXIR Germany | 97.50% | 16.74% | 1 |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 97.50% | 16.74% | 1 |
| [BRENDA](https://www.brenda-enzymes.org/index.php) | ELIXIR Germany | 97.50% | 16.74% | 1 |
| [CorkOakDB](https://corkoakdb.org/) | ELIXIR Portugal | 97.50% | 16.74% | 1 |
| [DisProt](https://www.disprot.org/) | ELIXIR Italy | 97.50% | 16.74% | 1 |
| [DMPortal](https://dmportal.biodata.pt) | ELIXIR Portugal | 97.50% | 16.74% | 1 |
| [DOME Registry](https://registry.dome-ml.org) | ELIXIR Italy | 97.50% | 16.74% | 1 |
| [DOME-ML](https://dome-ml.org) | ELIXIR Italy | 97.50% | 16.74% | 1 |
| [Expression Atlas](https://www.ebi.ac.uk/gxa/home) | EMBL-EBI | 97.50% | 16.74% | 1 |
| [FINDbase](https://findbase.org/#/) | ELIXIR Greece | 97.50% | 16.74% | 1 |
| [MediaDive](https://mediadive.dsmz.de/) | ELIXIR Germany | 97.50% | 16.74% | 1 |
| [PED](https://proteinensemble.org/) | ELIXIR Italy | 97.50% | 16.74% | 1 |
| [RepeatsDB](https://repeatsdb.org/) | ELIXIR Italy | 97.50% | 16.74% | 1 |
| [SIBiLS](https://sibils.org/) | ELIXIR Switzerland | 97.50% | 16.74% | 1 |
| [SIDER](https://sideeffects.embl.de/) | ELIXIR Germany | 97.50% | 16.74% | 1 |
| [SILVA](https://www.arb-silva.de/) | ELIXIR Germany | 97.50% | 16.74% | 1 |
| [SMART](https://smart.embl.de/smart/change_mode.cgi) | ELIXIR Germany | 97.50% | 16.74% | 1 |
| [Tabloid Proteome](https://iomics.ugent.be/tabloidproteome/information.xhtml#about) | ELIXIR Belgium | 97.50% | 16.74% | 1 |
| [YEASTRACT](https://yeastract-plus.org/) | ELIXIR Portugal | 97.50% | 16.74% | 1 |

---

## All resources

All 163 resources, sorted by name. Sortable and searchable on the [dashboard](https://gavinf97.github.io/ECD/).

| Resource | Node | State | Today | 7d | 30d | 90d | 365d | Coverage 30d | p95 30d |
|---|---|---|---|---|---|---|---|---|---|
| [2Dprots](https://2dprots.ncbr.muni.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [3D interacting domains (3Did)](https://3did.irbbarcelona.org/) | ELIXIR Spain | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [AgroLD (Agronomic Linked Data)](https://agrold.southgreen.fr/agrold) | ELIXIR France | 🟢 up | 83.33% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤1000 ms |
| [AlphaFold DB](https://alphafold.ebi.ac.uk/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [AmtDB](https://amtdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [Annotating PRincpial splice ISoforms (APPRIS)](https://appris.bioinfo.cnio.es/) | ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [BacDive](https://bacdive.dsmz.de/) | ELIXIR Germany | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [BEGDB](http://www.begdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Bgee](https://www.bgee.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [BioImage Informatics Index (BISE)](https://biii.eu/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [biomaRt](https://bioconductor.org/packages/release/bioc/html/biomaRt.html) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤1000 ms |
| [BioSurfDB](https://www.biosurfdb.org) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [BRENDA](https://www.brenda-enzymes.org/index.php) | ELIXIR Germany | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤1000 ms |
| [CATH/Gene3D](https://www.cathdb.info/) | ELIXIR UK | 🟢 up | 100.00% | 87.50% | 87.50% | 87.50% | 87.50% | 16.74% | ≤1000 ms |
| [Cellosaurus](https://www.cellosaurus.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [ChannelsDB](https://channelsdb2.biodata.ceitec.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [ChEBI](https://www.ebi.ac.uk/chebi) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [ChEMBL](https://www.ebi.ac.uk/chembl/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [Collections and registries from the Finnish population: SISU data resource](https://www.sisuproject.fi/) | ELIXIR Finland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [CorkOakDB](https://corkoakdb.org/) | ELIXIR Portugal | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [DGP](https://pmc.ncbi.nlm.nih.gov/articles/PMC434425/) | ELIXIR Greece | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [DisProt](https://www.disprot.org/) | ELIXIR Italy | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [DMPortal](https://dmportal.biodata.pt) | ELIXIR Portugal | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤5000 ms |
| [Dolbico](https://dolbico.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [DOME Registry](https://registry.dome-ml.org) | ELIXIR Italy | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [DOME-ML](https://dome-ml.org) | ELIXIR Italy | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤5000 ms |
| [Ensembl](https://www.ensembl.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [ENZYME](https://enzyme.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Evolutionary genealogy of genes: Non-supervised Orthologous Groups (eggNOG)](https://eggnogdb.org/) | ELIXIR Germany, ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [EvoPPI](http://evoppi.i3s.up.pt/) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [Expression Atlas](https://www.ebi.ac.uk/gxa/home) | EMBL-EBI | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤5000 ms |
| [FAIDARE](https://urgi.versailles.inrae.fr/faidare/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤10000 ms |
| [FINDbase](https://findbase.org/#/) | ELIXIR Greece | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤1000 ms |
| [FireProtDB](https://loschmidt.chemi.muni.cz/fireprotdb/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Flybase](https://flybase.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [Galactosemia Proteins Database](https://www.elixir-italy.org/services/galactosemia-proteins-database/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 🔴 down | 16.67% | 55.00% | 55.00% | 55.00% | 55.00% | 16.74% | ≤2000 ms |
| [GenomeRNAi](https://genomernai.dkfz.de) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [GENOMICUS](https://www.genomicus.bio.ens.psl.eu/genomicus-110.01/cgi-bin/search.pl) | ELIXIR France | 🟢 up | 100.00% | 85.00% | 85.00% | 85.00% | 85.00% | 16.74% | ≤5000 ms |
| [GlobalFungi](https://globalfungi.com/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [GnpIS](https://urgi.versailles.inrae.fr/gnpis/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤10000 ms |
| [GO annotation (GOA)](https://www.ebi.ac.uk/GOA/index) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [GWAS Central](https://help.gwascentral.org/about/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [HAMAP](https://hamap.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [HCVIVdb](http://www.hcvivdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [HERVd](https://herv.img.cas.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [HGNC](https://www.genenames.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 🔴 down | 33.33% | 40.00% | 40.00% | 40.00% | 40.00% | 16.74% | >10000 ms |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [HTP](https://htp.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Human Protein Atlas (HPA)](https://www.proteinatlas.org/) | ELIXIR Sweden | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [IDSM](https://idsm.elixir-czech.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 95.00% | 95.00% | 95.00% | 95.00% | 16.74% | ≤2000 ms |
| [IMGT](https://www.imgt.org) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [InterMine](http://intermine.org) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [InterPro](https://www.ebi.ac.uk/interpro/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [iPtgxDBs](https://iptgxdb.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [IreSite](http://iresite.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [IUPHAR/BPS Guide to PHARMACOLOGY](https://www.guidetopharmacology.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [JASPAR](https://jaspar.elixir.no/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [LiceBase](https://licebase.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [MaCPepDB](https://macpepdb.cubimed.rub.de) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [MassBank](https://massbank.eu/MassBank//) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 🔴 down | 0.00% | 77.50% | 77.50% | 77.50% | 77.50% | 16.74% | ≤2000 ms |
| [MediaDive](https://mediadive.dsmz.de/) | ELIXIR Germany | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [MeltDB](https://meltdb.cebitec.uni-bielefeld.de/cgi-bin/login.cgi) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [MEM](https://biit.cs.ut.ee/mem/) | ELIXIR Estonia | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤10000 ms |
| [Metabolic Atlas](https://metabolicatlas.org/) | ELIXIR Sweden | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [MetaNetX](https://www.metanetx.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [MetaPhOrs](https://orthology.phylomedb.org/) | ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [MGnify](https://www.ebi.ac.uk/metagenomics/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [MHC Motif Atlas](http://mhcmotifatlas.org/home) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 🔴 down | 0.00% | 32.50% | 32.50% | 32.50% | 32.50% | 16.74% | >10000 ms |
| [Microbe Atlas](https://microbeatlas.org/landing) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [MirGeneDB](https://mirgenedb.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [MobiDB](http://mobidb.bio.unipd.it/) | ELIXIR Italy | 🟢 up | 100.00% | 65.00% | 65.00% | 65.00% | 65.00% | 16.74% | ≤5000 ms |
| [MOLGENIS](https://molgenis.github.io/) | ELIXIR Netherlands | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [MolMeDB](https://molmedb.upol.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Nextstrain](https://nextstrain.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 🟢 up | 33.33% | 32.50% | 32.50% | 32.50% | 32.50% | 16.74% | ≤2000 ms |
| [OLIDA](https://olida.ibsquare.be/) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [OMA](https://omabrowser.org/oma/home/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Omics Discovery Index (OmicsDI)](https://www.omicsdi.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [OmniPath](https://omnipathdb.org/) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [OMPdb](http://www.ompdb.org/) | ELIXIR Greece | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [OpenTargets Platform](https://platform.opentargets.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [Orphadata](https://www.orphadata.com/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [Orphanet](https://www.orpha.net/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [OrthoDB](https://www.orthodb.org) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [PanDrugs](https://www.pandrugs.org) | ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [ParameciumDB](https://paramecium.i2bc.paris-saclay.fr) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [PAXdb](https://pax-db.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [PDBTM](https://pdbtm.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [PED](https://proteinensemble.org/) | ELIXIR Italy | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [PHI-base](http://www.phi-base.org) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [PhylomeDB](https://phylomedb.org/) | ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [PICKLE](http://www.pickle.gr) | ELIXIR Greece | 🟢 up | 100.00% | 65.00% | 65.00% | 65.00% | 65.00% | 16.74% | >10000 ms |
| [PIPPA](https://pippa.psb.ugent.be/pippa_nav/home/) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [PolarProtDb](https://polarprotdb.ttk.hu/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [PomBase](https://www.pombase.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Progenetix](https://progenetix.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [PROSITE](https://prosite.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Reactome](https://reactome.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [REDIportal](https://rediportal.cloud.ba.infn.it/atlas/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 🟢 up | 33.33% | 32.50% | 32.50% | 32.50% | 32.50% | 16.74% | ≤5000 ms |
| [RepeatsDB](https://repeatsdb.org/) | ELIXIR Italy | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [REXdb](http://repeatexplorer.org/?page_id=918) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [Rfam](https://rfam.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Rhea](https://www.rhea-db.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [Riboseq.org](https://riboseq.org/) | ELIXIR Ireland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [RNA Central](https://rnacentral.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [SABIO-RK](https://sabio.h-its.org/ui/search) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [SalmoBase](https://salmobase.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [SIBiLS](https://sibils.org/) | ELIXIR Switzerland | 🟢 up | 83.33% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [SIDER](https://sideeffects.embl.de/) | ELIXIR Germany | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [SIGNOR](http://signor.uniroma2.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [SILVA](https://www.arb-silva.de/) | ELIXIR Germany | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤1000 ms |
| [SMART](https://smart.embl.de/smart/change_mode.cgi) | ELIXIR Germany | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [sRNA Portal workflow](https://github.com/forestbiotech-lab/sRNA-Portal-workflow) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [STRING](https://string-db.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [SulfAtlas](https://sulfatlas.sb-roscoff.fr/sulfatlas/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [SWICZ](http://proteom.biomed.cas.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [SWISS-MODEL Repository](https://swissmodel.expasy.org/repository) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [SwissLipids](https://www.swisslipids.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [SwissRegulon](https://swissregulon.unibas.ch/sr/swissregulon) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Tabloid Proteome](https://iomics.ugent.be/tabloidproteome/information.xhtml#about) | ELIXIR Belgium | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤1000 ms |
| [TFLink](https://tflink.net/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [TmAlphaFold](https://tmalphafold.ttk.hu/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [TOPDB](https://topdb.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [Training Metrics Database](https://tmd.elixir-europe.org./world-map) | ELIXIR Sweden | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [Translational Medicine Data Catalog (TMDC)](https://datacatalogue.elixir-luxembourg.org/) | ELIXIR Luxembourg | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 16.74% | — |
| [UniCatDB](https://www.unicatdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [Unilectin](https://unilectin.unige.ch/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [UniProtKB](https://www.uniprot.org/) | ELIXIR Switzerland, EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [UniTmp](https://www.unitmp.org/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [UTRdb / UTRSite](http://utrdb.ba.itb.cnr.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [ValidatorDB](https://webchem.ncbr.muni.cz/Platform/ValidatorDb) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [ValTrendsDB](https://valtrendsdb.biodata.ceitec.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤1000 ms |
| [VEuPathDB](https://veupathdb.org/veupathdb/app) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [ViralZone](https://viralzone.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [WatAA](https://watlas.datmos.org/wataa/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤2000 ms |
| [WheatIS](https://urgi.versailles.inrae.fr/wheatis/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤5000 ms |
| [WikiPathways](https://www.wikipathways.org/index.php/WikiPathways) | ELIXIR Netherlands | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 16.74% | ≤500 ms |
| [YEASTRACT](https://yeastract-plus.org/) | ELIXIR Portugal | 🟢 up | 100.00% | 97.50% | 97.50% | 97.50% | 97.50% | 16.74% | ≤2000 ms |

---

## Recent state changes

The newest entries from `events.jsonl`, the full audit trail of every state change.

| When (UTC) | Resource | Change | Detail |
|---|---|---|---|
| 2026-09-23T23:44:36Z | ReMap | 🔴 down → 🟢 up | `ok` |
| 2026-09-23T23:44:36Z | Ocean Gene Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-09-23T23:44:36Z | HLA Ligand Atlas | 🟢 up → 🔴 down | `read_timeout` |
| 2026-09-23T23:44:36Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-09-23T23:44:36Z | AgroLD (Agronomic Linked Data) | 🔴 down → 🟢 up | `ok` |
| 2026-09-23T20:26:00Z | DGP | 🟡 challenged → 🟢 up | `ok` |
| 2026-09-23T20:26:00Z | AgroLD (Agronomic Linked Data) | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-09-23T17:06:54Z | SIBiLS | 🔴 down → 🟢 up | `ok` |
| 2026-09-23T17:06:54Z | HLA Ligand Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-09-23T11:42:56Z | SIBiLS | 🟢 up → 🔴 down | `dns_error` |
| 2026-09-23T11:42:56Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-09-23T06:01:32Z | ReMap | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-09-23T06:01:32Z | Ocean Gene Atlas | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-09-23T06:01:32Z | GenomeHubs | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-09-23T06:01:32Z | DGP | 🟡 challenged → 🟢 up | `ok` |
| 2026-09-22T22:13:23Z | HLA Ligand Atlas | 🟢 up → 🔴 down | `read_timeout` |
| 2026-09-22T18:57:17Z | ReMap | 🔴 down → 🟢 up | `ok` |
| 2026-09-22T18:57:17Z | Ocean Gene Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-09-22T18:57:17Z | HLA Ligand Atlas | 🔴 down → 🟢 up | `http_403` |
| 2026-09-22T18:57:17Z | GenomeHubs | 🔴 down → 🟢 up | `ok` |
| 2026-09-22T14:58:18Z | Micro-CTvlab | 🟢 up → 🔴 down | `read_timeout` |
| 2026-09-22T14:58:18Z | MATRIXDB | 🟢 up → 🔴 down | `tls_error` |
| 2026-09-22T14:58:18Z | GenomeHubs | reason changed: `read_timeout` → `connect_timeout` | `connect_timeout` |
| 2026-09-22T14:58:18Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-09-22T10:01:30Z | Micro-CTvlab | 🔴 down → 🟢 up | `ok` |

---

Generated by [uptime/scripts/summarize.py](https://github.com/gavinf97/ECD/blob/main/uptime/scripts/summarize.py) at **2026-09-23T23:46:10Z**, and rewritten after every check. Machine-readable: [summary.json](https://github.com/gavinf97/ECD/blob/uptime-data/summary.json).
