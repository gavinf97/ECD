#!/usr/bin/env python3
"""
resolve_resource.py — Phase 2 of the ECD Agent Skill.

Given a biodata resource name + URL, establishes the resource's identity across
the registries the ECD Checklist refers to, matching primarily on homepage
domain (strong) and normalised name (weaker):

  Bioregistry (full registry JSON, cached)    -> prefix, mappings (FAIRsharing, re3data,
                                                 MIRIAM/identifiers.org, bio.tools, UniProt...)
  identifiers.org registry API                 -> namespace prefix, MIR id
  re3data API (XML)                            -> repository record (types, licences, APIs,
                                                 metadata standards, institutions, versioning)
  bio.tools API                                -> tool/database record (topics, links, licence,
                                                 publications, credits)
  FAIRsharing                                  -> record id via Bioregistry mapping; API detail
                                                 only if FAIRSHARING_USERNAME/PASSWORD are set
  UniProt cross-reference database list        -> DB-xxxx (evidence of data outflow)
  OpenEBench monitor                           -> monitored tool id
  Code repository discovery                    -> GitHub/GitLab URLs from the above + homepage

Every registry result carries status found | not_found | query_failed, the
match basis and the evidence URL. Ambiguous candidates are listed so Claude
can confirm with the user.

Usage:
    python resolve_resource.py --name "DisProt" --url https://disprot.org [--repo URL] --out WORKDIR/identity.json
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (BROWSER_UA, cached_download, create_session, domain_of, emit,  # noqa: E402
                    get_json, http_get, load_json, log, norm_name, now_iso, result, same_site)

BIOREGISTRY_JSON = "https://raw.githubusercontent.com/biopragmatics/bioregistry/main/src/bioregistry/data/bioregistry.json"
REPO_RE = re.compile(r"https?://(?:www\.)?(github\.com|gitlab\.com|bitbucket\.org|codeberg\.org|gitlab\.[a-z0-9.-]+)/"
                     r"([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", re.I)
GENERIC_REPO_OWNERS = {"sponsors", "features", "about", "orgs", "topics", "login", "marketplace", "apps"}
BROWSER = create_session(user_agent=BROWSER_UA)


# ---------------------------------------------------------------- homepage
def probe_homepage(url: str) -> dict:
    r, err = http_get(url, session=BROWSER, timeout=30)
    if err:
        return result("query_failed", url=url, error=err)
    title = re.search(r"<title[^>]*>(.*?)</title>", r.text, re.S | re.I)
    return result("found" if r.status_code < 400 else "query_failed", url=url, final_url=r.url,
                  http_status=r.status_code, elapsed_ms=int(r.elapsed.total_seconds() * 1000),
                  title=re.sub(r"\s+", " ", title.group(1)).strip() if title else None,
                  html_excerpt_links=sorted(set(m.group(0) for m in REPO_RE.finditer(r.text)))[:20])


# ---------------------------------------------------------------- bioregistry
def match_bioregistry(name: str, url: str) -> dict:
    path, err = cached_download(BIOREGISTRY_JSON, "bioregistry.json", max_age_days=7)
    if err or not path:
        return result("query_failed", error=err)
    registry = load_json(path)
    target = norm_name(name)
    candidates = []
    for prefix, rec in registry.items():
        basis = []
        homepages = [rec.get("homepage")] + [(rec.get(k) or {}).get("homepage") for k in
                                              ("miriam", "fairsharing", "re3data", "biocontext", "prefixcommons", "n2t")]
        uri_formats = [rec.get("uri_format")] + [(rec.get(k) or {}).get("uri_format") for k in ("miriam", "n2t")]
        if any(h and same_site(h, url) for h in homepages):
            basis.append("homepage_domain")
        elif any(u and same_site(u.split("$1")[0], url) for u in uri_formats):
            basis.append("uri_format_domain")
        names = {norm_name(prefix), norm_name(rec.get("name", ""))} | {norm_name(s) for s in rec.get("synonyms", [])}
        if target and target in names:
            basis.append("name")
        if basis:
            candidates.append((prefix, rec, basis))
    if not candidates:
        return result("not_found", searched=BIOREGISTRY_JSON)
    candidates.sort(key=lambda c: (("homepage_domain" in c[2] or "uri_format_domain" in c[2]) and "name" in c[2],
                                   "homepage_domain" in c[2], "name" in c[2], -len(c[0])), reverse=True)
    out = []
    for prefix, rec, basis in candidates[:8]:
        out.append({
            "id": prefix, "url": f"https://bioregistry.io/{prefix}", "match_basis": basis,
            "name": rec.get("name"), "description": rec.get("description"), "homepage": rec.get("homepage"),
            "mappings": rec.get("mappings", {}), "publications": rec.get("publications", []),
            "repository": rec.get("repository"), "contact": rec.get("contact"), "keywords": rec.get("keywords"),
            "depends_on": rec.get("depends_on"), "appears_in": rec.get("appears_in"),
            "license": rec.get("license"), "deprecated": rec.get("deprecated"),
            "part_of": rec.get("part_of"), "has_canonical": rec.get("has_canonical"),
        })
    best = out[0]
    ambiguous = [c for c in out[1:] if c["match_basis"] == best["match_basis"] and not c.get("part_of")]
    return result("found", best=best, candidates=out, ambiguous=bool(ambiguous))


# ---------------------------------------------------------------- identifiers.org
def match_identifiers(name: str, url: str, prefix_hints: list[str]) -> dict:
    base = "https://registry.api.identifiers.org/restApi"
    tried, errors = [], []
    prefixes = list(dict.fromkeys([p.lower() for p in prefix_hints if p]))
    if not prefixes:
        data, err = get_json(f"{base}/namespaces/search/findByPrefixContaining", params={"content": norm_name(name)})
        if err:
            errors.append(err)
        else:
            prefixes = [n["prefix"] for n in (data or {}).get("_embedded", {}).get("namespaces", [])][:5]
    for prefix in prefixes:
        tried.append(prefix)
        ns, err = get_json(f"{base}/namespaces/search/findByPrefix", params={"prefix": prefix})
        if err:
            if "404" not in err:
                errors.append(err)
            continue
        res, _ = get_json(ns["_links"]["resources"]["href"]) if ns.get("_links", {}).get("resources") else (None, None)
        resources = (res or {}).get("_embedded", {}).get("resources", [])
        home_match = any(same_site(r.get("resourceHomeUrl") or r.get("urlPattern", ""), url) for r in resources)
        name_match = norm_name(ns.get("name")) == norm_name(name) or prefix == norm_name(name)
        if home_match or name_match or prefix in [p.lower() for p in prefix_hints]:
            return result("found", id=prefix, mir_id=ns.get("mirId"), name=ns.get("name"),
                          description=ns.get("description"), pattern=ns.get("pattern"), sample_id=ns.get("sampleId"),
                          url=f"https://registry.identifiers.org/registry/{prefix}",
                          resolver_example=f"https://identifiers.org/{prefix}:{ns.get('sampleId')}" if ns.get("sampleId") else None,
                          match_basis=["homepage_domain"] * home_match + ["name"] * name_match or ["bioregistry_mapping"],
                          resources=[{"name": r.get("name"), "home": r.get("resourceHomeUrl"), "urlPattern": r.get("urlPattern"),
                                      "institution": (r.get("institution") or {}).get("name")} for r in resources])
    if errors and not tried:
        return result("query_failed", error="; ".join(errors))
    return result("not_found", tried_prefixes=tried, errors=errors or None)


# ---------------------------------------------------------------- re3data
def xml_children_to_dict(elem: ET.Element) -> dict:
    out: dict = {}
    for child in elem:
        tag = child.tag.split("}")[-1]
        if len(child):
            val = xml_children_to_dict(child)
        else:
            val = (child.text or "").strip()
            if child.attrib:
                val = {"value": val, **{k.split('}')[-1]: v for k, v in child.attrib.items()}}
        out.setdefault(tag, []).append(val)
    return out


def fetch_re3data_record(r3d_id: str) -> tuple[dict | None, str | None]:
    r, err = http_get(f"https://www.re3data.org/api/beta/repository/{r3d_id}", timeout=30)
    if err or r.status_code != 200:
        return None, err or f"HTTP {r.status_code}"
    try:
        root = ET.fromstring(r.content)
    except ET.ParseError as exc:
        return None, f"XML parse error: {exc}"
    repo = next((e for e in root.iter() if e.tag.split("}")[-1] == "repository"), None)
    return (xml_children_to_dict(repo) if repo is not None else None), None


def match_re3data(name: str, url: str, id_hint: str | None) -> dict:
    ids = [id_hint] if id_hint else []
    if not ids:
        r, err = http_get("https://www.re3data.org/api/beta/repositories", params={"query": name}, timeout=30)
        if err or r.status_code != 200:
            return result("query_failed", error=err or f"HTTP {r.status_code}")
        try:
            root = ET.fromstring(r.content)
            ids = [e.text for e in root.iter("id")][:6]
        except ET.ParseError as exc:
            return result("query_failed", error=f"XML parse error: {exc}")
    for rid in ids:
        rec, err = fetch_re3data_record(rid)
        if not rec:
            continue
        rurl = (rec.get("repositoryURL") or [""])[0]
        rname = (rec.get("repositoryName") or [""])[0]
        rname = rname.get("value") if isinstance(rname, dict) else rname
        basis = (["homepage_domain"] if same_site(rurl, url) else []) + (["name"] if norm_name(rname) == norm_name(name) else [])
        if basis or rid == id_hint:
            return result("found", id=rid, url=f"https://www.re3data.org/repository/{rid}", name=rname,
                          match_basis=basis or ["bioregistry_mapping"], record=rec)
    return result("not_found", checked_ids=ids)


# ---------------------------------------------------------------- bio.tools
def match_biotools(name: str, url: str, id_hint: str | None) -> dict:
    base = "https://bio.tools/api/tool"
    if id_hint:
        data, err = get_json(f"{base}/{quote(id_hint)}/", params={"format": "json"})
        if data:
            return result("found", id=data["biotoolsID"], url=f"https://bio.tools/{data['biotoolsID']}",
                          match_basis=["bioregistry_mapping"], record=data)
    hits, errors = {}, []
    for q in (name, domain_of(url)):
        data, err = get_json(f"{base}/", params={"q": q, "format": "json"})
        if err:
            errors.append(err)
            continue
        for t in (data or {}).get("list", []):
            hits[t["biotoolsID"]] = t
    scored = []
    for tid, t in hits.items():
        basis = (["homepage_domain"] if same_site(t.get("homepage", ""), url) else []) + \
                (["name"] if norm_name(t.get("name")) == norm_name(name) or norm_name(tid) == norm_name(name) else [])
        if basis:
            scored.append((len(basis), "Database portal" in (t.get("toolType") or []), tid, t, basis))
    if scored:
        scored.sort(reverse=True, key=lambda s: (s[0], s[1]))
        _, _, tid, t, basis = scored[0]
        return result("found", id=tid, url=f"https://bio.tools/{tid}", match_basis=basis, record=t,
                      other_matches=[{"id": s[2], "match_basis": s[4], "toolType": s[3].get("toolType")} for s in scored[1:6]])
    if errors and not hits:
        return result("query_failed", error="; ".join(errors))
    return result("not_found", candidates_checked=list(hits)[:10])


# ---------------------------------------------------------------- FAIRsharing
def fairsharing_token() -> str | None:
    user, pwd = os.environ.get("FAIRSHARING_USERNAME"), os.environ.get("FAIRSHARING_PASSWORD")
    if not (user and pwd):
        return None
    s = create_session()
    try:
        r = s.post("https://api.fairsharing.org/users/sign_in", json={"user": {"login": user, "password": pwd}},
                   headers={"Accept": "application/json", "Content-Type": "application/json"}, timeout=30)
        return r.json().get("jwt") if r.status_code == 200 else None
    except Exception:  # noqa: BLE001
        return None


def match_fairsharing(name: str, url: str, id_hint: str | None) -> dict:
    token = fairsharing_token()
    if id_hint:
        rec_url = f"https://fairsharing.org/{id_hint}"
        out = result("found", id=id_hint, url=rec_url, match_basis=["bioregistry_mapping"], api_detail=False)
        if token:
            data, err = get_json(f"https://api.fairsharing.org/fairsharing_records/{id_hint}",
                                 headers={"Authorization": f"Bearer {token}"})
            if data:
                out.update(api_detail=True, record=data.get("data", data))
            else:
                out["api_error"] = err
        return out
    if not token:
        return result("not_found", note="No Bioregistry mapping to FAIRsharing and no FAIRSHARING_USERNAME/PASSWORD set; "
                                        "search https://fairsharing.org manually or via WebSearch before concluding 'No'.",
                      conclusive=False)
    s = create_session()
    try:
        r = s.post("https://api.fairsharing.org/search/fairsharing_records", params={"q": name},
                   headers={"Authorization": f"Bearer {token}", "Accept": "application/json"}, timeout=30)
        records = r.json().get("data", []) if r.status_code == 200 else None
    except Exception as exc:  # noqa: BLE001
        return result("query_failed", error=str(exc))
    if records is None:
        return result("query_failed", error=f"HTTP {r.status_code}")
    for rec in records:
        attrs = rec.get("attributes", {})
        if same_site(attrs.get("url") or attrs.get("homepage") or "", url) or norm_name(attrs.get("name")) == norm_name(name):
            rid = attrs.get("url_for_logo") and rec.get("id") or rec.get("id")
            return result("found", id=rid, url=f"https://fairsharing.org/{rid}", match_basis=["api_search"], record=attrs)
    return result("not_found", conclusive=True)


# ---------------------------------------------------------------- UniProt / OpenEBench
def match_uniprot_xref(name: str, url: str, id_hint: str | None) -> dict:
    data, err = get_json("https://rest.uniprot.org/database/search", params={"query": id_hint or name, "format": "json"})
    if err:
        return result("query_failed", error=err)
    for db in data.get("results", []):
        servers = db.get("servers") or []
        if db.get("id") == id_hint or any(same_site(s, url) for s in servers) or norm_name(db.get("abbrev")) == norm_name(name):
            return result("found", id=db["id"], abbrev=db.get("abbrev"), name=db.get("name"), category=db.get("category"),
                          url=f"https://www.uniprot.org/database/{db['id']}", servers=servers)
    return result("not_found")


def match_openebench(name: str, url: str) -> dict:
    data, err = get_json("https://openebench.bsc.es/monitor/rest/search", params={"name": name}, timeout=40)
    if err:
        return result("query_failed", error=err)
    for tool in data or []:
        home = (tool.get("web") or {}).get("homepage") or ""
        if same_site(home, url):
            tid = tool.get("@label")
            return result("found", id=tid, url=tool.get("@id"), homepage=home, match_basis=["homepage_domain"],
                          metrics_url=f"https://openebench.bsc.es/monitor/metrics/{tid}")
    return result("not_found", checked=len(data or []))


# ---------------------------------------------------------------- repositories
def collect_repositories(explicit: str | None, homepage: dict, bioreg: dict, biotools: dict, name: str) -> list[dict]:
    found: dict[str, dict] = {}

    def add(url: str | None, source: str) -> None:
        if not url:
            return
        m = REPO_RE.search(url)
        if not m or m.group(2).lower() in GENERIC_REPO_OWNERS:
            return
        canon = f"https://{m.group(1).lower()}/{m.group(2)}/{m.group(3).removesuffix('.git')}"
        found.setdefault(canon, {"url": canon, "sources": []})["sources"].append(source)

    add(explicit, "input")
    if bioreg.get("status") == "found":
        add(bioreg["best"].get("repository"), "bioregistry")
    if biotools.get("status") == "found":
        for link in biotools["record"].get("link", []) + biotools["record"].get("download", []):
            add(link.get("url"), f"bio.tools:{','.join(link.get('type') or [])}")
    for link in homepage.get("html_excerpt_links") or []:
        add(link, "homepage_link")
    target = norm_name(name)
    ranked = sorted(found.values(), key=lambda r: ("input" in r["sources"], target in norm_name(r["url"]), len(r["sources"])),
                    reverse=True)
    return ranked


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--repo")
    ap.add_argument("--out")
    args = ap.parse_args()
    url = args.url if "://" in args.url else f"https://{args.url}"

    log(f"[resolve] homepage {url}")
    homepage = probe_homepage(url)
    log("[resolve] bioregistry")
    bioreg = match_bioregistry(args.name, homepage.get("final_url") or url)
    maps = bioreg["best"]["mappings"] if bioreg.get("status") == "found" else {}
    prefix_hints = [maps.get("miriam"), maps.get("n2t")] + ([bioreg["best"]["id"]] if maps.get("miriam") else [])
    log("[resolve] identifiers.org")
    identifiers = match_identifiers(args.name, url, [p for p in prefix_hints if p])
    log("[resolve] re3data")
    re3 = match_re3data(args.name, url, maps.get("re3data"))
    log("[resolve] bio.tools")
    biotools = match_biotools(args.name, url, maps.get("biotools"))
    log("[resolve] FAIRsharing")
    fairsharing = match_fairsharing(args.name, url, maps.get("fairsharing"))
    log("[resolve] UniProt xref DB")
    uniprot = match_uniprot_xref(args.name, url, maps.get("uniprot"))
    log("[resolve] OpenEBench")
    oeb = match_openebench(args.name, url)
    repos = collect_repositories(args.repo, homepage, bioreg, biotools, args.name)

    identity = {
        "input": {"name": args.name, "url": url, "repo": args.repo},
        "resolved_at": now_iso(),
        "homepage": homepage,
        "matches": {"bioregistry": bioreg, "identifiers_org": identifiers, "re3data": re3, "biotools": biotools,
                    "fairsharing": fairsharing, "uniprot_xref": uniprot, "openebench": oeb},
        "repositories": repos,
        "chosen_repo": repos[0]["url"] if repos else None,
        "needs_confirmation": [k for k, v in {"bioregistry": bioreg.get("ambiguous"),
                                                "repository": len(repos) > 1 and not args.repo}.items() if v],
    }
    summary = {k: (v.get("status"), v.get("id") or (v.get("best") or {}).get("id")) for k, v in identity["matches"].items()}
    summary["repo"] = identity["chosen_repo"]
    emit(identity, args.out, summary=summary)


if __name__ == "__main__":
    main()
