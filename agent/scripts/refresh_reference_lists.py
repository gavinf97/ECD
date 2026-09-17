#!/usr/bin/env python3
"""
refresh_reference_lists.py — builds references/elixir_reference_lists.json.

Collects the ELIXIR lists the ECD Checklist Section 1 eligibility check needs:
  - ELIXIR Nodes, and each Node's Service Delivery Plan (SDP) services
    (name + homepage URL) from the Node pages on elixir-europe.org
  - ELIXIR Communities
  - Core Data Resources (CDR), ELIXIR Deposition Databases (EDD),
    Recommended Interoperability Resources (RIR)
  - Global Core Biodata Resources (GCBR) from the globalbiodata.org list page

elixir-europe.org returns HTTP 403 to non-browser clients (verified 2026-09-17),
so each page is fetched live first and then from the latest Wayback Machine
snapshot. Every list records its source URL, the snapshot actually used and a
retrieval date, so staleness is visible downstream.

Usage:
    python refresh_reference_lists.py [--out references/elixir_reference_lists.json]
                                      [--only nodes,communities,cdr,edd,rir,gcbr]
"""

from __future__ import annotations

import argparse
import html as htmllib
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (BROWSER_UA, REFERENCES, create_session, http_get, load_json,  # noqa: E402
                    log, now_iso, wayback_get, write_json)

ELIXIR = "https://elixir-europe.org"
BROWSER = create_session(user_agent=BROWSER_UA)


def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", htmllib.unescape(text)).strip()


def fetch_page(url: str) -> tuple[str | None, dict]:
    """Live first (browser UA), then Wayback. Returns (html, provenance)."""
    r, err = http_get(url, session=BROWSER, timeout=30)
    if r is not None and r.status_code == 200 and len(r.text) > 2000:
        return r.text, {"source_url": url, "fetched_via": "live", "retrieved": now_iso()}
    live_status = err or f"HTTP {r.status_code}"
    log(f"  live fetch failed ({live_status}); trying Wayback for {url}")
    html, snap, werr = wayback_get(url)
    if html:
        m = re.search(r"/web/(\d{14})", snap or "")
        return html, {"source_url": url, "fetched_via": "wayback", "snapshot_url": snap,
                      "snapshot_timestamp": m.group(1) if m else None,
                      "live_error": live_status, "retrieved": now_iso()}
    return None, {"source_url": url, "error": f"live: {live_status}; wayback: {werr}", "retrieved": now_iso()}


def main_region(html: str) -> str:
    m = re.search(r"<main.*?</main>", html, re.S)
    return m.group(0) if m else html


def parse_resource_table(html: str, base: str) -> list[dict]:
    """First two cells of each row in tables inside <main>: name(+link), description."""
    items = []
    for table in re.findall(r"<table.*?</table>", main_region(html), re.S):
        for row in re.findall(r"<tr.*?</tr>", table, re.S):
            cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
            if len(cells) < 1:
                continue
            link = re.search(r'<a[^>]+href="([^"]+)"', cells[0])
            name = clean(cells[0])
            if not name:
                continue
            items.append({"name": name,
                          "url": urljoin(base, htmllib.unescape(link.group(1))) if link else None,
                          "description": clean(cells[1])[:300] if len(cells) > 1 else None})
    return items


def build_status_list(path: str) -> dict:
    url = f"{ELIXIR}/{path}"
    log(f"[status] {url}")
    html, prov = fetch_page(url)
    if not html:
        return {**prov, "items": []}
    items = parse_resource_table(html, ELIXIR)
    return {**prov, "count": len(items), "items": items}


def build_communities() -> dict:
    url = f"{ELIXIR}/communities"
    log(f"[communities] {url}")
    html, prov = fetch_page(url)
    if not html:
        return {**prov, "items": []}
    seen: dict[str, dict] = {}
    for href, text in re.findall(r'<a[^>]+href="([^"]*?/communities/[a-z0-9-]+)"[^>]*>(.*?)</a>', html, re.S):
        name = clean(text)
        name = re.sub(r"\s*\([^)]*\)$", "", name)
        name = re.sub(r"\s+Community$", "", name)
        if not name or name.lower() in {"communities", "elixir communities"} or re.search(r"election|handbook|news", name, re.I):
            continue
        key = re.sub(r"[^a-z0-9]", "", name.lower())
        seen.setdefault(key, {"name": name, "url": urljoin(ELIXIR, href)})
    items = sorted(seen.values(), key=lambda x: x["name"].lower())
    return {**prov, "count": len(items), "items": items}


def build_nodes() -> dict:
    url = f"{ELIXIR}/about-us/who-we-are/nodes"
    log(f"[nodes] {url}")
    html, prov = fetch_page(url)
    if not html:
        return {**prov, "items": []}
    nodes: dict[str, dict] = {}
    for href, text in re.findall(r'<a[^>]+href="([^"]*?/about-us/who-we-are/nodes/[a-z0-9-]+)"[^>]*>(.*?)</a>', html, re.S):
        name = re.sub(r"\s*\(.*$", "", clean(text))
        slug = href.rstrip("/").rsplit("/", 1)[-1]
        if not name or slug in nodes:
            continue
        nodes[slug] = {"name": name, "slug": slug, "label": "EMBL-EBI" if slug == "embl-ebi" else f"ELIXIR-{name}",
                       "url": urljoin(ELIXIR, href)}
    items = []
    for slug, node in sorted(nodes.items()):
        log(f"  [node] {node['name']}")
        nhtml, nprov = fetch_page(node["url"])
        services = []
        if nhtml:
            m = re.search(r"(\d+)\s+services", nhtml)
            node["declared_service_count"] = int(m.group(1)) if m else None
            tables = re.findall(r"<table.*?</table>", main_region(nhtml), re.S)
            for row in re.findall(r"<tr.*?</tr>", tables[0] if tables else "", re.S):
                cell = re.search(r'views-field-title"[^>]*>(.*?)</td>', row, re.S)
                if not cell:
                    continue
                link = re.search(r'<a[^>]+href="([^"]+)"', cell.group(1))
                name = clean(cell.group(1))
                stype = re.search(r'views-field-field-type-of-service"[^>]*>(.*?)</td>', row, re.S)
                if name:
                    services.append({"name": name, "url": htmllib.unescape(link.group(1)).strip() if link else None,
                                     "type": clean(stype.group(1)) if stype else None})
        node["services"] = services
        node["page_provenance"] = nprov
        items.append(node)
    return {**prov, "count": len(items), "items": items}


def build_gcbr() -> dict:
    url = "https://globalbiodata.org/what-we-do/global-core-biodata-resources/list-of-current-global-core-biodata-resources/"
    log(f"[gcbr] {url}")
    html, prov = fetch_page(url)
    if not html:
        return {**prov, "items": []}
    items, seen = [], set()
    # Each resource is a WordPress column block: <h2><a href=URL>Name</a></h2><p><strong>Country</strong>...</p>
    for href, name, tail in re.findall(r'<h2[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>\s*</h2>(.{0,400})', html, re.S):
        name = clean(name)
        if not name or name.lower() in seen:
            continue
        seen.add(name.lower())
        country = re.search(r"<p[^>]*>(.*?)</p>", tail, re.S)
        items.append({"name": name, "url": htmllib.unescape(href), "host_countries": clean(country.group(1)) if country else None})
    return {**prov, "count": len(items), "items": items}


BUILDERS = {
    "nodes": build_nodes,
    "communities": build_communities,
    "cdr": lambda: build_status_list("platforms/data/core-data-resources"),
    "edd": lambda: build_status_list("platforms/data/elixir-deposition-databases"),
    "rir": lambda: build_status_list("platforms/interoperability/rirs"),
    "gcbr": build_gcbr,
}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(REFERENCES / "elixir_reference_lists.json"))
    ap.add_argument("--only", default=",".join(BUILDERS))
    args = ap.parse_args()

    out = Path(args.out)
    data = load_json(out) if out.exists() else {}
    data["_about"] = ("Reference lists for the ECD Agent Skill eligibility checks. Rebuild with "
                      "scripts/refresh_reference_lists.py. Treat lists older than ~6 months as stale.")
    summary = {}
    for key in [k.strip() for k in args.only.split(",") if k.strip()]:
        if key not in BUILDERS:
            log(f"unknown list {key}; skipping")
            continue
        built = BUILDERS[key]()
        if not built.get("items") and data.get(key, {}).get("items"):
            log(f"[{key}] refresh produced no items ({built.get('error')}); keeping previous snapshot")
            data[key]["last_refresh_error"] = built.get("error")
        else:
            data[key] = built
        summary[key] = len(data.get(key, {}).get("items", []))
    data["generated"] = now_iso()
    write_json(out, data)
    print({"written": str(out), "counts": summary})


if __name__ == "__main__":
    main()
