#!/usr/bin/env python3
"""
probe_website.py — Phase 3 (website evidence) of the ECD Agent Skill.

A polite, bounded crawl of the resource website that records *evidence
snippets*, never conclusions. Used for Checklist questions registries cannot
answer: team page (S4.4), helpdesk (S4.3), feedback (S4.2), roadmap/releases
(S4.1, S6.4), SAB (S4.9), privacy (S4.10), ethics (S4.11), data licence (S6.2),
APIs/FTP/SPARQL (S5.4), structured data / Bioschemas JSON-LD (S5.3),
ontology CURIEs (S5.2), analytics (S3.2), status/uptime pages (S3.1),
LS-AAI login (S7.6), APICURON/RDMkit/RSQkit mentions (S7.5, S7.9, S7.10).

Crawl rules:
  - honours robots.txt; max --max-pages same-site pages (default 25); 1 s delay
  - HTML comments are stripped before scanning (commented-out widgets are not evidence)
  - single-page apps are detected and, if Playwright is available (current Python or
    $ECD_PLAYWRIGHT_PYTHON), rendered via render_pages.py; otherwise flagged as
    `spa_unrendered` so Claude knows the evidence is thin
  - SPA index fallbacks (every path returning the same shell) are not counted as pages

Usage:
    python probe_website.py --identity WORKDIR/identity.json --out WORKDIR/evidence/website.json
                            [--max-pages 25] [--no-render]
"""

from __future__ import annotations

import argparse
import hashlib
import html as htmllib
import json
import re
import subprocess
import sys
import tempfile
import time
import urllib.robotparser
from pathlib import Path
from urllib.parse import urljoin, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (BROWSER_UA, create_session, emit, get_json, http_get, load_json, log,  # noqa: E402
                    now_iso, same_site)
from render_pages import playwright_python  # noqa: E402

BROWSER = create_session(user_agent=BROWSER_UA, max_retries=1)
SCRIPTS = Path(__file__).resolve().parent

# topic -> (regex over visible text/anchor text, regex over URLs)
TOPICS: dict[str, tuple[str, str]] = {
    "team": (r"\b(our team|the team|team members?|people|staff|who we are|contributors|curators|developers|group members)\b",
             r"/(team|people|staff|about|who-we-are|contributors|members)\b"),
    "helpdesk": (r"\b(help ?desk|support|contact us|get in touch|faq|frequently asked|mailing list|e-?mail us)\b",
                 r"/(help|support|contact|faq)\b|mailto:"),
    "feedback": (r"\b(feedback|user survey|suggest(ion)?s?|report (a|an) (issue|bug|error)|feature request|user forum)\b",
                 r"/(feedback|survey|issues)\b|github\.com/[^/]+/[^/]+/issues"),
    "roadmap": (r"\b(road ?map|release notes?|changelog|what'?s new|upcoming (features|release)|future developments?|news)\b",
                r"/(roadmap|release-?notes|changelog|news|releases)\b"),
    "versions": (r"\b(previous (releases|versions)|release archive|archived? (releases|versions)|version \d+(\.\d+)*|release \d{4}_\d+|data release)\b",
                 r"/(releases?|archive|versions?|previous)\b|ftp://|/pub/"),
    "sab": (r"\b(scientific advisory board|advisory board|advisory committee|steering committee|\bSAB\b)",
            r"/(sab|advisory|board|governance)\b"),
    "privacy": (r"\b(privacy (policy|notice|statement)|data protection|GDPR|cookie (policy|notice))\b",
                r"/(privacy|gdpr|cookie|data-protection)"),
    "ethics": (r"\b(ethic(s|al)|sensitive data|informed consent|data access committee|controlled access)\b",
               r"/(ethic|consent)"),
    "license": (r"\b(licen[cs]e[ds]?|terms of (use|service)|creative commons|CC[- ]BY(-[A-Z]{2})*( \d\.\d)?|CC0|public domain)\b",
                r"/(licen[cs]e|terms|legal)|creativecommons\.org"),
    "funding": (r"\b(funded by|funding|supported by|grant (agreement|no\.?|number)|horizon (2020|europe)|acknowledg(e)?ments?)\b",
                r"/(funding|acknowledg)"),
    "citation": (r"\b(how to cite|cite us|citing|please cite)\b", r"/(cite|citation|citing)"),
    "api": (r"\b(REST(ful)? API|web services?|API documentation|programmatic access|swagger|openapi|SPARQL( endpoint)?|GraphQL)\b",
            r"/(api|swagger|openapi|sparql|graphql|ws|webservices?)\b"),
    "download": (r"\b(bulk download|download(s)?|FTP|data dumps?)\b", r"/(download|ftp|dumps?)\b|^ftp://"),
    "statistics": (r"\b(statistics|stats|number of entries|\d[\d,.]* (entries|proteins|sequences|records|genomes|annotations))\b",
                   r"/(statistics|stats)\b"),
    "monitoring": (r"\b(status page|uptime|service status|updown\.io|uptimerobot|statuspage)\b",
                   r"updown\.io|uptimerobot|statuspage\.io|status\."),
    "dmp": (r"\b(data management plan|DMP)\b", r"dmp"),
    "smp": (r"\b(software management plan|SMP)\b", r"smp"),
    "backup": (r"\b(back-?ups?|mirror(s|ed)? site|off-?site|disaster recovery)\b", r"/mirror"),
    "container": (r"\b(docker|singularity|apptainer|podman|container image|biocontainers)\b",
                  r"hub\.docker\.com|quay\.io|ghcr\.io|biocontainers"),
    "elixir": (r"\bELIXIR\b", r"elixir-europe\.org"),
    "apicuron": (r"\bAPICURON\b", r"apicuron\.org"),
    "rdmkit": (r"\bRDMkit\b", r"rdmkit\.elixir-europe\.org"),
    "rsqkit": (r"\bRSQkit\b", r"rsqkit|everse\.software"),
    "aai": (r"\b(Life ?Science Login|LS ?Login|LS-AAI|ELIXIR AAI|ELIXIR login|sign in|log ?in)\b",
            r"login\.aai\.lifescience-ri\.eu|aai\.lifescience-ri\.eu|login\.elixir-czech|/login|/signin|orcid\.org/oauth"),
    "ontology": (r"\b(ontolog(y|ies)|controlled vocabular(y|ies)|OBO|EDAM|Gene Ontology)\b",
                 r"ebi\.ac\.uk/ols|obofoundry|/ontology"),
    "metadata_standard": (r"\b(Bioschemas|schema\.org|MIAME|MIAPE|MIxS|minimum information|metadata standard|DCAT|FAIRsharing)\b",
                          r"bioschemas\.org|fairsharing\.org"),
}
LSAAI_RE = re.compile(r"(login\.aai\.lifescience-ri\.eu|aai\.lifescience-ri\.eu|life ?science ?login|ls[- ]aai|elixir[- ]aai)", re.I)
ANALYTICS = {"Google Analytics / Tag Manager": r"google-analytics\.com|googletagmanager\.com|gtag\(",
             "Matomo/Piwik": r"matomo|piwik", "Plausible": r"plausible\.io", "Umami": r"umami", "StatCounter": r"statcounter"}
REGISTRY_LINK_RE = re.compile(r"(fairsharing\.org|identifiers\.org|bio\.tools|tess\.elixir-europe\.org|workflowhub\.eu|apicuron\.org|"
                              r"openebench|rdmkit\.elixir-europe|everse\.software|zenodo\.org|github\.com|gitlab\.com|hub\.docker\.com|"
                              r"quay\.io|biocontainers|creativecommons\.org|elixir-europe\.org|re3data\.org|ebi\.ac\.uk/ols|"
                              r"lifescience-ri\.eu|status\.|updown\.io|uptimerobot)", re.I)
CURIE_RE = re.compile(r"\b(GO|ECO|NCBITaxon|IDPO|SO|CHEBI|UBERON|MI|MOD|MONDO|HP|DOID|EFO|OBI|PATO|CL|UO|BTO|EDAM|SBO|PR|NCIT|"
                      r"ENVO|PO|TO|FBbt|ZFA|MA|OMIT|MS|XLMOD|EFO|ORDO|MAXO|CHMO|BAO|ERO|SWO|OGMS|NCBIGene)[:_](\d{3,9})\b")
GUESS_PATHS = ["about", "help", "contact", "faq", "team", "people", "privacy", "privacy-policy", "terms", "license", "licence",
               "api", "api/docs", "docs", "documentation", "download", "downloads", "statistics", "stats", "news",
               "release-notes", "releases", "changelog", "cite", "citation", "funding", "feedback", "governance"]
URL_SCORE_RE = re.compile(r"about|help|contact|faq|team|people|privacy|terms|licen|api|doc|download|stat|news|release|"
                          r"change|cite|citation|fund|feedback|governance|advis|legal|policy|ftp|training|ontology|login", re.I)


def strip_comments(html: str) -> str:
    return re.sub(r"<!--.*?-->", "", html, flags=re.S)


def visible_text(html: str) -> str:
    html = re.sub(r"<(script|style|noscript|svg|template)[^>]*>.*?</\1>", " ", strip_comments(html), flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", htmllib.unescape(text)).strip()


def extract_links(html: str, base: str) -> list[dict]:
    links = []
    for href, anchor in re.findall(r'<a\b[^>]*href="([^"#][^"]*)"[^>]*>(.*?)</a>', strip_comments(html), re.S | re.I):
        href = htmllib.unescape(href.strip())
        if href.startswith(("javascript:", "data:")):
            continue
        links.append({"url": urljoin(base, href), "text": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", anchor)).strip()[:120]})
    return links


def extract_jsonld(html: str) -> list:
    blocks = []
    for raw in re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S | re.I):
        try:
            blocks.append(json.loads(raw.strip()))
        except ValueError:
            blocks.append({"_unparseable": raw.strip()[:300]})
    return blocks


def jsonld_summary(blocks: list) -> list[dict]:
    out = []

    def walk(node):
        if isinstance(node, list):
            for n in node:
                walk(n)
        elif isinstance(node, dict):
            if "@type" in node:
                out.append({k: node.get(k) for k in ("@type", "name", "url", "identifier", "license", "conformsTo",
                                                    "dct:conformsTo", "http://purl.org/dc/terms/conformsTo", "version") if node.get(k)})
            for key in ("@graph", "mainEntity", "hasPart", "dataset"):
                if key in node:
                    walk(node[key])
    walk(blocks)
    return out[:20]


def snippets(text: str, pattern: str, width: int = 160, limit: int = 3) -> list[str]:
    out = []
    for m in re.finditer(pattern, text, re.I):
        s, e = max(0, m.start() - width), min(len(text), m.end() + width)
        out.append(("…" if s else "") + text[s:e] + ("…" if e < len(text) else ""))
        if len(out) >= limit:
            break
    return out


def is_spa_shell(html: str) -> bool:
    text = visible_text(html)
    return len(text) < 400 or bool(re.search(r"<(app-root|div id=\"(root|app|__next)\")", html, re.I)) and len(text) < 1500


class Crawler:
    def __init__(self, start: str, max_pages: int, render: bool):
        self.start = start
        self.max_pages = max_pages
        self.robots = urllib.robotparser.RobotFileParser()
        self.robots_txt = None
        self.render_python = playwright_python() if render else None
        self.pages: dict[str, dict] = {}
        self.shell_hash: str | None = None

    def load_robots(self) -> None:
        robots_url = urljoin(self.start, "/robots.txt")
        r, err = http_get(robots_url, session=BROWSER, timeout=15)
        if r is not None and r.status_code == 200:
            self.robots_txt = r.text[:4000]
            self.robots.parse(r.text.splitlines())
        else:
            self.robots.parse([])

    def allowed(self, url: str) -> bool:
        try:
            return self.robots.can_fetch(BROWSER_UA, url)
        except Exception:  # noqa: BLE001
            return True

    def fetch_static(self, url: str) -> dict:
        r, err = http_get(url, session=BROWSER, timeout=25)
        if err:
            return {"url": url, "error": err}
        ctype = r.headers.get("content-type", "")
        rec = {"url": url, "final_url": r.url, "status": r.status_code, "content_type": ctype,
               "elapsed_ms": int(r.elapsed.total_seconds() * 1000)}
        if "html" in ctype or not ctype:
            rec["html"] = r.text[:800000]
        return rec

    def render(self, urls: list[str]) -> dict[str, dict]:
        if not self.render_python or not urls:
            return {}
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
            out = tmp.name
        cmd = [self.render_python, str(SCRIPTS / "render_pages.py"), "--urls", *urls, "--out", out]
        try:
            subprocess.run(cmd, capture_output=True, timeout=60 + 25 * len(urls), check=False)
            data = json.loads(Path(out).read_text())
            return {d["url"]: d for d in data}
        except Exception as exc:  # noqa: BLE001
            log(f"[website] render failed: {exc}")
            return {}
        finally:
            Path(out).unlink(missing_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--identity", required=True)
    ap.add_argument("--out")
    ap.add_argument("--max-pages", type=int, default=25)
    ap.add_argument("--no-render", action="store_true")
    args = ap.parse_args()

    identity = load_json(args.identity)
    start = identity["homepage"].get("final_url") or identity["input"]["url"]
    crawler = Crawler(start, args.max_pages, render=not args.no_render)
    crawler.load_robots()

    log(f"[website] homepage {start}")
    home = crawler.fetch_static(start)
    if "html" not in home:
        emit({"status": "query_failed", "error": home.get("error") or f"HTTP {home.get('status')}", "url": start}, args.out)
        return
    raw_home = home["html"]
    spa = is_spa_shell(raw_home)
    crawler.shell_hash = hashlib.md5(visible_text(raw_home).encode()).hexdigest() if spa else None
    analytics = sorted({name for name, pat in ANALYTICS.items() if re.search(pat, strip_comments(raw_home), re.I)})
    render_mode = "static"
    if spa and crawler.render_python:
        rendered = crawler.render([start]).get(start, {})
        if rendered.get("html"):
            home["html"], render_mode = rendered["html"], "rendered"
    elif spa:
        render_mode = "spa_unrendered"
    crawler.pages[start] = home

    # candidate pages: homepage links + sitemap + guessed paths
    candidates: dict[str, int] = {}
    for link in extract_links(home["html"], start):
        u = link["url"].split("#")[0]
        if same_site(u, start) and u != start:
            score = 2 * bool(URL_SCORE_RE.search(urlparse(u).path)) + bool(URL_SCORE_RE.search(link["text"]))
            candidates[u] = max(candidates.get(u, 0), score)
    sm, _ = http_get(urljoin(start, "/sitemap.xml"), session=BROWSER, timeout=15)
    if sm is not None and sm.status_code == 200 and "<loc>" in sm.text:
        for loc in re.findall(r"<loc>(.*?)</loc>", sm.text)[:500]:
            if same_site(loc, start):
                candidates[loc] = max(candidates.get(loc, 0), 2 * bool(URL_SCORE_RE.search(urlparse(loc).path)))
    for path in GUESS_PATHS:
        candidates.setdefault(urljoin(start.rstrip("/") + "/", path), 1)
    ranked = [u for u, s in sorted(candidates.items(), key=lambda kv: -kv[1]) if s > 0 and crawler.allowed(u)]
    ranked = ranked[: args.max_pages]
    skipped_by_robots = [u for u in candidates if not crawler.allowed(u)][:20]

    log(f"[website] fetching {len(ranked)} candidate pages ({render_mode})")
    static_pages = {}
    for u in ranked:
        static_pages[u] = crawler.fetch_static(u)
        time.sleep(1)
    if render_mode == "rendered":
        to_render = [u for u, p in static_pages.items() if p.get("status") == 200 and "html" in p]
        rendered = crawler.render(to_render)
        for u, rd in rendered.items():
            if rd.get("html"):
                static_pages[u]["html"] = rd["html"]
                static_pages[u]["final_url"] = rd.get("final_url") or static_pages[u].get("final_url")
    seen_hashes = {hashlib.md5(visible_text(home["html"]).encode()).hexdigest()}
    for u, p in static_pages.items():
        if p.get("status") != 200 or "html" not in p:
            continue
        h = hashlib.md5(visible_text(p["html"]).encode()).hexdigest()
        if h in seen_hashes or (crawler.shell_hash and h == crawler.shell_hash):
            continue  # SPA fallback shell or duplicate content
        seen_hashes.add(h)
        crawler.pages[u] = p

    # scan
    signals: dict[str, list] = {t: [] for t in TOPICS}
    seen_snippets: dict[str, set] = {t: set() for t in TOPICS}
    registry_links: dict[str, set] = {}
    all_jsonld, curies, lsaai = [], {}, []
    pages_out = []
    for u, p in crawler.pages.items():
        html = p["html"]
        text = visible_text(html)
        links = extract_links(html, p.get("final_url") or u)
        topics_hit = []
        for topic, (text_re, url_re) in TOPICS.items():
            # footer/nav boilerplate repeats on every page: keep each snippet/link only once per topic
            hits = [h for h in snippets(text, text_re, limit=4) if h not in seen_snippets[topic]][:2]
            link_hits = [f"{l['text'] or '(no text)'} -> {l['url']}" for l in links
                         if re.search(url_re, l["url"], re.I) or (l["text"] and re.search(text_re, l["text"], re.I))]
            link_hits = [x for x in dict.fromkeys(link_hits) if x not in seen_snippets[topic]][:4]
            seen_snippets[topic].update(hits + link_hits)
            if hits or link_hits:
                topics_hit.append(topic)
                signals[topic].append({"page": u, "page_url_matches_topic": bool(re.search(url_re, u, re.I)),
                                       "text_snippets": hits, "links": link_hits})
        for l in links:
            m = REGISTRY_LINK_RE.search(l["url"])
            if m:
                registry_links.setdefault(m.group(1).lower(), set()).add(l["url"])
            if LSAAI_RE.search(l["url"]) or LSAAI_RE.search(l["text"] or ""):
                lsaai.append({"page": u, "link": l})
        if LSAAI_RE.search(text):
            lsaai.append({"page": u, "text_snippets": snippets(text, LSAAI_RE.pattern, limit=2)})
        blocks = extract_jsonld(html)
        if blocks:
            all_jsonld.append({"page": u, "summary": jsonld_summary(blocks)})
        for prefix, _ in CURIE_RE.findall(text):
            curies[prefix] = curies.get(prefix, 0) + 1
        pages_out.append({"url": u, "final_url": p.get("final_url"), "status": p.get("status"),
                          "title": (re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I) or [None, None])[1],
                          "text_chars": len(text), "topics": topics_hit})

    # structured entry page via identifiers.org resolver (Bioschemas usually lives on entry pages)
    entry = {}
    ido = identity["matches"].get("identifiers_org", {})
    if ido.get("resolver_example"):
        r, err = http_get(ido["resolver_example"], session=BROWSER, timeout=30)
        if r is not None and r.status_code == 200:
            entry_html = r.text
            if crawler.render_python and is_spa_shell(entry_html):
                entry_html = crawler.render([r.url]).get(r.url, {}).get("html") or entry_html
            entry = {"resolver": ido["resolver_example"], "entry_url": r.url,
                     "jsonld": jsonld_summary(extract_jsonld(entry_html)),
                     "curie_prefixes": sorted({p for p, _ in CURIE_RE.findall(visible_text(entry_html))})}
            for prefix, _ in CURIE_RE.findall(visible_text(entry_html)):
                curies[prefix] = curies.get(prefix, 0) + 1
        else:
            entry = {"resolver": ido["resolver_example"], "error": err or f"HTTP {r.status_code}"}

    # content negotiation on homepage
    conneg = {}
    for accept in ("application/ld+json", "text/turtle"):
        r, err = http_get(start, headers={"Accept": accept}, session=BROWSER, timeout=20)
        conneg[accept] = r.headers.get("content-type") if r is not None else err

    # API endpoint probes (only count as evidence if not the SPA shell and not HTML error pages)
    endpoints = []
    for path in ("api", "api/", "api/docs", "swagger", "swagger-ui", "swagger-ui.html", "openapi.json", "api/openapi.json",
                 "sparql", "graphql", "ws", "rest"):
        u = urljoin(start.rstrip("/") + "/", path)
        if not crawler.allowed(u):
            continue
        r, err = http_get(u, session=BROWSER, timeout=15)
        if r is None or r.status_code >= 400:
            continue
        ctype = r.headers.get("content-type", "")
        body_hash = hashlib.md5(visible_text(r.text).encode()).hexdigest() if "html" in ctype else None
        if body_hash and body_hash in seen_hashes | {crawler.shell_hash}:
            continue
        if "json" in ctype or "swagger" in r.text[:5000].lower() or "openapi" in r.text[:5000].lower() or "sparql" in path:
            endpoints.append({"url": r.url, "status": r.status_code, "content_type": ctype, "excerpt": r.text[:300]})
    # API base URLs referenced from SPA bundles
    bundle_api_refs = set()
    if spa:
        for src in re.findall(r'<script[^>]+src="([^"]+\.js)"', raw_home)[:4]:
            js_url = urljoin(start, src)
            if not same_site(js_url, start):
                continue
            r, _ = http_get(js_url, session=BROWSER, timeout=25)
            if r is not None and r.status_code == 200:
                bundle_api_refs |= set(re.findall(r"https?://[A-Za-z0-9._-]+(?:/[A-Za-z0-9._-]+)*/(?:api|ws|rest|sparql)[A-Za-z0-9/._-]*",
                                                  r.text))
    # verify ontology prefixes against OLS
    ontologies = []
    for prefix, count in sorted(curies.items(), key=lambda kv: -kv[1])[:12]:
        data, err = get_json(f"https://www.ebi.ac.uk/ols4/api/ontologies/{prefix.lower()}", timeout=20)
        ontologies.append({"prefix": prefix, "occurrences": count, "in_ols": bool(data and not err),
                           "ols_url": f"https://www.ebi.ac.uk/ols4/ontologies/{prefix.lower()}" if data else None,
                           "title": ((data or {}).get("config") or {}).get("title")})

    out = {
        "status": "found", "generated": now_iso(), "start_url": start, "render_mode": render_mode,
        "spa_detected": spa, "playwright_python": crawler.render_python,
        "robots_txt_excerpt": crawler.robots_txt, "skipped_by_robots": skipped_by_robots,
        "homepage_elapsed_ms": home.get("elapsed_ms"), "analytics_detected": analytics,
        "pages": pages_out,
        "signals": {k: sorted(v, key=lambda x: not x["page_url_matches_topic"])[:8] for k, v in signals.items() if v},
        "registry_links": {k: sorted(v)[:10] for k, v in registry_links.items()},
        "lsaai_evidence": lsaai[:10], "jsonld": all_jsonld, "entry_page": entry,
        "content_negotiation": conneg, "api_endpoints": endpoints, "bundle_api_refs": sorted(bundle_api_refs)[:20],
        "ontology_prefixes": ontologies,
    }
    summary = {"render_mode": render_mode, "pages": len(pages_out), "topics": sorted(out["signals"]),
               "api_endpoints": len(endpoints), "jsonld_pages": len(all_jsonld), "ontologies": [o["prefix"] for o in ontologies]}
    emit(out, args.out, summary=summary)


if __name__ == "__main__":
    main()
