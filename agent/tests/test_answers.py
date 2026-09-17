import json
import subprocess
import sys
from pathlib import Path

from answers import validate

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


def make_doc(tmp_path: Path) -> Path:
    path = tmp_path / "answers.json"
    subprocess.run([sys.executable, str(SCRIPTS / "answers.py"), "init", "--answers", str(path),
                    "--name", "TestDB", "--url", "https://testdb.example.org"], check=True, capture_output=True)
    return path


def load(path):
    return json.loads(Path(path).read_text())


def test_init_creates_all_records(tmp_path):
    doc = load(make_doc(tmp_path))
    assert len(doc["answers"]) == 75
    assert doc["answers"]["APP.resource_url"]["links"] == ["https://testdb.example.org"]


def test_yes_without_evidence_is_error(tmp_path):
    doc = load(make_doc(tmp_path))
    doc["answers"]["S7.2"].update(choice="Yes", status="verified")
    assert any("without any evidence URL" in e for e in validate(doc)["errors"])


def test_no_on_failed_query_is_error(tmp_path):
    doc = load(make_doc(tmp_path))
    doc["answers"]["S7.4"].update(choice="No", status="query_failed")
    assert any("failed query" in e for e in validate(doc)["errors"])


def test_word_limit_and_invalid_option(tmp_path):
    doc = load(make_doc(tmp_path))
    doc["answers"]["S2.1a"].update(text="word " * 101, status="inferred")
    doc["answers"]["S2.2"].update(choice="Ages ago", status="inferred")
    errors = validate(doc)["errors"]
    assert any("S2.1a" in e and "limit 100" in e for e in errors)
    assert any("S2.2" in e and "not in option set" in e for e in errors)


def test_declarations_must_come_from_applicant(tmp_path):
    doc = load(make_doc(tmp_path))
    doc["answers"]["S8.declaration"].update(choice="agree", status="inferred")
    assert any("S8.declaration" in e for e in validate(doc)["errors"])


def test_patch_skips_internal_keys(tmp_path):
    path = make_doc(tmp_path)
    patch = tmp_path / "patch.json"
    patch.write_text(json.dumps({"S7.2": {"choice": "Yes", "links": ["https://registry.identifiers.org/registry/x"],
                                          "status": "verified", "confidence": "high", "_proposed_by": "x",
                                          "evidence": [{"source": "identifiers.org", "url": "https://registry.identifiers.org/registry/x"}]}}))
    subprocess.run([sys.executable, str(SCRIPTS / "answers.py"), "patch", "--answers", str(path), "--patch", str(patch)],
                   check=True, capture_output=True)
    rec = load(path)["answers"]["S7.2"]
    assert "_proposed_by" not in rec and rec["choice"] == "Yes"
    assert validate(load(path))["valid"]


def test_strict_requires_resolution(tmp_path):
    doc = load(make_doc(tmp_path))
    report = validate(doc, strict=True)
    assert not report["valid"] and not report["ready_to_submit"]
