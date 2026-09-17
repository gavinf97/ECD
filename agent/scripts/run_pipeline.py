#!/usr/bin/env python3
"""
run_pipeline.py — runs Phases 2-4a of the ECD Agent Skill in one command.

  2   resolve_resource.py                       -> identity.json
  3a  query_registries.py all  ||  probe_website.py            (parallel)
  3b  inspect_repo.py  ||  fair_check.py  ||  check_eligibility.py (parallel; need 3a)
  4a  answers.py init (if absent)  +  propose_answers.py        -> answers.json, proposals.json, digest.md

Each step's exit code, duration and stdout summary go to WORKDIR/pipeline_log.json; a failing
step never stops the others (its evidence file simply reports query_failed / is missing).

Usage:
    python run_pipeline.py --name "DisProt" --url https://disprot.org
                           [--repo URL] [--community NAME] [--reapplication]
                           [--workdir DIR] [--services-xlsx PATH] [--no-render] [--skip-fair-api]
Default workdir: ./ecd-assessments/<slug>-<YYYYMMDD>
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import log, now_iso, slugify, write_json  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent
PY = sys.executable


def run(label: str, cmd: list[str], timeout: int) -> dict:
    log(f"[pipeline] ▶ {label}")
    t0 = time.time()
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        rec = {"step": label, "exit": proc.returncode, "seconds": round(time.time() - t0, 1),
               "stdout_tail": proc.stdout.strip()[-1200:], "stderr_tail": proc.stderr.strip()[-800:] if proc.returncode else None}
    except subprocess.TimeoutExpired:
        rec = {"step": label, "exit": "timeout", "seconds": round(time.time() - t0, 1)}
    log(f"[pipeline] ✔ {label} (exit {rec['exit']}, {rec['seconds']} s)")
    return rec


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--repo")
    ap.add_argument("--community")
    ap.add_argument("--reapplication", action="store_true")
    ap.add_argument("--workdir")
    ap.add_argument("--services-xlsx")
    ap.add_argument("--no-render", action="store_true", help="do not render SPA pages with Playwright")
    ap.add_argument("--skip-fair-api", action="store_true")
    args = ap.parse_args()

    wd = Path(args.workdir or Path.cwd() / "ecd-assessments" / f"{slugify(args.name)}-{datetime.now():%Y%m%d}")
    ev = wd / "evidence"
    ev.mkdir(parents=True, exist_ok=True)
    ident = str(wd / "identity.json")
    steps = []

    resolve = [PY, str(SCRIPTS / "resolve_resource.py"), "--name", args.name, "--url", args.url, "--out", ident]
    if args.repo:
        resolve += ["--repo", args.repo]
    steps.append(run("resolve_resource", resolve, 300))
    if not Path(ident).exists():
        write_json(wd / "pipeline_log.json", {"finished": now_iso(), "steps": steps})
        sys.exit("resolve_resource failed; see pipeline_log.json")

    website = [PY, str(SCRIPTS / "probe_website.py"), "--identity", ident, "--out", str(ev / "website.json")]
    if args.no_render:
        website.append("--no-render")
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(run, "query_registries", [PY, str(SCRIPTS / "query_registries.py"), "all", "--identity", ident,
                                                         "--evidence-dir", str(ev)], 900),
                   pool.submit(run, "probe_website", website, 1200)]
        steps += [f.result() for f in futures]

    fair = [PY, str(SCRIPTS / "fair_check.py"), "--identity", ident, "--website", str(ev / "website.json"),
            "--out", str(ev / "fairchecker.json"), "--png", str(wd / "fairchecker.png")]
    if args.skip_fair_api:
        fair.append("--skip-api")
    repo = [PY, str(SCRIPTS / "inspect_repo.py"), "--identity", ident, "--website", str(ev / "website.json"), "--out", str(ev / "repo.json")]
    if args.repo:
        repo += ["--repo", args.repo]
    elig = [PY, str(SCRIPTS / "check_eligibility.py"), "--identity", ident, "--evidence-dir", str(ev), "--out", str(ev / "eligibility.json")]
    if args.services_xlsx:
        elig += ["--services-xlsx", args.services_xlsx]
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(run, "inspect_repo", repo, 600), pool.submit(run, "fair_check", fair, 1200),
                   pool.submit(run, "check_eligibility", elig, 300)]
        steps += [f.result() for f in futures]

    answers = wd / "answers.json"
    if not answers.exists():
        init = [PY, str(SCRIPTS / "answers.py"), "init", "--answers", str(answers), "--name", args.name, "--url", args.url]
        if args.community:
            init += ["--community", args.community]
        if args.reapplication:
            init.append("--reapplication")
        steps.append(run("answers_init", init, 60))
    steps.append(run("propose_answers", [PY, str(SCRIPTS / "propose_answers.py"), "--workdir", str(wd)], 120))

    write_json(wd / "pipeline_log.json", {"finished": now_iso(), "workdir": str(wd), "steps": steps})
    print(json.dumps({"workdir": str(wd), "digest": str(wd / "digest.md"), "proposals": str(wd / "proposals.json"),
                      "answers": str(answers),
                      "steps": {s["step"]: s["exit"] for s in steps}}, indent=2))


if __name__ == "__main__":
    main()
