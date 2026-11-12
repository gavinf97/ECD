# ECD uptime status

[![monitoring](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/monitoring.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml) [![up](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/up.json)](#all-resources) [![down](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/down.json)](#needs-attention) [![last check](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gavinf97/ECD/uptime-data/badges/last-check.json)](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml)

## 🟢 Monitoring is ACTIVE

| | |
|---|---|
| **Resources monitored** | 163 — every one, every 20 minutes, continuously |
| **Last check** | 2026-11-12T23:50:34Z (2 min ago) |
| **Runs in the last 24 h** | 84 of a target 72 |
| **Checks recorded** | 4391 runs since monitoring began |
| **Runs on** | [GitHub Actions → uptime-check](https://github.com/gavinf97/ECD/actions/workflows/uptime-check.yml) |
| **Visual dashboard** | https://gavinf97.github.io/ECD/ |

### Right now

🟢 up **130** · 🟡 challenged **10** · 🔴 down **23** · ⚪ never checked **0** · 🔗 check URL to review **6**

Uptime = (up + challenged) ÷ recorded checks. Coverage = recorded ÷ expected checks. 99.00% is the ECD reference target (ECD Process V1 §5); it sorts the list below and carries no deadline — monitoring simply continues. Full definitions: [uptime/README.md](https://github.com/gavinf97/ECD/blob/main/uptime/README.md).

---

## Needs attention

### 🔴 Currently down

**23** of 163 resources are not responding.

| Resource | Node | Since (UTC) | Reason | 30d uptime |
|---|---|---|---|---|
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 2026-09-17T16:07:30Z | `tls_error` | 0.00% |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 2026-09-17T16:07:30Z | `http_404` 🔗 | 0.00% |
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
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 2026-09-22T14:58:18Z | `tls_error` | 0.00% |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 2026-10-21T14:10:32Z | `http_503` | 26.38% |
| [SWICZ](http://proteom.biomed.cas.cz/) | ELIXIR Czech Republic | 2026-10-21T19:10:32Z | `connect_timeout` | 27.11% |
| [PIPPA](https://pippa.psb.ugent.be/pippa_nav/home/) | ELIXIR Belgium | 2026-10-21T20:03:12Z | `connect_timeout` | 27.26% |
| [MetaPhOrs](https://orthology.phylomedb.org/) | ELIXIR Spain | 2026-11-04T11:30:47Z | `http_503` | 68.75% |
| [PhylomeDB](https://phylomedb.org/) | ELIXIR Spain | 2026-11-04T11:30:47Z | `http_503` | 68.78% |
| [Dolbico](https://dolbico.org/) | ELIXIR Czech Republic | 2026-11-08T12:30:48Z | `tls_error` | 80.75% |

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

**72** resources, worst first.

| Resource | Node | 30d uptime | 30d coverage | Down checks |
|---|---|---|---|---|
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 0.00% | 100.00% | 2707 |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 0.00% | 100.00% | 2707 |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 0.00% | 100.00% | 2707 |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 0.00% | 100.00% | 2707 |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 0.00% | 100.00% | 2707 |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 0.00% | 100.00% | 2707 |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 0.00% | 100.00% | 2707 |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 0.00% | 100.00% | 2707 |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 0.00% | 100.00% | 2707 |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 0.00% | 100.00% | 2707 |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 0.00% | 100.00% | 2707 |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 0.00% | 100.00% | 2707 |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 0.00% | 100.00% | 2707 |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 0.00% | 100.00% | 2707 |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 0.00% | 100.00% | 2707 |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 0.00% | 100.00% | 2707 |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 0.00% | 100.00% | 2707 |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 26.38% | 100.00% | 1993 |
| [SWICZ](http://proteom.biomed.cas.cz/) | ELIXIR Czech Republic | 27.11% | 100.00% | 1973 |
| [PIPPA](https://pippa.psb.ugent.be/pippa_nav/home/) | ELIXIR Belgium | 27.26% | 100.00% | 1969 |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 33.36% | 100.00% | 1804 |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 33.73% | 100.00% | 1794 |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 34.10% | 100.00% | 1784 |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 55.26% | 100.00% | 1211 |
| [SIGNOR](http://signor.uniroma2.it/) | ELIXIR Italy | 57.67% | 100.00% | 1146 |
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 57.70% | 100.00% | 1145 |
| [PICKLE](http://www.pickle.gr) | ELIXIR Greece | 64.57% | 100.00% | 959 |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 65.83% | 100.00% | 925 |
| [Unilectin](https://unilectin.unige.ch/) | ELIXIR Switzerland | 66.97% | 100.00% | 894 |
| [MetaPhOrs](https://orthology.phylomedb.org/) | ELIXIR Spain | 68.75% | 100.00% | 846 |
| [PhylomeDB](https://phylomedb.org/) | ELIXIR Spain | 68.78% | 100.00% | 845 |
| [2Dprots](https://2dprots.ncbr.muni.cz/) | ELIXIR Czech Republic | 71.19% | 100.00% | 780 |
| [GENOMICUS](https://www.genomicus.bio.ens.psl.eu/genomicus-110.01/cgi-bin/search.pl) | ELIXIR France | 78.91% | 100.00% | 571 |
| [Dolbico](https://dolbico.org/) | ELIXIR Czech Republic | 80.75% | 100.00% | 521 |
| [3D interacting domains (3Did)](https://3did.irbbarcelona.org/) | ELIXIR Spain | 89.10% | 100.00% | 295 |
| [Expression Atlas](https://www.ebi.ac.uk/gxa/home) | EMBL-EBI | 90.69% | 100.00% | 252 |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 91.39% | 100.00% | 233 |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 92.39% | 100.00% | 206 |
| [MaCPepDB](https://macpepdb.cubimed.rub.de) | ELIXIR Germany | 92.61% | 100.00% | 200 |
| [AlphaFold DB](https://alphafold.ebi.ac.uk/) | EMBL-EBI | 93.09% | 100.00% | 187 |
| [MediaDive](https://mediadive.dsmz.de/) | ELIXIR Germany | 93.68% | 100.00% | 171 |
| [Tabloid Proteome](https://iomics.ugent.be/tabloidproteome/information.xhtml#about) | ELIXIR Belgium | 93.76% | 100.00% | 169 |
| [WatAA](https://watlas.datmos.org/wataa/) | ELIXIR Czech Republic | 93.83% | 100.00% | 167 |
| [SIDER](https://sideeffects.embl.de/) | ELIXIR Germany | 94.09% | 100.00% | 160 |
| [ParameciumDB](https://paramecium.i2bc.paris-saclay.fr) | ELIXIR France | 94.13% | 100.00% | 159 |
| [ValTrendsDB](https://valtrendsdb.biodata.ceitec.cz/) | ELIXIR Czech Republic | 94.31% | 100.00% | 154 |
| [GlobalFungi](https://globalfungi.com/) | ELIXIR Czech Republic | 95.75% | 100.00% | 115 |
| [PHI-base](http://www.phi-base.org) | ELIXIR UK | 95.86% | 100.00% | 112 |
| [MeltDB](https://meltdb.cebitec.uni-bielefeld.de/cgi-bin/login.cgi) | ELIXIR Germany | 96.42% | 100.00% | 97 |
| [AmtDB](https://amtdb.org/) | ELIXIR Czech Republic | 96.60% | 100.00% | 92 |
| [ChannelsDB](https://channelsdb2.biodata.ceitec.cz/) | ELIXIR Czech Republic | 96.68% | 100.00% | 90 |
| [HTP](https://htp.unitmp.org) | ELIXIR Hungary | 96.75% | 100.00% | 88 |
| [PDBTM](https://pdbtm.unitmp.org) | ELIXIR Hungary | 96.79% | 100.00% | 87 |
| [PolarProtDb](https://polarprotdb.ttk.hu/) | ELIXIR Hungary | 96.79% | 100.00% | 87 |
| [TmAlphaFold](https://tmalphafold.ttk.hu/) | ELIXIR Hungary | 96.79% | 100.00% | 87 |
| [TOPDB](https://topdb.unitmp.org) | ELIXIR Hungary | 96.79% | 100.00% | 87 |
| [UniTmp](https://www.unitmp.org/) | ELIXIR Hungary | 96.79% | 100.00% | 87 |
| [MassBank](https://massbank.eu/MassBank/) | ELIXIR Germany | 96.97% | 100.00% | 82 |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 97.01% | 100.00% | 81 |
| [SWISS-MODEL Repository](https://swissmodel.expasy.org/repository) | ELIXIR Switzerland | 97.16% | 100.00% | 77 |
| [PanDrugs](https://www.pandrugs.org) | ELIXIR Spain | 97.23% | 100.00% | 75 |
| [SwissRegulon](https://swissregulon.unibas.ch/sr/swissregulon) | ELIXIR Switzerland | 97.30% | 100.00% | 73 |
| [iPtgxDBs](https://iptgxdb.expasy.org/) | ELIXIR Switzerland | 97.34% | 100.00% | 72 |
| [IMGT](https://www.imgt.org) | ELIXIR France | 97.52% | 100.00% | 67 |
| [BioSurfDB](https://www.biosurfdb.org) | ELIXIR Portugal | 97.67% | 100.00% | 63 |
| [Omics Discovery Index (OmicsDI)](https://www.omicsdi.org/) | EMBL-EBI | 97.67% | 100.00% | 63 |
| [YEASTRACT](https://yeastract-plus.org/) | ELIXIR Portugal | 97.71% | 100.00% | 62 |
| [RNA Central](https://rnacentral.org/) | EMBL-EBI | 98.19% | 100.00% | 49 |
| [Nextstrain](https://nextstrain.org/) | ELIXIR Switzerland | 98.74% | 100.00% | 34 |
| [RepeatsDB](https://repeatsdb.org/) | ELIXIR Italy | 98.78% | 100.00% | 33 |
| [SulfAtlas](https://sulfatlas.sb-roscoff.fr/sulfatlas/) | ELIXIR France | 98.85% | 100.00% | 31 |
| [FINDbase](https://findbase.org/#/) | ELIXIR Greece | 98.93% | 100.00% | 29 |

---

## All resources

All 163 resources, sorted by name. Sortable and searchable on the [dashboard](https://gavinf97.github.io/ECD/).

| Resource | Node | State | Today | 7d | 30d | 90d | 365d | Coverage 30d | p95 30d |
|---|---|---|---|---|---|---|---|---|---|
| [2Dprots](https://2dprots.ncbr.muni.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 96.52% | 71.19% | 79.98% | 79.98% | 100.00% | ≤2000 ms |
| [3D interacting domains (3Did)](https://3did.irbbarcelona.org/) | ELIXIR Spain | 🟢 up | 79.76% | 79.10% | 89.10% | 93.28% | 93.28% | 100.00% | ≤1000 ms |
| [AgroLD (Agronomic Linked Data)](https://agrold.southgreen.fr/agrold) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 99.78% | 99.57% | 99.57% | 100.00% | ≤1000 ms |
| [AlphaFold DB](https://alphafold.ebi.ac.uk/) | EMBL-EBI | 🟢 up | 100.00% | 77.11% | 93.09% | 95.29% | 95.29% | 100.00% | ≤10000 ms |
| [AmtDB](https://amtdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 96.60% | 97.90% | 97.90% | 100.00% | ≤2000 ms |
| [ANISEED](https://www.aniseed.cnrs.fr/) | ELIXIR France | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [Annotating PRincpial splice ISoforms (APPRIS)](https://appris.bioinfo.cnio.es/) | ELIXIR Spain | 🟢 up | 100.00% | 99.83% | 99.82% | 99.86% | 99.86% | 100.00% | ≤1000 ms |
| [AspicDB](https://rediportal.cloud.ba.infn.it/ASPicDB/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [BacDive](https://bacdive.dsmz.de/) | ELIXIR Germany | 🟢 up | 100.00% | 99.83% | 99.70% | 99.32% | 99.32% | 100.00% | ≤5000 ms |
| [BEGDB](http://www.begdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 99.98% | 99.98% | 100.00% | ≤5000 ms |
| [Bgee](https://www.bgee.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [BioImage Informatics Index (BISE)](https://biii.eu/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [biomaRt](https://bioconductor.org/packages/release/bioc/html/biomaRt.html) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 100.00% | 99.84% | 99.84% | 100.00% | ≤1000 ms |
| [Biophysical Proteome Atlas](https://bio2byte.be/proteome/) | ELIXIR Belgium | 🟢 up | 100.00% | 96.02% | 91.39% | 93.65% | 93.65% | 100.00% | ≤1000 ms |
| [BioSurfDB](https://www.biosurfdb.org) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 97.67% | 98.57% | 98.57% | 100.00% | ≤2000 ms |
| [BRENDA](https://www.brenda-enzymes.org/index.php) | ELIXIR Germany | 🟢 up | 100.00% | 99.67% | 99.78% | 99.34% | 99.34% | 100.00% | ≤2000 ms |
| [CATH/Gene3D](https://www.cathdb.info/) | ELIXIR UK | 🟢 up | 98.81% | 99.83% | 99.56% | 97.43% | 97.43% | 100.00% | ≤1000 ms |
| [Cellosaurus](https://www.cellosaurus.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 99.83% | 99.96% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [ChannelsDB](https://channelsdb2.biodata.ceitec.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 96.68% | 97.95% | 97.95% | 100.00% | ≤2000 ms |
| [ChEBI](https://www.ebi.ac.uk/chebi) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ChEMBL](https://www.ebi.ac.uk/chembl/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ChIPSummitDB](https://summit.med.unideb.hu/summitdb/) | ELIXIR Hungary | 🟢 up | 100.00% | 99.83% | 34.10% | 21.02% | 21.02% | 100.00% | ≤2000 ms |
| [Collections and registries from the Finnish population: SISU data resource](https://www.sisuproject.fi/) | ELIXIR Finland | 🟡 challenged | 100.00% | 100.00% | 99.96% | 99.98% | 99.98% | 100.00% | ≤1000 ms |
| [CorkOakDB](https://corkoakdb.org/) | ELIXIR Portugal | 🟢 up | 100.00% | 99.83% | 99.78% | 99.48% | 99.48% | 100.00% | ≤2000 ms |
| [DEEP data portal](https://deep.dkfz.de/#/home) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [DGP](https://pmc.ncbi.nlm.nih.gov/articles/PMC434425/) | ELIXIR Greece | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [DisProt](https://www.disprot.org/) | ELIXIR Italy | 🟢 up | 100.00% | 99.67% | 99.52% | 98.31% | 98.31% | 100.00% | ≤2000 ms |
| [DMPortal](https://dmportal.biodata.pt) | ELIXIR Portugal | 🟢 up | 98.81% | 99.67% | 99.59% | 99.36% | 99.36% | 100.00% | ≤5000 ms |
| [Dolbico](https://dolbico.org/) | ELIXIR Czech Republic | 🔴 down | 0.00% | 36.82% | 80.75% | 88.09% | 88.09% | 100.00% | ≤5000 ms |
| [DOME Registry](https://registry.dome-ml.org) | ELIXIR Italy | 🟢 up | 100.00% | 99.67% | 99.63% | 98.63% | 98.63% | 100.00% | ≤2000 ms |
| [DOME-ML](https://dome-ml.org) | ELIXIR Italy | 🟢 up | 100.00% | 99.67% | 99.63% | 98.61% | 98.61% | 100.00% | ≤2000 ms |
| [Ensembl](https://www.ensembl.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ENZYME](https://enzyme.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Evolutionary genealogy of genes: Non-supervised Orthologous Groups (eggNOG)](https://eggnogdb.org/) | ELIXIR Germany, ELIXIR Spain | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [EvoPPI](http://evoppi.i3s.up.pt/) | ELIXIR Portugal | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Expression Atlas](https://www.ebi.ac.uk/gxa/home) | EMBL-EBI | 🟢 up | 100.00% | 98.51% | 90.69% | 93.99% | 93.99% | 100.00% | ≤10000 ms |
| [FAIDARE](https://urgi.versailles.inrae.fr/faidare/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [FINDbase](https://findbase.org/#/) | ELIXIR Greece | 🟢 up | 97.62% | 99.00% | 98.93% | 98.86% | 98.86% | 100.00% | ≤500 ms |
| [FireProtDB](https://loschmidt.chemi.muni.cz/fireprotdb/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 99.86% | 99.86% | 100.00% | ≤2000 ms |
| [Flybase](https://flybase.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 99.89% | 99.93% | 99.93% | 100.00% | ≤500 ms |
| [Galactosemia Proteins Database](https://www.elixir-italy.org/services/galactosemia-proteins-database/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 99.96% | 99.98% | 99.98% | 100.00% | ≤2000 ms |
| [GenomeCRISPR](https://genomecrispr.dkfz.de/) | ELIXIR Germany | 🟢 up | 98.81% | 48.26% | 33.73% | 42.59% | 42.59% | 100.00% | ≤2000 ms |
| [GenomeHubs](https://www.southgreen.fr/genomehubs) | ELIXIR France | 🟢 up | 97.62% | 97.18% | 92.39% | 88.91% | 88.91% | 100.00% | ≤2000 ms |
| [GenomeRNAi](https://genomernai.dkfz.de) | ELIXIR Germany | 🟢 up | 100.00% | 99.50% | 99.74% | 99.82% | 99.82% | 100.00% | ≤2000 ms |
| [GENOMICUS](https://www.genomicus.bio.ens.psl.eu/genomicus-110.01/cgi-bin/search.pl) | ELIXIR France | 🟢 up | 100.00% | 99.83% | 78.91% | 86.59% | 86.59% | 100.00% | ≤5000 ms |
| [GlobalFungi](https://globalfungi.com/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 95.75% | 97.38% | 97.38% | 100.00% | ≤2000 ms |
| [GnpIS](https://urgi.versailles.inrae.fr/gnpis/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [GO annotation (GOA)](https://www.ebi.ac.uk/GOA/index) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [GWAS Central](https://help.gwascentral.org/about/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 99.15% | 99.48% | 99.48% | 100.00% | ≤5000 ms |
| [HAMAP](https://hamap.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [HCVIVdb](http://www.hcvivdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.89% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [HERVd](https://herv.img.cas.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 99.83% | 99.26% | 99.29% | 99.29% | 100.00% | ≤2000 ms |
| [HGNC](https://www.genenames.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [HLA Ligand Atlas](https://hla-ligand-atlas.org/welcome) | ELIXIR Germany | 🟢 up | 92.86% | 53.90% | 65.83% | 71.35% | 71.35% | 100.00% | >10000 ms |
| [HmtDB](http://www.hmtdb.uniba.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [HTP](https://htp.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 96.75% | 97.95% | 97.95% | 100.00% | ≤2000 ms |
| [Human Protein Atlas (HPA)](https://www.proteinatlas.org/) | ELIXIR Sweden | 🟢 up | 100.00% | 100.00% | 99.82% | 99.82% | 99.82% | 100.00% | ≤2000 ms |
| [IDSM](https://idsm.elixir-czech.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.93% | 99.82% | 99.82% | 100.00% | ≤2000 ms |
| [IMGT](https://www.imgt.org) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 97.52% | 98.47% | 98.47% | 100.00% | ≤2000 ms |
| [InterMine](http://intermine.org) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [InterPro](https://www.ebi.ac.uk/interpro/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [iPtgxDBs](https://iptgxdb.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 97.34% | 81.62% | 81.62% | 100.00% | ≤2000 ms |
| [IreSite](http://iresite.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.93% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [Italian COVID-19 Data Portal](https://www.covid19dataportal.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [ITSoneDB](https://itsonedb.cloud.ba.infn.it/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [IUPHAR/BPS Guide to PHARMACOLOGY](https://www.guidetopharmacology.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [JASPAR](https://jaspar.elixir.no/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [LiceBase](https://licebase.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [MaCPepDB](https://macpepdb.cubimed.rub.de) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 92.61% | 95.42% | 95.42% | 100.00% | ≤1000 ms |
| [Marine Metagenomics Portal (MMP)](https://mmp.sfb.uit.no) | ELIXIR Norway | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [MassBank](https://massbank.eu/MassBank/) | ELIXIR Germany | 🟢 up | 98.81% | 99.83% | 96.97% | 98.13% | 98.13% | 100.00% | ≤1000 ms |
| [MATRIXDB](https://matrixdb.univ-lyon1.fr/) | ELIXIR France, ELIXIR Switzerland | 🔴 down | 0.00% | 0.00% | 0.00% | 0.71% | 0.71% | 100.00% | — |
| [MediaDive](https://mediadive.dsmz.de/) | ELIXIR Germany | 🟢 up | 100.00% | 99.83% | 93.68% | 95.65% | 95.65% | 100.00% | ≤5000 ms |
| [MeltDB](https://meltdb.cebitec.uni-bielefeld.de/cgi-bin/login.cgi) | ELIXIR Germany | 🟢 up | 100.00% | 97.51% | 96.42% | 97.79% | 97.79% | 100.00% | ≤2000 ms |
| [MEM](https://biit.cs.ut.ee/mem/) | ELIXIR Estonia | 🟢 up | 100.00% | 100.00% | 99.63% | 99.64% | 99.64% | 100.00% | >10000 ms |
| [Metabolic Atlas](https://metabolicatlas.org/) | ELIXIR Sweden | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [MetaNetX](https://www.metanetx.org/) | ELIXIR Switzerland | 🟢 up | 98.81% | 99.83% | 99.70% | 98.20% | 98.20% | 100.00% | ≤5000 ms |
| [MetaPhOrs](https://orthology.phylomedb.org/) | ELIXIR Spain | 🔴 down | 0.00% | 0.00% | 68.75% | 70.53% | 70.53% | 100.00% | ≤10000 ms |
| [MGnify](https://www.ebi.ac.uk/metagenomics/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 99.96% | 99.98% | 99.98% | 100.00% | ≤1000 ms |
| [MHC Motif Atlas](http://mhcmotifatlas.org/home) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Micro-CTvlab](https://www.lifewatch.eu/microctvlab) | ELIXIR Greece | 🟢 up | 100.00% | 99.50% | 97.01% | 85.56% | 85.56% | 100.00% | >10000 ms |
| [Microbe Atlas](https://microbeatlas.org/landing) | ELIXIR Switzerland | 🟢 up | 100.00% | 99.67% | 99.85% | 99.91% | 99.91% | 100.00% | ≤5000 ms |
| [MINT](http://mint.bio.uniroma2.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 57.70% | 42.22% | 42.22% | 100.00% | ≤5000 ms |
| [MirGeneDB](https://mirgenedb.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [MitoZoa](https://rediportal.cloud.ba.infn.it/mitozoa/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [MobiDB](http://mobidb.bio.unipd.it/) | ELIXIR Italy | 🟢 up | 100.00% | 99.83% | 99.67% | 94.22% | 94.22% | 100.00% | ≤5000 ms |
| [MOLGENIS](https://molgenis.github.io/) | ELIXIR Netherlands | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [MolMeDB](https://molmedb.upol.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Nextstrain](https://nextstrain.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 97.51% | 98.74% | 97.86% | 97.86% | 100.00% | ≤1000 ms |
| [Norine](http://bioinfo.cristal.univ-lille.fr/norine/) | ELIXIR France | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [Ocean Gene Atlas](https://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/) | ELIXIR France | 🟢 up | 77.38% | 70.98% | 55.26% | 49.37% | 49.37% | 100.00% | ≤5000 ms |
| [OLIDA](https://olida.ibsquare.be/) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 99.96% | 99.93% | 99.93% | 100.00% | ≤1000 ms |
| [OMA](https://omabrowser.org/oma/home/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 99.32% | 99.32% | 100.00% | ≤1000 ms |
| [Omics Discovery Index (OmicsDI)](https://www.omicsdi.org/) | EMBL-EBI | 🟢 up | 95.24% | 90.55% | 97.67% | 97.79% | 97.79% | 100.00% | ≤2000 ms |
| [OmniPath](https://omnipathdb.org/) | ELIXIR Germany | 🟢 up | 100.00% | 99.83% | 99.89% | 99.93% | 99.93% | 100.00% | ≤1000 ms |
| [OMPdb](http://www.ompdb.org/) | ELIXIR Greece | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [OpenTargets Platform](https://platform.opentargets.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [Orphadata](https://www.orphadata.com/) | ELIXIR France | 🟢 up | 100.00% | 99.83% | 99.93% | 99.95% | 99.95% | 100.00% | ≤5000 ms |
| [Orphanet](https://www.orpha.net/) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [OrthoDB](https://www.orthodb.org) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [PanDrugs](https://www.pandrugs.org) | ELIXIR Spain | 🟢 up | 98.81% | 99.34% | 97.23% | 97.45% | 97.45% | 100.00% | ≤1000 ms |
| [ParameciumDB](https://paramecium.i2bc.paris-saclay.fr) | ELIXIR France | 🟢 up | 100.00% | 100.00% | 94.13% | 96.33% | 96.33% | 100.00% | ≤5000 ms |
| [PAXdb](https://pax-db.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 99.39% | 99.39% | 100.00% | ≤1000 ms |
| [PDBTM](https://pdbtm.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 96.79% | 97.97% | 97.97% | 100.00% | ≤5000 ms |
| [PED](https://proteinensemble.org/) | ELIXIR Italy | 🟢 up | 100.00% | 99.67% | 99.63% | 98.59% | 98.59% | 100.00% | ≤2000 ms |
| [PHI-base](http://www.phi-base.org) | ELIXIR UK | 🟢 up | 63.10% | 82.59% | 95.86% | 97.34% | 97.34% | 100.00% | ≤5000 ms |
| [PhylomeDB](https://phylomedb.org/) | ELIXIR Spain | 🔴 down | 0.00% | 0.00% | 68.78% | 70.55% | 70.55% | 100.00% | ≤5000 ms |
| [PICKLE](http://www.pickle.gr) | ELIXIR Greece | 🟢 up | 40.48% | 56.38% | 64.57% | 70.46% | 70.46% | 100.00% | >10000 ms |
| [PIPPA](https://pippa.psb.ugent.be/pippa_nav/home/) | ELIXIR Belgium | 🔴 down | 0.00% | 0.00% | 27.26% | 55.16% | 55.16% | 100.00% | ≤2000 ms |
| [PlantsDB](http://pgsb.helmholtz-muenchen.de/plant/plantsdb.jsp) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [PMDB](https://rediportal.cloud.ba.infn.it/PMDB/help.php) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [PolarProtDb](https://polarprotdb.ttk.hu/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 96.79% | 97.97% | 97.97% | 100.00% | ≤5000 ms |
| [PomBase](https://www.pombase.org/) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [Progenetix](https://progenetix.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [PROSITE](https://prosite.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 99.96% | 99.98% | 99.98% | 100.00% | ≤2000 ms |
| [Reactome](https://reactome.org/) | EMBL-EBI | 🟢 up | 100.00% | 99.83% | 99.74% | 99.75% | 99.75% | 100.00% | ≤1000 ms |
| [REDIdb](https://rediportal.cloud.ba.infn.it/redidb/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [REDIportal](https://rediportal.cloud.ba.infn.it/atlas/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤5000 ms |
| [ReMap](https://remap.univ-amu.fr/) | ELIXIR France | 🟢 up | 77.38% | 68.99% | 33.36% | 35.71% | 35.71% | 100.00% | ≤5000 ms |
| [RepeatsDB](https://repeatsdb.org/) | ELIXIR Italy | 🟢 up | 100.00% | 96.02% | 98.78% | 98.06% | 98.06% | 100.00% | ≤2000 ms |
| [REXdb](http://repeatexplorer.org/?page_id=918) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [Rfam](https://rfam.org/) | EMBL-EBI | 🟢 up | 100.00% | 100.00% | 100.00% | 99.98% | 99.98% | 100.00% | ≤2000 ms |
| [Rhea](https://www.rhea-db.org/) | ELIXIR Switzerland | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [Riboseq.org](https://riboseq.org/) | ELIXIR Ireland | 🟢 up | 100.00% | 100.00% | 99.96% | 99.98% | 99.98% | 100.00% | ≤1000 ms |
| [RNA Central](https://rnacentral.org/) | EMBL-EBI | 🟢 up | 100.00% | 98.84% | 98.19% | 98.25% | 98.25% | 100.00% | ≤2000 ms |
| [SABIO-RK](https://sabio.h-its.org/ui/search) | ELIXIR Germany | 🟢 up | 100.00% | 100.00% | 99.89% | 99.91% | 99.91% | 100.00% | ≤1000 ms |
| [SalmoBase](https://salmobase.org/) | ELIXIR Norway | 🟢 up | 100.00% | 100.00% | 99.93% | 99.95% | 99.95% | 100.00% | ≤1000 ms |
| [SARS-CoV-2 DB](https://covid19.sfb.uit.no/) | ELIXIR Norway | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [SIBiLS](https://sibils.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 99.98% | 99.98% | 100.00% | ≤2000 ms |
| [SIDER](https://sideeffects.embl.de/) | ELIXIR Germany | 🟢 up | 100.00% | 99.83% | 94.09% | 96.22% | 96.22% | 100.00% | ≤2000 ms |
| [SIGNOR](http://signor.uniroma2.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 57.67% | 73.88% | 73.88% | 100.00% | ≤2000 ms |
| [SILVA](https://www.arb-silva.de/) | ELIXIR Germany | 🟢 up | 100.00% | 99.83% | 99.82% | 99.43% | 99.43% | 100.00% | ≤2000 ms |
| [SMART](https://smart.embl.de/smart/change_mode.cgi) | ELIXIR Germany | 🟢 up | 100.00% | 99.83% | 99.89% | 99.48% | 99.48% | 100.00% | ≤2000 ms |
| [SpliceAid-F](https://rediportal.cloud.ba.infn.it/SpliceAidF/) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [sRNA Portal workflow](https://github.com/forestbiotech-lab/sRNA-Portal-workflow) | ELIXIR Portugal | 🟢 up | 100.00% | 98.84% | 99.74% | 99.84% | 99.84% | 100.00% | ≤1000 ms |
| [STAMPS](https://stamps.isas.de/) | ELIXIR Germany | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [STRING](https://string-db.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [SulfAtlas](https://sulfatlas.sb-roscoff.fr/sulfatlas/) | ELIXIR France | 🟢 up | 92.86% | 98.67% | 98.85% | 99.09% | 99.09% | 100.00% | ≤5000 ms |
| [SWICZ](http://proteom.biomed.cas.cz/) | ELIXIR Czech Republic | 🔴 down | 0.00% | 0.00% | 27.11% | 55.07% | 55.07% | 100.00% | ≤1000 ms |
| [SWISS-MODEL Repository](https://swissmodel.expasy.org/repository) | ELIXIR Switzerland | 🟢 up | 100.00% | 99.17% | 97.16% | 98.25% | 98.25% | 100.00% | ≤1000 ms |
| [SwissLipids](https://www.swisslipids.org/) | ELIXIR Switzerland | 🟢 up | 98.81% | 99.83% | 99.89% | 99.91% | 99.91% | 100.00% | ≤2000 ms |
| [SwissRegulon](https://swissregulon.unibas.ch/sr/swissregulon) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 97.30% | 98.34% | 98.34% | 100.00% | ≤2000 ms |
| [Tabloid Proteome](https://iomics.ugent.be/tabloidproteome/information.xhtml#about) | ELIXIR Belgium | 🟢 up | 100.00% | 100.00% | 93.76% | 96.04% | 96.04% | 100.00% | ≤1000 ms |
| [TFLink](https://tflink.net/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤500 ms |
| [The B6 database](https://bioinformatics.unipr.it/cgi-bin/bioinformatics/B6db/home.pl) | ELIXIR Italy | 🔴 down | 0.00% | 0.00% | 26.38% | 43.07% | 43.07% | 100.00% | ≤5000 ms |
| [TmAlphaFold](https://tmalphafold.ttk.hu/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 96.79% | 97.97% | 97.97% | 100.00% | ≤5000 ms |
| [TOPDB](https://topdb.unitmp.org) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 96.79% | 97.97% | 97.97% | 100.00% | ≤2000 ms |
| [Training Metrics Database](https://tmd.elixir-europe.org./world-map) | ELIXIR Sweden | 🟢 up | 100.00% | 100.00% | 99.96% | 99.98% | 99.98% | 100.00% | ≤1000 ms |
| [Translational Medicine Data Catalog (TMDC)](https://datacatalogue.elixir-luxembourg.org/) | ELIXIR Luxembourg | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [TSTMP](http://tstmp.enzim.ttk.mta.hu/) | ELIXIR Hungary | 🔴 down | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 100.00% | — |
| [UniCatDB](https://www.unicatdb.org/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 99.93% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [Unilectin](https://unilectin.unige.ch/) | ELIXIR Switzerland | 🟢 up | 100.00% | 48.26% | 66.97% | 73.65% | 73.65% | 100.00% | ≤1000 ms |
| [UniProtKB](https://www.uniprot.org/) | ELIXIR Switzerland, EMBL-EBI | 🟢 up | 97.62% | 99.67% | 99.93% | 99.95% | 99.95% | 100.00% | ≤2000 ms |
| [UniTmp](https://www.unitmp.org/) | ELIXIR Hungary | 🟢 up | 100.00% | 100.00% | 96.79% | 97.97% | 97.97% | 100.00% | ≤2000 ms |
| [UTRdb / UTRSite](http://utrdb.ba.itb.cnr.it/) | ELIXIR Italy | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ValidatorDB](https://webchem.ncbr.muni.cz/Platform/ValidatorDb) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [ValTrendsDB](https://valtrendsdb.biodata.ceitec.cz/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 94.31% | 96.49% | 96.49% | 100.00% | ≤1000 ms |
| [VEuPathDB](https://veupathdb.org/veupathdb/app) | ELIXIR UK | 🟢 up | 100.00% | 100.00% | 99.11% | 99.43% | 99.43% | 100.00% | ≤500 ms |
| [ViralZone](https://viralzone.expasy.org/) | ELIXIR Switzerland | 🟢 up | 100.00% | 100.00% | 100.00% | 99.98% | 99.98% | 100.00% | ≤2000 ms |
| [WatAA](https://watlas.datmos.org/wataa/) | ELIXIR Czech Republic | 🟢 up | 100.00% | 100.00% | 93.83% | 96.20% | 96.20% | 100.00% | ≤2000 ms |
| [WheatIS](https://urgi.versailles.inrae.fr/wheatis/) | ELIXIR France | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤2000 ms |
| [WikiPathways](https://www.wikipathways.org/index.php/WikiPathways) | ELIXIR Netherlands | 🟡 challenged | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | ≤1000 ms |
| [YEASTRACT](https://yeastract-plus.org/) | ELIXIR Portugal | 🟢 up | 57.14% | 91.38% | 97.71% | 98.18% | 98.18% | 100.00% | ≤2000 ms |

---

## Recent state changes

The newest entries from `events.jsonl`, the full audit trail of every state change.

| When (UTC) | Resource | Change | Detail |
|---|---|---|---|
| 2026-11-12T23:10:33Z | YEASTRACT | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T23:10:33Z | SulfAtlas | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T23:10:33Z | ReMap | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T23:10:33Z | Ocean Gene Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T23:10:33Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-11-12T22:50:37Z | SulfAtlas | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-12T22:50:37Z | ReMap | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-12T22:50:37Z | Ocean Gene Atlas | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-12T22:30:46Z | ReMap | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T22:30:46Z | Ocean Gene Atlas | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T22:30:46Z | FINDbase | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T22:10:37Z | YEASTRACT | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-12T22:10:37Z | ReMap | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-12T22:10:37Z | Ocean Gene Atlas | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-12T21:50:35Z | FINDbase | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-12T21:50:35Z | DGP | 🟡 challenged → 🟢 up | `ok` |
| 2026-11-12T21:50:35Z | CATH/Gene3D | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T21:30:44Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-11-12T21:30:44Z | CATH/Gene3D | 🟢 up → 🔴 down | `connect_timeout` |
| 2026-11-12T21:10:38Z | DGP | 🟡 challenged → 🟢 up | `ok` |
| 2026-11-12T21:08:53Z | SulfAtlas | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T20:52:33Z | DGP | 🟢 up → 🟡 challenged | `challenge:browser-check` |
| 2026-11-12T20:50:35Z | YEASTRACT | 🔴 down → 🟢 up | `ok` |
| 2026-11-12T20:50:35Z | SulfAtlas | 🟢 up → 🔴 down | `read_timeout` |
| 2026-11-12T20:30:46Z | UniProtKB | 🔴 down → 🟢 up | `ok` |

---

Generated by [uptime/scripts/summarize.py](https://github.com/gavinf97/ECD/blob/main/uptime/scripts/summarize.py) at **2026-11-12T23:52:10Z**, and rewritten after every check. Machine-readable: [summary.json](https://github.com/gavinf97/ECD/blob/uptime-data/summary.json).
