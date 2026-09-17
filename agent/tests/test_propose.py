"""propose_answers.py on a minimal synthetic evidence set (offline)."""
import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


def write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))


def build_workdir(tmp_path: Path, site_down: bool) -> Path:
    wd = tmp_path / "wd"
    identity = {
        "input": {"name": "TestDB", "url": "https://testdb.example.org"},
        "homepage": {"status": "query_failed" if site_down else "found", "final_url": "https://testdb.example.org/",
                     "error": "ConnectTimeout" if site_down else None},
        "matches": {
            "bioregistry": {"status": "found", "best": {"id": "testdb", "mappings": {}}},
            "identifiers_org": {"status": "not_found", "tried_prefixes": ["testdb"]},
            "re3data": {"status": "not_found"}, "biotools": {"status": "not_found"},
            "fairsharing": {"status": "found", "id": "FAIRsharing.abc123", "url": "https://fairsharing.org/FAIRsharing.abc123",
                            "match_basis": ["bioregistry_mapping"]},
            "uniprot_xref": {"status": "not_found"}, "openebench": {"status": "not_found"},
        },
        "repositories": [], "chosen_repo": None, "needs_confirmation": [],
    }
    write(wd / "identity.json", identity)
    ev = wd / "evidence"
    png = wd / "fairchecker.png"
    png.write_bytes(b"\x89PNG\r\n")
    write(ev / "fairchecker.json", {"screenshot": {"status": "ok", "png": str(png)},
                                     "metric_scores": [{"metric": m, "score": 0 if site_down else 2} for m in
                                                       ["F1A", "F1B", "F2A", "F2B", "A11", "A12", "I1", "I2", "I3", "R11", "R12", "R13"]],
                                     "assessment_url": "https://fair-checker.france-bioinformatique.fr/assessment/x"})
    write(ev / "website.json", {"status": "query_failed", "error": "ConnectTimeout"} if site_down else {
        "status": "found", "start_url": "https://testdb.example.org/", "analytics_detected": [],
        "signals": {"privacy": [{"page": "https://testdb.example.org/privacy", "page_url_matches_topic": True,
                                 "text_snippets": ["Privacy notice: this privacy notice explains ..."], "links": []}]},
        "jsonld": [], "entry_page": {}, "api_endpoints": [], "ontology_prefixes": [], "registry_links": {}, "pages": []})
    write(ev / "eligibility.json", {"holds_existing_status": ["Core Data Resource (CDR)"],
                                     "status_match": {"cdr": {"label": "Core Data Resource (CDR)", "matched": True,
                                                              "hits": [{"name": "TestDB", "match_basis": ["name"]}],
                                                              "source_url": "https://elixir-europe.org/platforms/data/core-data-resources"}},
                                     "sdp_match": {"listed": False, "hits": [], "nodes": []}, "node_match": {}})
    write(ev / "registry_tess.json", {"status": "not_found", "materials": {"status": "not_found", "items": []},
                                       "events": {"status": "not_found", "items": []}})
    return wd


def run(wd: Path) -> dict:
    subprocess.run([sys.executable, str(SCRIPTS / "propose_answers.py"), "--workdir", str(wd)], check=True, capture_output=True)
    return json.loads((wd / "proposals.json").read_text())


def test_proposals_site_up(tmp_path):
    p = run(build_workdir(tmp_path, site_down=False))
    assert p["S7.1"]["choice"] == "Yes" and p["S7.1"]["status"] == "verified"
    assert p["S7.2"]["choice"] == "No" and p["S7.2"]["status"] == "not_found"      # conclusive registry miss
    assert p["S7.4"]["choice"] == "No"
    assert p["S1.4"]["choice"] == "Not met"                                          # already a CDR -> Hub rejection
    assert p["S4.10"]["choice"] == "Yes"
    assert p["S7.8"]["status"] == "inferred" and p["S7.8"]["image"]
    assert p["S8.declaration"]["status"] == "needs_applicant"
    assert "choice" not in p["S1.2"]                                                 # SDP miss never becomes "Not met"
    assert "website unreachable" not in (build := (tmp_path / "wd" / "digest.md").read_text())


def test_proposals_site_down(tmp_path):
    wd = build_workdir(tmp_path, site_down=True)
    p = run(wd)
    assert p["S7.8"]["status"] == "needs_applicant" and "unreachable" in p["S7.8"]["hint"]
    assert "WARNING — website unreachable" in (wd / "digest.md").read_text()
    assert p["S4.10"]["status"] == "needs_applicant"                                 # absence of crawl != No
