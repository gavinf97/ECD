#!/usr/bin/env python3
"""
render_pages.py — optional headless-browser helper for the ECD Agent Skill.

Many biodata resources are single-page apps (Angular/React/Vue) whose static
HTML contains almost no text or links, so probe_website.py delegates to this
script to obtain rendered DOM HTML. fair_check.py uses it to screenshot the
FAIR-Checker result (Checklist S7.8).

Requires Playwright (`pip install playwright && playwright install chromium`).
It runs under whichever Python has Playwright: the current interpreter if it can
import playwright, otherwise the interpreter named in $ECD_PLAYWRIGHT_PYTHON
(callers handle that choice via `playwright_python()`).

Usage:
    python render_pages.py --urls https://a.org https://a.org/about --out rendered.json [--wait-ms 2500]
    python render_pages.py --screenshot URL --png out.png [--wait-selector CSS] [--timeout-ms 180000]
                           [--fill-selector CSS --fill-value TEXT] [--click-selector CSS]
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys


def playwright_python() -> str | None:
    """Return a Python executable that can import playwright, or None."""
    try:
        import playwright  # noqa: F401
        return sys.executable
    except ImportError:
        pass
    candidate = os.environ.get("ECD_PLAYWRIGHT_PYTHON")
    if candidate and shutil.which(candidate) or (candidate and os.path.exists(candidate)):
        ok = subprocess.run([candidate, "-c", "import playwright"], capture_output=True).returncode == 0
        return candidate if ok else None
    return None


def render(urls: list[str], wait_ms: int, max_chars: int) -> list[dict]:
    from playwright.sync_api import sync_playwright
    out = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                             "Chrome/126.0 Safari/537.36 ECDAgentSkill/0.1")
        page = ctx.new_page()
        for url in urls:
            rec = {"url": url}
            try:
                resp = page.goto(url, wait_until="domcontentloaded", timeout=45000)
                try:
                    page.wait_for_load_state("networkidle", timeout=wait_ms + 8000)
                except Exception:  # noqa: BLE001 — some SPAs never go idle
                    page.wait_for_timeout(wait_ms)
                rec.update(final_url=page.url, status=resp.status if resp else None, title=page.title(),
                           html=page.content()[:max_chars])
            except Exception as exc:  # noqa: BLE001
                rec["error"] = f"{type(exc).__name__}: {exc}"
            out.append(rec)
        browser.close()
    return out


def screenshot(url: str, png: str, wait_selector: str | None, timeout_ms: int,
               fill_selector: str | None = None, fill_value: str | None = None,
               click_selector: str | None = None) -> dict:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 1000})
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            if fill_selector and fill_value:
                field = page.locator(fill_selector).first
                field.click()
                field.press_sequentially(fill_value, delay=20)  # fires input events that enable submit buttons
            if click_selector:
                page.locator(click_selector).first.click(timeout=30000)
            if wait_selector:
                page.wait_for_selector(wait_selector, timeout=timeout_ms)
            else:
                page.wait_for_load_state("networkidle", timeout=timeout_ms)
            page.screenshot(path=png, full_page=True)
            return {"status": "ok", "png": png, "final_url": page.url, "title": page.title(),
                    "text_excerpt": page.inner_text("body")[:6000],
                    "links": page.eval_on_selector_all("a[href], textarea, code", "els => els.map(e => e.href || e.textContent).slice(0, 200)")}
        except Exception as exc:  # noqa: BLE001
            try:
                page.screenshot(path=png, full_page=True)
            except Exception:  # noqa: BLE001
                png = None
            return {"status": "error", "error": f"{type(exc).__name__}: {exc}", "png": png}
        finally:
            browser.close()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--urls", nargs="*")
    ap.add_argument("--out")
    ap.add_argument("--wait-ms", type=int, default=2500)
    ap.add_argument("--max-chars", type=int, default=600000)
    ap.add_argument("--screenshot")
    ap.add_argument("--png")
    ap.add_argument("--wait-selector")
    ap.add_argument("--timeout-ms", type=int, default=180000)
    ap.add_argument("--fill-selector", help="CSS selector of an input to fill before waiting (e.g. a URL box)")
    ap.add_argument("--fill-value")
    ap.add_argument("--click-selector", help="CSS selector of a button to click after filling")
    args = ap.parse_args()
    try:
        import playwright  # noqa: F401
    except ImportError:
        print(json.dumps({"error": "playwright not importable in this interpreter"}))
        sys.exit(1)
    if args.screenshot:
        data = screenshot(args.screenshot, args.png or "screenshot.png", args.wait_selector, args.timeout_ms,
                          args.fill_selector, args.fill_value, args.click_selector)
    else:
        data = render(args.urls or [], args.wait_ms, args.max_chars)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
        print(json.dumps({"written": args.out}))
    else:
        print(json.dumps(data))


if __name__ == "__main__":
    main()
