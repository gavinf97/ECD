#!/usr/bin/env python3
"""
propose_answers.py — Phase 4a of the ECD Agent Skill (deterministic proposals + evidence digest).

Maps the evidence files onto Checklist question ids and writes:

  WORKDIR/proposals.json   {qid: {choice/text/list/links/image, status, confidence, evidence, hint}}
                           — machine proposals for questions with a clear evidence rule
                             (registry presence, licences, APIs, ontologies, eligibility lists...)
  WORKDIR/digest.md        compact per-question evidence digest (the file Claude reads in Phase 4b),
                           including leads for questions that need judgement or drafting

Proposals are deliberately conservative:
  - "Yes" only with an evidence URL; "No" only when the lookup succeeded AND is conclusive
    (e.g. identifiers.org registry); website absence never yields "No" (the crawl is partial)
  - applicant-only questions get `needs_applicant` + hints
  - free-text questions needing judgement are left for Claude (listed under "Claude to draft")

Claude reviews every proposal, edits where the digest shows it is wrong, drafts the rest, then applies
with `answers.py patch`.

Usage:
    python propose_answers.py --workdir WORKDIR
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import evidence as ev, iter_questions, load_json, load_schema, now_iso, write_json  # noqa: E402

YEAR = datetime.now().year


def load(path: Path) -> dict:
    return load_json(path) if path.exists() else {}


def band_years(years: float) -> str:
    return ("Less than 1 year" if years < 1 else "1-3 years" if years < 3 else "3-5 years" if years < 5
            else "5-10 years" if years < 10 else "More than 10 years")


def snippets_for(web: dict, topic: str, n: int = 2) -> list[dict]:
    out = []
    for hit in (web.get("signals") or {}).get(topic, [])[:4]:
        for sn in hit.get("text_snippets", [])[:1]:
            out.append(ev(f"website:{topic}", hit["page"], sn))
        for ln in hit.get("links", [])[:1]:
            out.append(ev(f"website:{topic}-link", ln.split(" -> ")[-1], ln))
        if len(out) >= n:
            break
    return out[:n]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", required=True)
    args = ap.parse_args()
    wd = Path(args.workdir)
    e = wd / "evidence"
    identity = load(wd / "identity.json")
    web, repo_ev, fair = load(e / "website.json"), load(e / "repo.json"), load(e / "fairchecker.json")
    elig, epmc, tess = load(e / "eligibility.json"), load(e / "registry_europepmc.json"), load(e / "registry_tess.json")
    wfh, apic, oeb = load(e / "registry_workflowhub.json"), load(e / "registry_apicuron.json"), load(e / "registry_openebench.json")
    wb, sim, bh, summ = load(e / "registry_wayback.json"), load(e / "registry_similar.json"), load(e / "registry_biohackathon.json"), load(e / "registry_summary.json")
    m = identity.get("matches", {})
    re3 = summ.get("re3data") or {}
    bt = summ.get("biotools") or {}
    P: dict[str, dict] = {}
    leads: dict[str, list[str]] = {}

    def lead(qid: str, text: str) -> None:
        leads.setdefault(qid, []).append(text)

    # ---------------- applicant details
    repo = (repo_ev.get("repo") or {})
    if repo.get("status") == "found":
        P["APP.repo_url"] = dict(links=[repo["url"]], status="verified", confidence="high",
                                 evidence=[ev("github", repo["url"], repo.get("description"))])
    else:
        cands = [c["url"] for c in repo_ev.get("candidates", [])][:5]
        P["APP.repo_url"] = dict(status="needs_applicant", hint="No repository linked from registries/website."
                                 + (f" GitHub candidates to confirm: {', '.join(cands)}" if cands else ""))
    nodes = (elig.get("sdp_match") or {}).get("nodes") or []
    if nodes:
        P["APP.node"] = dict(text=", ".join(sorted(set(nodes))), status="inferred", confidence="medium",
                             evidence=[ev("elixir-sdp", h.get("node_page"), f"{h['service_name']} listed under {h['node']}")
                                       for h in (elig["sdp_match"].get("hits") or [])[:2]],
                             hint="Node of the SDP listing; confirm it is the submitting applicant's Node.")
    else:
        P["APP.node"] = dict(status="needs_applicant", hint=f"Affiliation hints: {list((elig.get('node_match') or {}).get('affiliation_hints', {}))[:3]}")
    insts = [i.get("institutionName") for i in re3.get("institutions") or [] if i.get("institutionName")]
    affs = [a for a, _ in epmc.get("top_affiliations") or []][:4]
    P["APP.institute"] = dict(status="needs_applicant",
                              hint=("re3data institutions: " + "; ".join(insts[:4]) if insts else "")
                              + (" | recent paper affiliations: " + "; ".join(affs) if affs else ""))
    sugg = [c["community"] for c in elig.get("community_suggestions") or []]
    if "APP.community" not in P:
        P["APP.community"] = dict(status="needs_applicant", hint=f"Suggested (keyword/link heuristic): {', '.join(sugg[:3]) or 'none'}")
    contact = ((summ.get("bioregistry") or {}).get("contact") or {})
    P["APP.submitter_name"] = dict(status="needs_applicant", hint=f"Registry contact: {contact.get('name')}" if contact.get("name") else None)
    P["APP.submitter_email"] = dict(status="needs_applicant", hint="Institutional email only.")

    # ---------------- Section 1
    sdp = elig.get("sdp_match") or {}
    if sdp.get("listed"):
        h = sdp["hits"][0]
        P["S1.2"] = dict(choice="Met", status="verified", confidence="high",
                         text=f"Listed as '{h['service_name']}' under {h['node']} on the ELIXIR SDP.",
                         evidence=[ev("elixir-sdp", h["node_page"], f"{h['service_name']} ({h.get('service_url')})")])
    else:
        P["S1.2"] = dict(status="needs_applicant", hint="Not matched in the ELIXIR Node service lists snapshot; confirm via https://elixir-europe.org/services")
    holds = elig.get("holds_existing_status") or []
    status_ev = [ev("elixir-status-list", v.get("source_url"), f"{v['label']}: {'MATCH ' + str([x['name'] for x in v['hits']]) if v['matched'] else 'no match'}")
                 for v in (elig.get("status_match") or {}).values()]
    if holds:
        P["S1.4"] = dict(choice="Not met", status="verified", confidence="high", text=f"Resource already holds: {', '.join(holds)}.",
                         evidence=[x for x in status_ev if "MATCH" in (x.get("snippet") or "")])
    elif elig:
        P["S1.4"] = dict(choice="Met", status="verified", confidence="medium" if elig.get("reference_lists_stale") else "high",
                         text="Not found in the current CDR, EDD, RIR or GCBR lists.", evidence=status_ev)
    if nodes and (elig.get("node_match") or {}).get("affiliation_hints"):
        P["S1.1"] = dict(status="needs_applicant", hint=f"Resource is on the {', '.join(nodes)} SDP; confirm the primary applicant belongs to that Node and a Node institute.")
    else:
        P["S1.1"] = dict(status="needs_applicant", hint="Only the applicant can confirm Node membership.")
    lead("S1.3", "Type signals: " + " | ".join(elig.get("resource_type_signals") or []))
    fed = elig.get("federation_signals") or {}
    lead("S1.5", f"re3data institutions: {fed.get('re3data_institution_count')} in {fed.get('institution_countries')}")
    P["S1.confirm"] = dict(status="needs_applicant",
                           hint="Pre-check blocks eligibility: " + "; ".join(holds) if holds else "Applicant must confirm after reviewing S1.1-S1.5.")

    # ---------------- Section 2
    dbp = epmc.get("database_papers") or []
    if dbp:
        P["S2.1e"] = dict(choice="Yes", links=[p["url"] for p in sorted(dbp, key=lambda p: -(p["year"] or 0))[:3]], status="verified",
                          confidence="high", evidence=[ev("europepmc", p["url"], f"{p['title']} — {p['journal']} {p['year']}") for p in dbp[:4]])
    elif epmc.get("status") == "not_found":
        P["S2.1e"] = dict(status="needs_applicant", hint="No database paper found in Europe PMC by title/DOI; ask the applicant for any database article.")
    years = [y for y in (epmc.get("first_paper_year"), wb.get("first_capture_year"),
                         int(str(re3.get("start_date"))[:4]) if str(re3.get("start_date") or "")[:4].isdigit() else None) if y]
    if years:
        first = min(years)
        P["S2.2"] = dict(choice=band_years(YEAR - first), status="inferred", confidence="medium",
                         evidence=[x for x in (
                             ev("europepmc", None, f"earliest paper about resource: {epmc.get('first_paper_year')}") if epmc.get("first_paper_year") else None,
                             ev("wayback", wb.get("url"), f"first archived capture {wb.get('first_capture')}") if wb.get("first_capture") else None,
                             ev("re3data", re3.get("url"), f"startDate {re3.get('start_date')}") if re3.get("start_date") else None) if x],
                         hint=f"Earliest public trace {first}; confirm the official go-live year.")
    bh_items = [i for i in bh.get("github_elixir_org_mentions") or [] if i.get("is_biohackathon_repo")]
    if bh_items or bh.get("biohackathon_reports"):
        lead("S2.3c", "Leads: " + "; ".join([f"{i['title']} ({i['url']})" for i in bh_items[:3]] +
                                            [f"{r['title']} ({r['url']})" for r in (bh.get("biohackathon_reports") or [])[:3]]))
    for q in ("S2.3a", "S2.3b"):
        P[q] = dict(status="needs_applicant", hint="ELIXIR commissioned-service participation is not systematically public; ask the applicant.")
    P["S2.3c"] = dict(status="needs_applicant", hint=(leads.get("S2.3c") or ["No public BioHackathon/AHM trace found."])[0])
    P["S2.5"] = dict(status="needs_applicant")
    P["S2.6"] = dict(status="needs_applicant")
    lead("S2.1c", "Candidate overlapping resources (judge genuinely overlapping ones only): "
         + ", ".join(f"{c['name']} [{'; '.join(sorted(set(c['shared_topics'])))[:60]}]" for c in (sim.get("candidates") or [])[:10]))
    lead("S2.1a", f"Descriptions — re3data: {(re3.get('description') or '')[:300]} | bioregistry: {((summ.get('bioregistry') or {}).get('description') or '')[:200]}")
    stats = (web.get("signals") or {}).get("statistics", [])
    lead("S2.1b", "Statistics snippets: " + " || ".join(sn for h in stats[:3] for sn in h.get("text_snippets", [])[:1])[:700]
         + f" | re3data content types: {re3.get('content_types')}")
    lead("S2.1d", f"Community suggestions: {sugg[:3]}; bio.tools topics: {bt.get('topics')}")
    lead("S3.3", f"Citations of resource papers: {epmc.get('total_citations_of_resource_papers')}; domain mentions by year: {epmc.get('domain_mentions_by_year')}")

    # ---------------- Section 3
    mon_ev = []
    if oeb.get("status") == "found":
        lm = oeb.get("last_month") or {}
        mon_ev.append(ev("openebench", oeb.get("observatory_url"), f"OpenEBench monitor: last month uptime {lm.get('uptime_days')} d, "
                         f"downtime {lm.get('downtime_days')} d, avg access {lm.get('average_access_time')} ms"))
    mon_ev += snippets_for(web, "monitoring", 2)
    if mon_ev:
        P["S3.1"] = dict(choice="Yes", status="inferred", confidence="low", evidence=mon_ev,
                         text="Uptime and response time are tracked by the OpenEBench monitoring service." if oeb.get("status") == "found" else None,
                         hint="External monitoring (OpenEBench) found; confirm whether the team runs its own uptime/response-time monitoring.")
    else:
        P["S3.1"] = dict(status="needs_applicant")
    if web.get("analytics_detected"):
        P["S3.2"] = dict(choice="Yes", status="inferred", confidence="medium",
                         text=f"Web usage analytics are collected ({', '.join(web['analytics_detected'])}).",
                         evidence=[ev("website:analytics", web.get("start_url"), f"analytics tags detected: {web['analytics_detected']}")],
                         hint="Analytics tags detected; confirm which usage metrics are tracked (do not report numbers).")
    else:
        P["S3.2"] = dict(status="needs_applicant")

    # ---------------- Section 4
    for qid, topic, conf in (("S4.3", "helpdesk", "high"), ("S4.9", "sab", "medium"), ("S4.10", "privacy", "high"), ("S4.11", "ethics", "low")):
        evs = snippets_for(web, topic, 3)
        strong = {"S4.3": r"help ?desk|support|contact|mailto|faq", "S4.9": r"scientific advisory board|advisory board",
                  "S4.10": r"privacy (notice|policy|statement)|data protection", "S4.11": r"ethic"}[qid]
        good = [x for x in evs if re.search(strong, (x.get("snippet") or "") + (x.get("url") or ""), re.I)]
        if good:
            P[qid] = dict(choice="Yes", links=[good[0]["url"]], status="inferred" if qid == "S4.11" else "verified",
                          confidence=conf, evidence=good)
        else:
            P[qid] = dict(status="needs_applicant", hint=f"No '{topic}' evidence found in the crawled pages (crawl is partial).")
    team = snippets_for(web, "team", 3)
    team_pages = [p["url"] for p in web.get("pages", []) if re.search(r"/(team|people|staff|about|who)", p["url"])]
    lead("S4.4", f"Team-like pages crawled: {team_pages}; snippets: " + " || ".join((x.get('snippet') or '')[:160] for x in team))
    if repo.get("status") == "found":
        lead("S4.1", f"Repo releases: {[r['tag'] for r in repo.get('releases', [])[:5]]}; milestones: {len(repo.get('milestones') or [])}")
        lead("S4.2", f"Issue tracker: has_issues={repo.get('has_issues')}, closed issues={repo.get('closed_issues_total')}")
        lead("S4.5", f"Hint only: {repo.get('active_committers_last_12_months')} active committers in last 12 months; {repo.get('contributors_total')} contributors")
        lead("S4.8", f"Hint only: top contributor share {repo.get('top_contributor_share')}, recent commit concentration {repo.get('recent_commit_concentration')}")
    lead("S4.1", "Roadmap/news snippets: " + " || ".join((x.get("snippet") or "")[:160] for x in snippets_for(web, "roadmap", 3)))
    lead("S4.2", "Feedback snippets: " + " || ".join((x.get("snippet") or "")[:160] for x in snippets_for(web, "feedback", 3))
         + f" | robots.txt excerpt: {(web.get('robots_txt_excerpt') or '')[:200]}")
    lead("S4.6", f"re3data institutions: {insts[:6]}")
    grants = epmc.get("grant_agencies") or []
    for qid in ("S4.5", "S4.7a", "S4.7b", "S4.8"):
        P[qid] = dict(status="needs_applicant", hint="; ".join(leads.get(qid, [])) or None)
    if grants:
        P["S4.7a"]["hint"] = f"Funders acknowledged in resource papers (not proof of current dedicated funding): {grants[:6]}"
    fund = snippets_for(web, "funding", 2)
    if fund:
        P["S4.7a"]["hint"] = (P["S4.7a"].get("hint") or "") + " | website: " + (fund[0].get("snippet") or "")[:200]

    # ---------------- Section 5
    ms = re3.get("metadata_standards") or []
    jsonld = [j for block in web.get("jsonld", []) for j in block.get("summary", [])] + ((web.get("entry_page") or {}).get("jsonld") or [])
    s51_ev = [ev("re3data:metadataStandard", x.get("metadataStandardURL") or re3.get("url"), x.get("metadataStandardName")) for x in ms]
    if jsonld:
        s51_ev.append(ev("website:json-ld", (web.get("entry_page") or {}).get("entry_url") or web.get("start_url"),
                         f"schema.org/Bioschemas JSON-LD types: {sorted({str(j.get('@type')) for j in jsonld})}"))
    if s51_ev:
        P["S5.1"] = dict(choice="Yes", status="inferred", confidence="medium", evidence=s51_ev,
                         hint="Name the actual standards (e.g. Bioschemas profile, MIAPE) and add FAIRsharing standard links.")
    onts = [o for o in web.get("ontology_prefixes") or [] if o.get("in_ols")]
    if onts:
        P["S5.2"] = dict(choice="Yes", status="verified", confidence="high",
                         links=[o["ols_url"] for o in onts[:5]],
                         text="Uses " + ", ".join(f"{o['title']} ({o['prefix']})" for o in onts[:5]) + " for annotations.",
                         evidence=[ev("website:curie", (web.get("entry_page") or {}).get("entry_url") or web.get("start_url"),
                                      f"{o['prefix']} terms found {o['occurrences']}x; in OLS: {o['title']}") for o in onts[:5]])
    other_prefixes = [o["prefix"] for o in web.get("ontology_prefixes") or [] if not o.get("in_ols")]
    if other_prefixes:
        lead("S5.2", f"Ontology prefixes used but not in OLS4 (check OBO Foundry/BioPortal): {other_prefixes}")
    if jsonld:
        P["S5.3"] = dict(choice="Yes", status="verified", confidence="high",
                         links=[(web.get("entry_page") or {}).get("entry_url") or web.get("start_url")],
                         text=f"Pages embed schema.org/Bioschemas JSON-LD ({', '.join(sorted({str(j.get('@type')) for j in jsonld})[:4])}).",
                         evidence=s51_ev[-1:])
    api_items, api_ev = [], []
    for ep in web.get("api_endpoints") or []:
        api_items.append(f"REST API: {ep['url']}")
        api_ev.append(ev("website:api-endpoint", ep["url"], f"{ep['content_type']}: {ep['excerpt'][:120]}"))
    for a in re3.get("apis") or []:
        api_items.append(f"{a.get('type')}: {a.get('url')}")
        api_ev.append(ev("re3data:api", a.get("url") or re3.get("url"), f"re3data API type {a.get('type')}"))
    for x in snippets_for(web, "api", 2) + snippets_for(web, "download", 1):
        api_ev.append(x)
    if "Web API" in (bt.get("tool_types") or []):
        api_ev.append(ev("bio.tools", bt.get("url"), "bio.tools toolType includes 'Web API'"))
        if not api_items:
            api_items.append(f"Web API (registered in bio.tools: {bt.get('url')})")
    if api_items or any("Web API" in (x.get("snippet") or "") for x in api_ev):
        P["S5.4"] = dict(choice="Yes", list=list(dict.fromkeys(api_items))[:6], status="verified", confidence="high", evidence=api_ev[:6],
                         hint="Add download/FTP and documentation links if available.")
    uni = m.get("uniprot_xref") or {}
    out_items, out_ev = [], []
    if uni.get("status") == "found":
        out_items.append(f"UniProtKB cross-references ({uni.get('id')})")
        out_ev.append(ev("uniprot", uni.get("url"), f"{uni.get('name')} is a UniProt cross-referenced database ({uni.get('category')})"))
    for pre in ((summ.get("bioregistry") or {}).get("appears_in") or [])[:5]:
        out_items.append(f"Referenced by {pre}")
        out_ev.append(ev("bioregistry:appears_in", f"https://bioregistry.io/{pre}", f"prefix used in {pre}"))
    if out_items:
        P["S5.6"] = dict(choice="Yes", list=out_items, status="verified", confidence="high", evidence=out_ev,
                         hint="Add other known consumers (e.g. InterPro, MobiDB) if the applicant knows them.")
    if (summ.get("bioregistry") or {}).get("depends_on"):
        lead("S5.5", f"Bioregistry depends_on: {summ['bioregistry']['depends_on']}")
    P["S5.7"] = dict(status="needs_applicant")

    # ---------------- Section 6
    lic_ev = snippets_for(web, "license", 3)
    for dl in re3.get("database_licenses") or []:
        lic_ev.append(ev("re3data:databaseLicense", dl.get("databaseLicenseURL") or re3.get("url"), dl.get("databaseLicenseName")))
    if lic_ev:
        lead("S6.2", "Licence evidence: " + " || ".join(f"{x['source']}: {(x.get('snippet') or '')[:160]}" for x in lic_ev))
        P["S6.2"] = dict(status="pending", evidence=lic_ev, hint="Claude: state the exact data licence named on the website (prefer the site over registries).")
    else:
        P["S6.2"] = dict(status="needs_applicant")
    ver = snippets_for(web, "versions", 2) + snippets_for(web, "roadmap", 1)
    if re3.get("versioning") == "yes":
        ver.append(ev("re3data:versioning", re3.get("url"), "versioning: yes"))
    if ver:
        P["S6.4"] = dict(choice="Yes", status="inferred", confidence="medium", evidence=ver,
                         hint="Describe release cadence and where previous releases are archived.")
    P["S6.3"] = dict(status="needs_applicant")
    if repo.get("status") == "found":
        P["S6.6"] = dict(text=f"{repo.get('license_name') or repo.get('license_spdx') or 'No licence file detected'} (repository licence).",
                         links=[repo["url"]], status="verified" if repo.get("license_spdx") else "inferred", confidence="high",
                         evidence=[ev("github:license", repo["url"], f"SPDX {repo.get('license_spdx')}")])
        P["S6.8"] = dict(choice="Yes" if repo.get("open_source") else "No", links=[repo["url"]], status="verified", confidence="high",
                         evidence=[ev("github", repo["url"], f"public={not repo.get('private')}, licence={repo.get('license_spdx')}, OSI={repo.get('osi_license')}")])
        if repo.get("container_files") or repo.get("ghcr_packages"):
            P["S6.7"] = dict(choice="Yes", links=[repo["url"]], status="verified", confidence="medium",
                             evidence=[ev("github:containers", repo["url"], f"files {repo.get('container_files')}, ghcr {repo.get('ghcr_packages')}")])
        if repo.get("smp_related_files"):
            lead("S6.5", f"Repo governance files (not an SMP by themselves): {repo['smp_related_files']}")
    else:
        for qid in ("S6.6", "S6.7", "S6.8"):
            P[qid] = dict(status="needs_applicant", hint="No confirmed code repository.")
    reg = repo_ev.get("container_registries") or {}
    hub = [x for x in (reg.get("dockerhub") or []) if isinstance(x, dict)] + [x for x in (reg.get("quay") or []) if isinstance(x, dict)]
    if hub:
        lead("S6.7", f"Container registry name matches (verify ownership): {[x['url'] for x in hub[:4]]}")

    # ---------------- Section 7
    fs = m.get("fairsharing") or {}
    if fs.get("status") == "found":
        P["S7.1"] = dict(choice="Yes", links=[fs["url"]] + ([m["re3data"]["url"]] if (m.get("re3data") or {}).get("status") == "found" else []),
                         status="verified", confidence="high", evidence=[ev("fairsharing", fs["url"], f"FAIRsharing record {fs['id']} (via {fs.get('match_basis')})")])
    elif (m.get("re3data") or {}).get("status") == "found":
        P["S7.1"] = dict(choice="Yes", links=[m["re3data"]["url"]], status="verified", confidence="medium",
                         evidence=[ev("re3data", m["re3data"]["url"], "listed in re3data")], hint="Not found in FAIRsharing via Bioregistry; check FAIRsharing directly.")
    else:
        P["S7.1"] = dict(status="needs_applicant", hint=fs.get("note") or "Not found via Bioregistry/re3data; search FAIRsharing.")
    ido = m.get("identifiers_org") or {}
    if ido.get("status") == "found":
        P["S7.2"] = dict(choice="Yes", links=[ido["url"]], status="verified", confidence="high",
                         evidence=[ev("identifiers.org", ido["url"], f"prefix {ido['id']} ({ido.get('mir_id')})")])
    elif ido.get("status") == "not_found":
        P["S7.2"] = dict(choice="No", status="not_found", confidence="medium",
                         evidence=[ev("identifiers.org", "https://registry.identifiers.org/registry", f"no namespace matched; tried {ido.get('tried_prefixes')}")])
    s73_links, s73_ev = [], []
    if (m.get("biotools") or {}).get("status") == "found":
        s73_links.append(m["biotools"]["url"])
        s73_ev.append(ev("bio.tools", m["biotools"]["url"], f"bio.tools entry {m['biotools']['id']} ({bt.get('tool_types')})"))
    for w in [x for x in wfh.get("items") or [] if x.get("mentions_name_in_title")][:3]:
        s73_links.append(w["url"])
        s73_ev.append(ev("workflowhub", w["url"], w["title"]))
    if s73_links:
        P["S7.3"] = dict(choice="Yes", links=s73_links, status="verified", confidence="medium", evidence=s73_ev,
                         hint="bio.tools entry found; add any separate tools/workflows the resource provides.")
    t_items = [i for k in ("materials", "events") for i in (tess.get(k) or {}).get("items", []) if i.get("mentions_name_in_title") or i.get("mentions_name")]
    if t_items:
        P["S7.4"] = dict(choice="Yes", links=[i["url"] for i in t_items[:3]], status="verified", confidence="high",
                         evidence=[ev("tess", i["url"], i["title"]) for i in t_items[:4]])
    elif tess.get("status") == "not_found":
        P["S7.4"] = dict(choice="No", status="not_found", confidence="medium",
                         evidence=[ev("tess", f"https://tess.elixir-europe.org/materials?q={identity['input']['name']}", "no TeSS materials/events mention the resource")])
    apicuron_links = (web.get("registry_links") or {}).get("apicuron.org", [])
    if apic.get("status") == "found":
        P["S7.5"] = dict(choice="Yes", links=[apic["url"]], status="verified", confidence="high", evidence=[ev("apicuron", apic["url"], "APICURON partner resource")])
    elif apicuron_links:
        P["S7.5"] = dict(choice="Yes", links=apicuron_links[:1], status="inferred", confidence="medium",
                         evidence=[ev("website:apicuron-link", apicuron_links[0], "resource website links to APICURON")],
                         hint="Website links to APICURON; confirm curator credit is actually submitted and add the APICURON resource page link.")
    else:
        P["S7.5"] = dict(status="needs_applicant", hint="APICURON resource list API unavailable and no APICURON link on the website.")
    ls = web.get("lsaai_evidence") or []
    if ls:
        P["S7.6"] = dict(choice="Yes", status="inferred", confidence="medium",
                         evidence=[ev("website:ls-aai", x.get("page"), str(x.get("link") or x.get("text_snippets"))[:200]) for x in ls[:2]])
    else:
        login = [ln for h in (web.get("signals") or {}).get("aai", []) for ln in h.get("links", [])]
        P["S7.6"] = dict(status="needs_applicant",
                         hint=f"No LS Login detected. Login-related links: {login[:3]}" if login else "No login/AAI detected (Not applicable if no authentication).")
    if oeb.get("status") == "found":
        P["S7.7"] = dict(choice="Yes", links=[oeb["observatory_url"]], status="inferred", confidence="medium",
                         evidence=[ev("openebench", oeb.get("metrics_url"), f"last check {oeb.get('last_check')}")],
                         hint="Resource is monitored in OpenEBench (auto-imported from bio.tools); confirm the team uses it.")
    shot = fair.get("screenshot") or {}
    png = shot.get("png")
    scores = [r.get("score") or 0 for r in fair.get("metric_scores") or []]
    site_down = web.get("status") == "query_failed" or (identity.get("homepage") or {}).get("status") == "query_failed"
    degenerate = bool(scores) and sum(scores) <= 2
    if shot.get("status") == "ok" and png and Path(png).exists() and (site_down or degenerate):
        P["S7.8"] = dict(status="needs_applicant",
                         hint=(f"FAIR-Checker ran but {'the website was unreachable' if site_down else 'almost every metric failed'} "
                               f"(scores {scores}); re-run fair_check.py when the site is up before using the screenshot. "
                               f"Screenshot: {png}"))
    elif shot.get("status") == "ok" and png and Path(png).exists():
        P["S7.8"] = dict(image=png, links=[fair["assessment_url"]] if fair.get("assessment_url") else [], status="inferred", confidence="high",
                         evidence=[ev("fair-checker", fair.get("assessment_url") or fair.get("fair_checker_url"),
                                      "scores: " + ", ".join(f"{r['metric']}={r['score']}" for r in fair.get("metric_scores") or []))],
                         hint="Claude must view the PNG to confirm it shows completed results before marking verified.")
    else:
        P["S7.8"] = dict(status="needs_applicant", hint=fair.get("manual_instructions"))
    for qid, topic in (("S7.9", "rdmkit"), ("S7.10", "rsqkit")):
        hits = snippets_for(web, topic, 1)
        P[qid] = dict(status="needs_applicant", hint=f"Website mentions {topic}: {hits[0]['url']}" if hits else None)
    P["S8.declaration"] = dict(status="needs_applicant")

    for qid, rec in P.items():
        rec.setdefault("evidence", [])
        rec["_proposed_by"] = "propose_answers.py"
    write_json(wd / "proposals.json", P)

    # ---------------- digest
    schema = load_schema()
    lines = [f"# ECD evidence digest — {identity['input']['name']}", "",
             f"Generated {now_iso()} · homepage {identity['homepage'].get('final_url')} · website render mode: {web.get('render_mode')}",
             f"Registry matches: " + ", ".join(f"{k}={v.get('status')}:{v.get('id') or (v.get('best') or {}).get('id')}" for k, v in m.items()),
             f"Needs confirmation: {identity.get('needs_confirmation')}", ""]
    if web.get("status") == "query_failed" or (identity.get("homepage") or {}).get("status") == "query_failed":
        lines.insert(2, f"**WARNING — website unreachable during assessment** ({web.get('error') or identity['homepage'].get('error')}). "
                        "Website-based answers are missing: re-run `probe_website.py` + `propose_answers.py` later, or use WebFetch; "
                        "check the FAIR-Checker screenshot shows real results; mention the outage in the report (ECD health check targets 99% uptime).\n")
    to_draft = []
    for section, q in iter_questions(schema):
        if section.get("conditional_on") == "reapplication":
            continue
        prop = P.get(q["id"])
        qleads = leads.get(q["id"], [])
        if q.get("automation") in ("input", "derived"):
            continue  # set by `answers.py init`
        if not prop and not qleads:
            to_draft.append(q["id"])
        lines.append(f"## {q['id']} — {q['prompt'][:110]}")
        if prop:
            shown = {k: v for k, v in prop.items() if k in ("choice", "text", "list", "links", "image") and v}
            lines.append(f"- PROPOSAL [{prop.get('status')}/{prop.get('confidence')}]: {shown}")
            for x in prop.get("evidence", [])[:3]:
                lines.append(f"  - {x['source']}: {x.get('url')} — {(x.get('snippet') or '')[:180]}")
            if prop.get("hint"):
                lines.append(f"  - hint: {prop['hint'][:300]}")
        for l in qleads:
            lines.append(f"- LEAD: {l[:600]}")
        if not prop or prop.get("status") == "pending":
            lines.append("- CLAUDE: decide/draft from leads + evidence files")
        lines.append("")
    lines.insert(5, f"Claude to draft (no proposal or lead): {', '.join(to_draft)}\n")
    (wd / "digest.md").write_text("\n".join(lines), encoding="utf-8")
    print({"proposals": len(P), "digest": str(wd / "digest.md"), "no_lead": to_draft})


if __name__ == "__main__":
    main()
