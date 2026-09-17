import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


@pytest.fixture()
def answers(tmp_path):
    path = tmp_path / "answers.json"
    subprocess.run([sys.executable, str(SCRIPTS / "answers.py"), "init", "--answers", str(path), "--name", "TestDB",
                    "--url", "https://testdb.example.org"], check=True, capture_output=True)
    doc = json.loads(path.read_text())
    doc["answers"]["S7.2"].update(choice="Yes", links=["https://registry.identifiers.org/registry/testdb"], status="verified",
                                  confidence="high", evidence=[{"source": "identifiers.org",
                                                                "url": "https://registry.identifiers.org/registry/testdb",
                                                                "snippet": "prefix testdb"}])
    doc["answers"]["S5.4"].update(choice="Yes", list=["REST API: https://testdb.example.org/api"], status="verified",
                                  evidence=[{"source": "website", "url": "https://testdb.example.org/api"}])
    doc["answers"]["S2.1a"].update(text="TestDB fills a gap <with> & special characters.", status="inferred")
    path.write_text(json.dumps(doc))
    return path


@pytest.mark.parametrize("formats", ["json,md,html,docx"])
def test_render_formats(answers, tmp_path, formats):
    out = tmp_path / "out"
    proc = subprocess.run([sys.executable, str(SCRIPTS / "render_outputs.py"), "--answers", str(answers), "--outdir", str(out),
                           "--formats", formats], capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    for ext in formats.split(","):
        assert (out / f"ECD_testdb_checklist.{ext}").stat().st_size > 500
    html = (out / "ECD_testdb_checklist.html").read_text()
    assert "&lt;with&gt;" in html                      # autoescaped
    assert "Section 8: Final Declaration" in html
    assert "Appendix 1" not in html                      # not a reapplication
    md = (out / "ECD_testdb_checklist.md").read_text()
    assert "REST API: https://testdb.example.org/api" in md


def test_render_pdf(answers, tmp_path):
    out = tmp_path / "out"
    proc = subprocess.run([sys.executable, str(SCRIPTS / "render_outputs.py"), "--answers", str(answers), "--outdir", str(out),
                           "--formats", "pdf", "--submission-copy"], capture_output=True, text=True, timeout=300)
    assert proc.returncode == 0, proc.stderr
    pdf = out / "ECD_testdb_checklist_submission.pdf"
    assert pdf.read_bytes()[:4] == b"%PDF"
