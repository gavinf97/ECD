from pathlib import Path

import pytest
import yaml

pytest.importorskip("openpyxl")

from common import UPTIME_ROOT, load_resources  # noqa: E402
from import_resources import DEFAULT_DIVISION, DEFAULT_MANUAL, DEFAULT_XLSX, build, write_yaml  # noqa: E402


@pytest.fixture(scope="module")
def resources():
    return build(DEFAULT_XLSX, DEFAULT_MANUAL, DEFAULT_DIVISION, existing=None)


def test_counts_and_ids(resources):
    assert len(resources) == 163
    ids = [r["id"] for r in resources]
    assert len(set(ids)) == len(ids)
    assert sum(1 for r in resources if r["source"] == DEFAULT_MANUAL.name) == 2


def test_urls_are_http(resources):
    assert all(r["url"].startswith(("http://", "https://")) for r in resources)


def test_dome_resources_present(resources):
    by_id = {r["id"]: r for r in resources}
    assert by_id["dome-registry"]["url"] == "https://registry.dome-ml.org"
    assert by_id["dome-ml"]["url"] == "https://dome-ml.org"


def test_reimport_preserves_hand_edits(tmp_path, resources):
    out = tmp_path / "resources.yml"
    write_yaml(resources, out, DEFAULT_XLSX, DEFAULT_DIVISION)
    doc = yaml.safe_load(out.read_text())
    doc["resources"][0]["enabled"] = False
    doc["resources"][0]["check"] = {"url": "https://moved.example.org/"}
    out.write_text(yaml.safe_dump(doc, sort_keys=False))

    again = build(DEFAULT_XLSX, DEFAULT_MANUAL, DEFAULT_DIVISION, existing=out)
    first = next(r for r in again if r["id"] == doc["resources"][0]["id"])
    assert first["enabled"] is False
    assert first["check"] == {"url": "https://moved.example.org/"}


def test_committed_resources_yml_is_valid():
    committed = UPTIME_ROOT / "resources.yml"
    resources = load_resources(committed)
    assert len(resources) == 163


@pytest.mark.parametrize("cell,expected", [
    ("http://www.hmtdb.uniba.it/, https://ngdc.cncb.ac.cn/databasecommons/database/id/568", "http://www.hmtdb.uniba.it/"),
    ("https://sulfatlas.sb-roscoff.fr/sulfatlas/;jsessionid=7B1B3339E8FACA2810E5ADE38489B55D?execution=e1s1",
     "https://sulfatlas.sb-roscoff.fr/sulfatlas/"),
    ("  https://www.disprot.org/ ", "https://www.disprot.org/"),
    ("https://example.org/search?q=a", "https://example.org/search?q=a"),
    (None, None),
])
def test_normalise_url(cell, expected):
    from import_resources import normalise_url
    assert normalise_url(cell) == expected
