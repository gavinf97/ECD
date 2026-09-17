#!/usr/bin/env python3
"""
inspect_repo.py — Phase 3 (software evidence) of the ECD Agent Skill.

Inspects the resource's code repository for Checklist Section 6 (software) and
Section 4 hints: licence (S6.6), open source (S6.8), containers (S6.7),
software management plan files (S6.5), release cadence / milestones (S4.1,
S6.4), issue tracker as feedback channel (S4.2/S4.3), contributor counts and
concentration (hints only for S4.5 FTE and S4.8 bus factor), Software Heritage
archival.

Metadata only — no cloning, no walking beyond the root tree listing.
GitHub auth: $GITHUB_TOKEN, else `gh auth token` if the gh CLI is logged in,
else unauthenticated (60 requests/hour).

If identity.json has no repository, searches GitHub for repos whose name or
homepage matches the resource and returns them as *candidates* needing
confirmation (never auto-selected).

Usage:
    python inspect_repo.py --identity WORKDIR/identity.json --out WORKDIR/evidence/repo.json [--repo URL]
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import domain_of, emit, get_json, load_json, log, norm_name, now_iso, result, same_site  # noqa: E402

GH = "https://api.github.com"
SMP_FILES = re.compile(r"^(CONTRIBUTING|CODE_OF_CONDUCT|GOVERNANCE|ROADMAP|CHANGELOG|CHANGES|HISTORY|RELEASE|SECURITY|"
                       r"CITATION\.cff|codemeta\.json|SMP|software[-_ ]management[-_ ]plan|MAINTAINERS|SUPPORT)(\.[a-z]+)?$", re.I)
CONTAINER_FILES = re.compile(r"^(Dockerfile(\..*)?|docker-compose\.ya?ml|compose\.ya?ml|Containerfile|Singularity(\..*)?|.*\.def|"
                             r"apptainer\.def|helm|charts|kubernetes|k8s|\.devcontainer)$", re.I)
OSI_LICENSES = {"MIT", "Apache-2.0", "GPL-2.0", "GPL-3.0", "LGPL-2.1", "LGPL-3.0", "BSD-2-Clause", "BSD-3-Clause", "MPL-2.0",
                "AGPL-3.0", "EPL-2.0", "EUPL-1.2", "ISC", "Artistic-2.0", "CECILL-2.1", "GPL-2.0-only", "GPL-3.0-only",
                "GPL-3.0-or-later", "AGPL-3.0-only", "LGPL-3.0-only", "0BSD", "Unlicense"}


def gh_headers() -> dict:
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        try:
            token = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip() or None
        except Exception:  # noqa: BLE001
            token = None
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def gh(path: str, headers: dict, params: dict | None = None):
    return get_json(f"{GH}{path}", headers=headers, params=params, timeout=30)


def inspect_github(owner: str, repo: str, headers: dict) -> dict:
    meta, err = gh(f"/repos/{owner}/{repo}", headers)
    if err:
        return result("query_failed" if "404" not in err else "not_found", error=err, url=f"https://github.com/{owner}/{repo}")
    full = meta["full_name"]
    out = {
        "url": meta["html_url"], "description": meta.get("description"), "homepage": meta.get("homepage"),
        "private": meta.get("private"), "archived": meta.get("archived"), "fork": meta.get("fork"),
        "license_spdx": (meta.get("license") or {}).get("spdx_id"), "license_name": (meta.get("license") or {}).get("name"),
        "created_at": meta.get("created_at"), "pushed_at": meta.get("pushed_at"), "default_branch": meta.get("default_branch"),
        "stars": meta.get("stargazers_count"), "forks": meta.get("forks_count"), "topics": meta.get("topics"),
        "has_issues": meta.get("has_issues"), "open_issues_count": meta.get("open_issues_count"),
        "language": meta.get("language"),
    }
    out["open_source"] = bool(not meta.get("private") and out["license_spdx"] and out["license_spdx"] != "NOASSERTION")
    out["osi_license"] = out["license_spdx"] in OSI_LICENSES

    tree, _ = gh(f"/repos/{full}/contents/", headers)
    root_files = [x["name"] for x in tree or [] if isinstance(x, dict)]
    out["root_files"] = root_files[:80]
    out["smp_related_files"] = [f for f in root_files if SMP_FILES.match(f)]
    out["container_files"] = [f for f in root_files if CONTAINER_FILES.match(f)]
    wf, _ = gh(f"/repos/{full}/contents/.github/workflows", headers)
    out["ci_workflows"] = [x["name"] for x in wf or [] if isinstance(x, dict)]

    releases, _ = gh(f"/repos/{full}/releases", headers, {"per_page": 30})
    out["releases"] = [{"tag": r.get("tag_name"), "published_at": r.get("published_at")} for r in releases or []][:15]
    tags, _ = gh(f"/repos/{full}/tags", headers, {"per_page": 30})
    out["tag_count_first_page"] = len(tags or [])
    milestones, _ = gh(f"/repos/{full}/milestones", headers, {"state": "all", "per_page": 20})
    out["milestones"] = [{"title": m.get("title"), "state": m.get("state"), "due_on": m.get("due_on")} for m in milestones or []]
    closed_issues, _ = get_json(f"{GH}/search/issues", headers=headers,
                                params={"q": f"repo:{full} is:issue is:closed", "per_page": 1}, timeout=30)
    out["closed_issues_total"] = (closed_issues or {}).get("total_count")

    contributors, _ = gh(f"/repos/{full}/contributors", headers, {"per_page": 100, "anon": "false"})
    contrib = [(c.get("login"), c.get("contributions", 0)) for c in contributors or [] if isinstance(c, dict)]
    total = sum(n for _, n in contrib) or 1
    out["contributors_total"] = len(contrib)
    out["top_contributor_share"] = round(contrib[0][1] / total, 2) if contrib else None
    since = (datetime.now(timezone.utc) - timedelta(days=365)).isoformat()
    commits, _ = gh(f"/repos/{full}/commits", headers, {"since": since, "per_page": 100})
    recent = Counter(((c.get("author") or {}).get("login") or (c.get("commit", {}).get("author") or {}).get("name"))
                     for c in commits or [] if isinstance(c, dict))
    out["commits_last_12_months_first_page"] = sum(recent.values())
    out["active_committers_last_12_months"] = len(recent)
    out["recent_commit_concentration"] = round(recent.most_common(1)[0][1] / sum(recent.values()), 2) if recent else None

    pkgs, _ = gh(f"/orgs/{owner}/packages", headers, {"package_type": "container"})
    out["ghcr_packages"] = [p.get("name") for p in pkgs or [] if isinstance(p, dict)][:20]

    swh, swh_err = get_json(f"https://archive.softwareheritage.org/api/1/origin/{quote(out['url'], safe='')}/get/", timeout=30)
    out["software_heritage"] = {"archived": bool(swh and not swh_err),
                                "url": f"https://archive.softwareheritage.org/browse/origin/?origin_url={out['url']}" if swh else None}
    return result("found", **out)


def search_candidates(name: str, url: str, headers: dict, owners_hint: set[str]) -> list[dict]:
    queries = [f"{name} in:name", f"{domain_of(url)} in:description,readme"]
    queries += [f"user:{o} {name}" for o in sorted(owners_hint)[:3]]
    seen: dict[str, dict] = {}
    for q in queries:
        data, err = get_json(f"{GH}/search/repositories", headers=headers, params={"q": q, "per_page": 10}, timeout=30)
        for item in (data or {}).get("items", []):
            basis = []
            if item.get("homepage") and same_site(item["homepage"], url):
                basis.append("homepage_domain")
            if norm_name(name) in norm_name(item["name"]):
                basis.append("name_in_repo")
            if item["owner"]["login"].lower() in {o.lower() for o in owners_hint}:
                basis.append("owner_linked_from_site")
            if basis:
                seen.setdefault(item["html_url"], {"url": item["html_url"], "match_basis": basis, "stars": item.get("stargazers_count"),
                                                   "description": item.get("description"), "pushed_at": item.get("pushed_at")})
    return sorted(seen.values(), key=lambda c: (len(c["match_basis"]), c["stars"] or 0), reverse=True)[:10]


def name_token_match(name: str, repo: str | None) -> bool:
    """True when the image/repo name (last path part) is the resource name, optionally with a -suffix."""
    part = re.split(r"[/:]", repo or "")[-1].lower()
    target = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return part == target or part.startswith(target + "-") or part.startswith(target + "_") or norm_name(part) == norm_name(name)


def search_container_registries(name: str) -> dict:
    out = {}
    data, err = get_json("https://hub.docker.com/v2/search/repositories/", params={"query": name, "page_size": 10}, timeout=30)
    out["dockerhub"] = [{"repo": r.get("repo_name"), "description": r.get("short_description"), "pulls": r.get("pull_count"),
                         "url": f"https://hub.docker.com/r/{r.get('repo_name')}"} for r in (data or {}).get("results", [])
                        if name_token_match(name, r.get("repo_name"))] if not err else {"error": err}
    data, err = get_json("https://quay.io/api/v1/find/repositories", params={"query": name}, timeout=30)
    out["quay"] = [{"repo": f"{r.get('namespace', {}).get('name')}/{r.get('name')}", "url": f"https://quay.io/repository/{r.get('namespace', {}).get('name')}/{r.get('name')}"}
                   for r in (data or {}).get("results", []) if name_token_match(name, r.get("name"))][:10] if not err else {"error": err}
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--identity", required=True)
    ap.add_argument("--repo", help="override repository URL")
    ap.add_argument("--website", help="website.json (optional) to harvest GitHub owners linked from the site")
    ap.add_argument("--out")
    args = ap.parse_args()
    identity = load_json(args.identity)
    name, url = identity["input"]["name"], identity["input"]["url"]
    headers = gh_headers()
    repo_url = args.repo or identity.get("chosen_repo")

    owners_hint = set()
    web_path = Path(args.website) if args.website else Path(args.identity).parent / "evidence" / "website.json"
    if web_path.exists():
        web = load_json(web_path)
        for link in (web.get("registry_links") or {}).get("github.com", []):
            m = re.search(r"github\.com/([^/]+)", link)
            if m:
                owners_hint.add(m.group(1))

    out = {"generated": now_iso(), "authenticated": "Authorization" in headers,
           "container_registries": search_container_registries(name)}
    if repo_url and "github.com" in repo_url:
        m = re.search(r"github\.com/([^/]+)/([^/#?]+)", repo_url)
        log(f"[repo] inspecting {m.group(1)}/{m.group(2)}")
        out["repo"] = inspect_github(m.group(1), m.group(2).removesuffix(".git"), headers)
        out["status"] = out["repo"]["status"]
    elif repo_url:
        out["repo"] = result("skipped", url=repo_url, note="Non-GitHub host: inspect manually (licence file, Dockerfile, releases).")
        out["status"] = "skipped"
    else:
        log("[repo] no repository known; searching GitHub for candidates")
        cands = search_candidates(name, url, headers, owners_hint)
        out["status"] = "not_found"
        out["candidates"] = cands
        out["note"] = ("No repository was linked from registries or the homepage. Candidates below need user confirmation "
                       "before any S6.6-S6.8 answer uses them; an unconfirmed repo must not be treated as the resource's code.")
    emit(out, args.out, summary={"status": out["status"], "repo": (out.get("repo") or {}).get("url"),
                                 "candidates": [c["url"] for c in out.get("candidates", [])][:5]})


if __name__ == "__main__":
    main()
