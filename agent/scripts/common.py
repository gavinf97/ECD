"""
common.py — shared helpers for the ECD Agent Skill scripts.

Conventions (mirroring dome-agent-skill):
  - log() writes progress to stderr; stdout carries JSON only.
  - Every script accepts --out FILE; emit() writes JSON there and prints a
    compact summary (or the full JSON when no --out is given).
  - Network failures are never swallowed into "not found": results carry an
    explicit status of "found" | "not_found" | "query_failed".
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

SKILL_ROOT = Path(__file__).resolve().parent.parent
REFERENCES = SKILL_ROOT / "references"
CACHE_DIR = Path(os.environ.get("ECD_CACHE_DIR", Path.home() / ".cache" / "ecd-agent-skill"))

USER_AGENT = "ECDAgentSkill/0.1 (+https://doi.org/10.5281/zenodo.17289009)"
BROWSER_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
DEFAULT_TIMEOUT = 25


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def today() -> str:
    return datetime.now().strftime("%d-%m-%Y")


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "resource"


def create_session(max_retries: int = 3, backoff_factor: float = 1.0,
                   user_agent: str = USER_AGENT) -> requests.Session:
    """Retrying session (pattern from dome-triage EpmcClient.create_session)."""
    session = requests.Session()
    retry = Retry(total=max_retries, backoff_factor=backoff_factor,
                  status_forcelist=[429, 500, 502, 503, 504], allowed_methods=["GET", "HEAD"])
    adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=20)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers["User-Agent"] = user_agent
    return session


SESSION = create_session()


def http_get(url: str, *, params: Optional[dict] = None, headers: Optional[dict] = None,
             timeout: int = DEFAULT_TIMEOUT, session: Optional[requests.Session] = None,
             allow_redirects: bool = True) -> tuple[Optional[requests.Response], Optional[str]]:
    """GET returning (response, error). Error is set only on transport failure."""
    s = session or SESSION
    try:
        r = s.get(url, params=params, headers=headers, timeout=timeout, allow_redirects=allow_redirects)
        return r, None
    except requests.RequestException as exc:
        return None, f"{type(exc).__name__}: {exc}"


def get_json(url: str, *, params: Optional[dict] = None, headers: Optional[dict] = None,
             timeout: int = DEFAULT_TIMEOUT) -> tuple[Any, Optional[str]]:
    """GET and decode JSON; returns (data, error)."""
    h = {"Accept": "application/json"}
    h.update(headers or {})
    r, err = http_get(url, params=params, headers=h, timeout=timeout)
    if err:
        return None, err
    if r.status_code != 200:
        return None, f"HTTP {r.status_code} from {r.url}"
    try:
        return r.json(), None
    except ValueError:
        return None, f"Non-JSON response from {r.url}"


def wayback_get(url: str, timeout: int = 90) -> tuple[Optional[str], Optional[str], Optional[str]]:
    """Fetch the latest Wayback Machine snapshot of url.
    Returns (html, snapshot_url, error). Used for sites that block non-browser clients
    (elixir-europe.org returns 403 to scripted requests)."""
    # A timestamp of "now" makes Wayback redirect to the closest (i.e. latest) capture;
    # the id_ suffix returns the original bytes without the Wayback toolbar.
    wb = f"https://web.archive.org/web/{datetime.now().strftime('%Y%m%d%H%M%S')}id_/{url}"
    r, err = http_get(wb, timeout=timeout)
    if err:
        return None, None, err
    if r.status_code != 200 or "Temporarily Offline" in r.text[:2000]:
        return None, None, f"Wayback HTTP {r.status_code}"
    return r.text, r.url, None


def domain_of(url: str) -> str:
    host = urlparse(url if "://" in url else f"https://{url}").netloc.lower()
    return host[4:] if host.startswith("www.") else host


def same_site(url_a: str, url_b: str) -> bool:
    a, b = domain_of(url_a), domain_of(url_b)
    return bool(a and b) and (a == b or a.endswith("." + b) or b.endswith("." + a))


def norm_name(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (text or "").lower())


def evidence(source: str, url: Optional[str], snippet: Optional[str] = None, **extra: Any) -> dict:
    rec = {"source": source, "url": url, "snippet": (snippet or "")[:400] or None, "retrieved": now_iso()}
    rec.update({k: v for k, v in extra.items() if v is not None})
    return rec


def result(status: str, **data: Any) -> dict:
    """status: found | not_found | query_failed | skipped"""
    return {"status": status, **data}


def load_json(path: os.PathLike | str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: os.PathLike | str, data: Any) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)


def emit(data: Any, out: Optional[str], summary: Optional[str] = None) -> None:
    """Write JSON to --out (printing a compact summary) or print the JSON itself."""
    if out:
        write_json(out, data)
        print(json.dumps({"written": out, "summary": summary}, ensure_ascii=False) if summary
              else json.dumps({"written": out}))
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def fail(message: str, out: Optional[str] = None) -> None:
    payload = {"error": message}
    if out:
        write_json(out, payload)
    print(json.dumps(payload))
    sys.exit(1)


def cached_download(url: str, name: str, max_age_days: float = 7, timeout: int = 120) -> tuple[Optional[Path], Optional[str]]:
    """Download url into the cache dir unless a fresh copy exists."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / name
    if path.exists() and (time.time() - path.stat().st_mtime) < max_age_days * 86400:
        return path, None
    r, err = http_get(url, timeout=timeout)
    if err or r is None or r.status_code != 200:
        if path.exists():
            log(f"[cache] refresh failed ({err or r.status_code}); using stale {path}")
            return path, None
        return None, err or f"HTTP {r.status_code}"
    path.write_bytes(r.content)
    return path, None


def load_schema() -> dict:
    return load_json(REFERENCES / "ecd_checklist_schema_v1.json")


def iter_questions(schema: dict):
    for section in schema["sections"]:
        for q in section["questions"]:
            yield section, q


def load_reference_lists() -> dict:
    path = REFERENCES / "elixir_reference_lists.json"
    return load_json(path) if path.exists() else {}
