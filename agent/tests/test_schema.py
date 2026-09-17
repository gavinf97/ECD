"""The schema must stay faithful to the Checklist PDF text (references/ecd_checklist_v1_text.txt)."""
import re

from common import REFERENCES, iter_questions, load_schema


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower().replace("’", "'")).strip()


def test_ids_unique_and_count():
    ids = [q["id"] for _, q in iter_questions(load_schema())]
    assert len(ids) == len(set(ids))
    assert len(ids) == 75


def test_option_sets_exist():
    schema = load_schema()
    for _, q in iter_questions(schema):
        choice = q["parts"].get("choice")
        if choice:
            assert choice["option_set"] in schema["option_sets"], q["id"]


def test_prompts_appear_in_checklist_text_in_order():
    source = norm((REFERENCES / "ecd_checklist_v1_text.txt").read_text())
    # Skip the preamble (section list) so positions refer to the question body
    body_start = source.find("applicant details submitter s name")
    assert body_start > 0
    last = body_start
    for section, q in iter_questions(load_schema()):
        if q["id"] in ("S1.confirm", "S8.declaration") or section["id"] == "APX1":
            continue
        probe = norm(q["prompt"])[:45]
        pos = source.find(probe, body_start)
        assert pos >= 0, f"{q['id']} prompt not found in checklist text: {probe!r}"
        assert pos >= last - 400, f"{q['id']} appears out of order"
        last = max(last, pos)


def test_word_limits_match_source():
    schema = load_schema()
    limits = {q["id"]: (q["parts"].get("text") or {}).get("word_limit") for _, q in iter_questions(schema)}
    assert limits["S3.3"] == 150
    assert limits["S2.1a"] == 100
