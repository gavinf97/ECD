#!/usr/bin/env python3
"""
query_registries.py — Phase 3 (registry evidence) of the ECD Agent Skill.

Reads identity.json (from resolve_resource.py) and gathers evidence for the
Checklist questions that registries can answer. Each subcommand writes one
JSON file under WORKDIR/evidence/ and prints a compact summary line.

Subcommands (or `all`):
  europepmc     database papers (S2.1e), first paper year (S2.2), citation trend (S3.3),
                grants (S4.7 hint), author affiliations (APP.institute / S4.6)
  tess          TeSS training materials + events mentioning the resource (S7.4)
  workflowhub   WorkflowHub workflows mentioning the resource (S7.3)
  apicuron      APICURON partner resource check (S7.5)
  openebench    OpenEBench monitor metrics: uptime days, https, licence, bioschemas (S3.1, S7.7)
  wayback       first Internet Archive capture of the homepage (S2.2)
  similar       overlapping resources via bio.tools EDAM topics + re3data subjects (S2.1c)
  biohackathon  elixir-europe GitHub mentions + BioHackathon/BioHackrXiv reports (S2.3c, hints S2.3a/b)
  summary       condensed view of identity.json registry records (S1.3, S5, S6, S7.1-7.3)

Usage:
    python query_registries.py all --identity WORKDIR/identity.json --evidence-dir WORKDIR/evidence
    python query_registries.py tess --identity WORKDIR/identity.json --evidence-dir WORKDIR/evidence
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (domain_of, get_json, http_get, load_json, log, norm_name, now_iso,  # noqa: E402
                    result, same_site, write_json)

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
DATABASE_JOURNALS = ("nucleic acids res", "database (oxford)", "database", "bioinformatics", "sci data",
                     "scientific data", "plos comput biol", "brief bioinform", "gigascience", "genome res",
                     "nar genom bioinform", "protein sci", "j mol biol", "bmc bioinformatics")


def first(v, default=None):
    if isinstance(v, list):
        v = v[0] if v else default
    if isinstance(v, dict) and "value" in v:
        return v["value"]
    return v if v not in (None, "") else default


# ------------------------------------------------------------------ Europe PMC
def q_europepmc(identity: dict) -> dict:
    name = identity["input"]["name"]
    domain = domain_of(identity["homepage"].get("final_url") or identity["input"]["url"])
    dois = set()
    br = identity["matches"]["bioregistry"]
    if br.get("status") == "found":
        dois |= {p.get("doi", "").lower() for p in br["best"].get("publications") or [] if p.get("doi")}
    bt = identity["matches"]["biotools"]
    if bt.get("status") == "found":
        dois |= {(p.get("doi") or "").lower() for p in bt["record"].get("publication", []) if p.get("doi")}
    dois.discard("")

    queries = {
        "title_name": f'TITLE:"{name}"',
        "domain_mention": f'"{domain}"',
    }
    if dois:
        queries["registry_dois"] = " OR ".join(f'DOI:"{d}"' for d in sorted(dois)[:15])
    papers: dict[str, dict] = {}
    errors = []
    for label, query in queries.items():
        data, err = get_json(EPMC, params={"query": query, "format": "json", "resultType": "core",
                                           "pageSize": 100, "sort": "P_PDATE_D desc"}, timeout=40)
        if err:
            errors.append(f"{label}: {err}")
            continue
        for r in data.get("resultList", {}).get("result", []):
            key = r.get("doi") or r.get("id")
            rec = papers.setdefault(key, {
                "title": r.get("title"), "doi": r.get("doi"), "pmid": r.get("pmid"), "pmcid": r.get("pmcid"),
                "year": int(r["pubYear"]) if r.get("pubYear", "").isdigit() else None,
                "journal": ((r.get("journalInfo") or {}).get("journal") or {}).get("title") or r.get("bookOrReportDetails", {}).get("publisher"),
                "cited_by": r.get("citedByCount", 0), "is_open_access": r.get("isOpenAccess"),
                "url": f"https://doi.org/{r['doi']}" if r.get("doi") else f"https://europepmc.org/article/{r.get('source')}/{r.get('id')}",
                "grants": [{"agency": g.get("agency"), "id": g.get("grantId")} for g in (r.get("grantsList") or {}).get("grant", [])],
                "affiliations": sorted({a.get("affiliation") for au in (r.get("authorList") or {}).get("author", [])
                                        for a in ((au.get("authorAffiliationDetailsList") or {}).get("authorAffiliation") or [])
                                        if a.get("affiliation")})[:25],
                "abstract_excerpt": (r.get("abstractText") or "")[:600],
                "matched_by": [],
            })
            rec["matched_by"].append(label)

    def is_db_paper(p: dict) -> bool:
        title_hit = norm_name(name) in norm_name(p["title"] or "")
        doi_hit = (p.get("doi") or "").lower() in dois
        journal = (p.get("journal") or "").lower()
        return (title_hit or doi_hit) and any(journal.startswith(j) for j in DATABASE_JOURNALS)

    ranked = sorted(papers.values(), key=lambda p: (is_db_paper(p), p["cited_by"] or 0), reverse=True)
    db_papers = [p for p in ranked if is_db_paper(p)]
    about = [p for p in ranked if norm_name(name) in norm_name(p["title"] or "") or (p.get("doi") or "").lower() in dois]
    years = [p["year"] for p in about if p["year"]]
    mention_years = Counter(p["year"] for p in papers.values() if "domain_mention" in p["matched_by"] and p["year"])
    grants = Counter((g["agency"] or "").strip() for p in about for g in p["grants"] if g["agency"])
    recent_db = sorted(db_papers, key=lambda p: p["year"] or 0, reverse=True)[:3]
    affiliations = Counter(a for p in recent_db for a in p["affiliations"])
    status = "found" if about else ("query_failed" if errors and not papers else "not_found")
    return result(status, queries=queries, errors=errors or None,
                  database_papers=db_papers[:10], papers_about_resource=about[:25],
                  first_paper_year=min(years) if years else None,
                  total_citations_of_resource_papers=sum(p["cited_by"] or 0 for p in about),
                  domain_mentions_by_year=dict(sorted(mention_years.items())),
                  grant_agencies=grants.most_common(15),
                  top_affiliations=affiliations.most_common(15))


# ------------------------------------------------------------------ TeSS
def q_tess(identity: dict) -> dict:
    name = identity["input"]["name"]
    out = {}
    for kind in ("materials", "events"):
        data, err = get_json(f"https://tess.elixir-europe.org/{kind}.json_api", params={"q": name},
                             headers={"Accept": "application/vnd.api+json"}, timeout=40)
        if err:
            out[kind] = result("query_failed", error=err)
            continue
        items = []
        for x in data.get("data", []):
            attrs = x.get("attributes", {})
            text = " ".join(str(attrs.get(k) or "") for k in ("title", "description", "keywords"))
            items.append({"title": attrs.get("title"), "url": "https://tess.elixir-europe.org" + x["links"]["self"],
                          "mentions_name_in_title": norm_name(name) in norm_name(attrs.get("title") or ""),
                          "mentions_name": norm_name(name) in norm_name(text)})
        facet = (data.get("meta", {}).get("available-facets", {}) or {}).get("standard-database-or-policy", [])
        out[kind] = result("found" if items else "not_found", count=data.get("meta", {}).get("results-count"),
                           search_url=f"https://tess.elixir-europe.org/{kind}?q={name}", items=items[:20],
                           tagged_as_database=[f for f in facet if norm_name(f.get("value")) == norm_name(name)],
                           nodes=(data.get("meta", {}).get("available-facets", {}) or {}).get("node"))
    status = "found" if any(v.get("status") == "found" for v in out.values()) else \
        ("query_failed" if all(v.get("status") == "query_failed" for v in out.values()) else "not_found")
    return result(status, **out)


# ------------------------------------------------------------------ WorkflowHub
def q_workflowhub(identity: dict) -> dict:
    name = identity["input"]["name"]
    data, err = get_json("https://workflowhub.eu/workflows", params={"filter[query]": name},
                         headers={"Accept": "application/vnd.api+json"}, timeout=40)
    if err:
        return result("query_failed", error=err)
    items = [{"title": x["attributes"].get("title"), "url": f"https://workflowhub.eu/workflows/{x['id']}",
              "mentions_name_in_title": norm_name(name) in norm_name(x["attributes"].get("title") or "")}
             for x in data.get("data", [])]
    return result("found" if items else "not_found", search_url=f"https://workflowhub.eu/search?q={name}", items=items[:20])


# ------------------------------------------------------------------ APICURON
def q_apicuron(identity: dict) -> dict:
    """APICURON's documented /api/partner-resources returns 404 publicly (checked 2026-09-17).
    Try it anyway; on failure report query_failed so the answer falls back to the website scan
    (probe_website.py records links to apicuron.org) or to the applicant."""
    name, url = identity["input"]["name"], identity["input"]["url"]
    for endpoint in ("https://apicuron.org/api/partner-resources", "https://apicuron.org/api/resources"):
        data, err = get_json(endpoint, timeout=30)
        if err or not isinstance(data, (list, dict)) or (isinstance(data, dict) and data.get("statusCode") == 404):
            continue
        rows = data if isinstance(data, list) else data.get("data") or data.get("resources") or []
        for row in rows:
            if norm_name(row.get("resource_name") or row.get("name")) == norm_name(name) or \
                    same_site(row.get("resource_url") or row.get("url") or "", url):
                rid = row.get("resource_id") or row.get("id")
                return result("found", id=rid, url=f"https://apicuron.org/resources/{rid}", record=row)
        return result("not_found", endpoint=endpoint, checked=len(rows))
    return result("query_failed", error="APICURON public resource list endpoint unavailable",
                  fallback="Check probe_website.py 'apicuron' keyword hits; otherwise ask the applicant.",
                  browse_url="https://apicuron.org/resources")


# ------------------------------------------------------------------ OpenEBench
def q_openebench(identity: dict) -> dict:
    oeb = identity["matches"].get("openebench", {})
    if oeb.get("status") != "found":
        return result(oeb.get("status", "not_found"), note="Resource not found in OpenEBench monitor search")
    data, err = get_json(oeb["metrics_url"], timeout=40)
    if err:
        return result("query_failed", error=err, tool_url=oeb.get("url"))
    web = (data.get("project") or {}).get("website") or {}
    return result("found", tool_url=oeb.get("url"), metrics_url=oeb["metrics_url"],
                  observatory_url=f"https://openebench.bsc.es/observatory/Tool/{oeb['id']}",
                  last_check=web.get("last_check"), operational_http=web.get("operational"),
                  https=web.get("https"), ssl=web.get("ssl"), bioschemas=web.get("bioschemas"),
                  license_detected=web.get("license"), copyright_detected=web.get("copyright"),
                  last_month=web.get("last_month_access"), half_year=web.get("half_year_stat"),
                  note=("OpenEBench monitors bio.tools entries automatically; presence here shows the resource IS "
                        "monitored, not that the provider actively uses OpenEBench. Confirm with the applicant."))


# ------------------------------------------------------------------ Wayback
def q_wayback(identity: dict) -> dict:
    url = identity["homepage"].get("final_url") or identity["input"]["url"]
    domain = domain_of(url)
    data, err = get_json("https://web.archive.org/cdx/search/cdx",
                         params={"url": domain, "limit": 1, "output": "json", "fl": "timestamp,original"}, timeout=60)
    if data and len(data) > 1:
        ts = data[1][0]
        return result("found", first_capture=ts, first_capture_year=int(ts[:4]),
                      url=f"https://web.archive.org/web/{ts}/{data[1][1]}", method="cdx")
    # CDX is intermittently offline; the availability API returns the capture closest to a timestamp.
    avail, err2 = get_json("https://archive.org/wayback/available", params={"url": domain, "timestamp": "19950101"}, timeout=60)
    snap = ((avail or {}).get("archived_snapshots") or {}).get("closest")
    if snap:
        ts = snap["timestamp"]
        return result("found", first_capture=ts, first_capture_year=int(ts[:4]), url=snap["url"], method="availability_api",
                      caveat="closest capture to 1995 — normally the earliest, but not guaranteed")
    if err and err2:
        return result("query_failed", error=f"cdx: {err}; availability: {err2}")
    return result("not_found")


# ------------------------------------------------------------------ similar resources
def q_similar(identity: dict) -> dict:
    name = identity["input"]["name"]
    bt = identity["matches"]["biotools"]
    re3 = identity["matches"]["re3data"]
    similar: dict[str, dict] = {}
    queries = []
    if bt.get("status") == "found":
        topics = [t["uri"].rsplit("/", 1)[-1] for t in bt["record"].get("topic", [])][:3]
        topic_terms = [t["term"] for t in bt["record"].get("topic", [])][:3]
        for tid, term in zip(topics, topic_terms):
            params = {"topicID": f'"{tid}"', "toolType": '"Database portal"', "format": "json", "sort": "citationCount", "ord": "desc"}
            data, err = get_json("https://bio.tools/api/tool/", params=params, timeout=40)
            queries.append({"source": "bio.tools", "topic": term, "error": err})
            for t in (data or {}).get("list", [])[:15]:
                if t["biotoolsID"] == bt["id"]:
                    continue
                rec = similar.setdefault(norm_name(t["name"]), {"name": t["name"], "url": t.get("homepage"),
                                                                "biotools": f"https://bio.tools/{t['biotoolsID']}",
                                                                "shared_topics": [], "description": (t.get("description") or "")[:250]})
                rec["shared_topics"].append(term)
    if re3.get("status") == "found":
        keywords = [first(k) for k in re3["record"].get("keyword", [])][:3]
        for kw in keywords:
            r, err = http_get("https://www.re3data.org/api/beta/repositories", params={"query": kw}, timeout=30)
            queries.append({"source": "re3data", "keyword": kw, "error": err})
            if r is not None and r.status_code == 200:
                for rid, rname in re.findall(r"<id>(r3d\d+)</id>.*?<name>(.*?)</name>", r.text, re.S)[:15]:
                    if rid == re3["id"] or norm_name(rname) == norm_name(name):
                        continue
                    rec = similar.setdefault(norm_name(rname), {"name": rname, "re3data": f"https://www.re3data.org/repository/{rid}",
                                                                "shared_topics": []})
                    rec.setdefault("re3data", f"https://www.re3data.org/repository/{rid}")
                    rec["shared_topics"].append(f"re3data keyword: {kw}")
    ranked = sorted(similar.values(), key=lambda s: len(s["shared_topics"]), reverse=True)
    if not queries:
        return result("not_found", note="No bio.tools/re3data record to derive topics from; use WebSearch for overlapping resources.")
    return result("found" if ranked else "not_found", queries=queries, candidates=ranked[:25],
                  note="Candidates share topics/keywords only; Claude must judge genuine overlap before listing any.")


# ------------------------------------------------------------------ BioHackathon / ELIXIR projects (S2.3)
def q_biohackathon(identity: dict) -> dict:
    """Evidence for S2.3c (BioHackathon/AHM) and hints for S2.3a/b: GitHub issues/PRs in the elixir-europe
    org mentioning the resource (BioHackathon-projects-YYYY repos hold project proposals) and BioHackrXiv /
    BioHackathon reports in Europe PMC. Absence is NOT evidence of 'No' — ELIXIR commissioned services are
    not systematically public."""
    import os
    import subprocess
    name = identity["input"]["name"]
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        try:
            token = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip()
        except Exception:  # noqa: BLE001
            token = None
    if token:
        headers["Authorization"] = f"Bearer {token}"
    gh_items, gh_err = [], None
    data, gh_err = get_json("https://api.github.com/search/issues", params={"q": f'"{name}" org:elixir-europe', "per_page": 30},
                            headers=headers, timeout=30)
    for it in (data or {}).get("items", []):
        repo = it["repository_url"].rsplit("/", 1)[-1]
        gh_items.append({"title": it["title"], "url": it["html_url"], "repo": repo,
                         "is_biohackathon_repo": "biohackathon" in repo.lower(), "created_at": it.get("created_at")})
    epmc, ep_err = get_json(EPMC, params={"query": f'"{name}" AND (BioHackathon OR BioHackrXiv OR "ELIXIR All Hands")',
                                          "format": "json", "pageSize": 25}, timeout=40)
    reports = [{"title": r.get("title"), "year": r.get("pubYear"), "source": r.get("journalTitle") or r.get("bookOrReportDetails", {}).get("publisher"),
                "url": f"https://doi.org/{r['doi']}" if r.get("doi") else f"https://europepmc.org/article/{r.get('source')}/{r.get('id')}"}
               for r in (epmc or {}).get("resultList", {}).get("result", [])]
    found = [i for i in gh_items if i["is_biohackathon_repo"]] or reports
    status = "found" if found else ("query_failed" if gh_err and ep_err else "not_found")
    return result(status, github_elixir_org_mentions=gh_items[:20], biohackathon_reports=reports[:15],
                  errors=[e for e in (gh_err, ep_err) if e] or None,
                  note="Mentions are leads, not proof of participation: Claude must read titles/links before answering S2.3c.")


# ------------------------------------------------------------------ registry summary
def q_summary(identity: dict) -> dict:
    m = identity["matches"]
    out: dict = {}
    re3 = m.get("re3data", {})
    if re3.get("status") == "found":
        r = re3["record"]

        def many(key, sub=None):
            vals = []
            for v in r.get(key, []):
                if sub and isinstance(v, dict):
                    vals.append({s: first(v.get(s)) for s in sub})
                else:
                    vals.append(first(v))
            return vals
        out["re3data"] = {
            "url": re3["url"], "name": first(r.get("repositoryName")), "repository_url": first(r.get("repositoryURL")),
            "description": first(r.get("description")), "types": many("type"), "content_types": many("contentType"),
            "subjects": many("subject"), "keywords": many("keyword"), "start_date": first(r.get("startDate")),
            "institutions": many("institution", ["institutionName", "institutionCountry", "responsibilityType", "institutionType", "institutionURL"]),
            "database_access": many("databaseAccess", ["databaseAccessType", "databaseAccessRestriction"]),
            "database_licenses": many("databaseLicense", ["databaseLicenseName", "databaseLicenseURL"]),
            "data_upload": many("dataUpload", ["dataUploadType", "dataUploadRestriction"]),
            "software": many("software", ["softwareName"]), "versioning": first(r.get("versioning")),
            "apis": [{"type": v.get("apiType"), "url": v.get("value")} if isinstance(v, dict) else {"url": v} for v in r.get("api", [])],
            "pid_systems": many("pidSystem"), "metadata_standards": many("metadataStandard", ["metadataStandardName", "metadataStandardURL"]),
            "certificates": many("certificate"), "quality_management": first(r.get("qualityManagement")),
            "last_update": first(r.get("lastUpdate")),
        }
    bt = m.get("biotools", {})
    if bt.get("status") == "found":
        t = bt["record"]
        out["biotools"] = {
            "url": bt["url"], "tool_types": t.get("toolType"), "topics": [x["term"] for x in t.get("topic", [])],
            "operations": sorted({o["term"] for f in t.get("function", []) for o in f.get("operation", [])}),
            "license": t.get("license"), "links": t.get("link"), "documentation": t.get("documentation"),
            "download": t.get("download"), "credit": t.get("credit"), "elixir_node": t.get("elixirNode"),
            "elixir_platform": t.get("elixirPlatform"), "elixir_community": t.get("elixirCommunity"),
            "collection": t.get("collectionID"), "maturity": t.get("maturity"), "cost": t.get("cost"),
            "accessibility": t.get("accessibility"), "publications": t.get("publication"),
            "other_matches": bt.get("other_matches"),
        }
    br = m.get("bioregistry", {})
    if br.get("status") == "found":
        out["bioregistry"] = {k: br["best"].get(k) for k in ("url", "id", "name", "description", "homepage", "mappings",
                                                            "repository", "contact", "license", "keywords", "depends_on", "appears_in")}
        out["bioregistry"]["ambiguous_candidates"] = [c["id"] for c in br.get("candidates", [])[1:]]
    for key in ("identifiers_org", "fairsharing", "uniprot_xref", "openebench"):
        v = m.get(key, {})
        out[key] = {k: v.get(k) for k in ("status", "id", "url", "mir_id", "resolver_example", "abbrev", "category",
                                          "api_detail", "note", "conclusive", "match_basis") if v.get(k) is not None}
    return result("found", **out)


SUBCOMMANDS = {"europepmc": q_europepmc, "tess": q_tess, "workflowhub": q_workflowhub, "apicuron": q_apicuron,
               "openebench": q_openebench, "wayback": q_wayback, "similar": q_similar, "biohackathon": q_biohackathon,
               "summary": q_summary}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=[*SUBCOMMANDS, "all"])
    ap.add_argument("--identity", required=True)
    ap.add_argument("--evidence-dir", required=True)
    args = ap.parse_args()
    identity = load_json(args.identity)
    evdir = Path(args.evidence_dir)
    commands = list(SUBCOMMANDS) if args.command == "all" else [args.command]
    for cmd in commands:
        log(f"[registries] {cmd}")
        try:
            data = SUBCOMMANDS[cmd](identity)
        except Exception as exc:  # noqa: BLE001 — one failing registry must not abort the rest
            data = result("query_failed", error=f"{type(exc).__name__}: {exc}")
        data["_generated"] = now_iso()
        write_json(evdir / f"registry_{cmd}.json", data)
        print(f"{cmd}: {data.get('status')}" + (f" ({data.get('error')})" if data.get("error") else ""))


if __name__ == "__main__":
    main()
