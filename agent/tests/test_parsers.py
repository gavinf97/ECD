from check_eligibility import matches
from fair_check import parse_metrics
from inspect_repo import name_token_match


def test_fair_metrics_mapped_by_position_when_ids_missing():
    rows = [{"http://www.w3.org/ns/dqv#isMeasurementOf": [{"@id": "https://x/eval/None"}],
             "http://www.w3.org/ns/dqv#value": [{"@value": 2}]} for _ in range(12)]
    rows.append({"@id": "https://x/assessment/1"})  # non-measurement node
    parsed = parse_metrics(rows)
    assert [r["metric"] for r in parsed][:3] == ["F1A", "F1B", "F2A"]
    assert len(parsed) == 12 and all(r["metric_id_inferred_by_position"] for r in parsed)


def test_fair_metrics_named():
    rows = [{"http://www.w3.org/ns/dqv#isMeasurementOf": [{"@id": f"https://x/eval/{m}"}],
             "http://www.w3.org/ns/dqv#value": [{"@value": 1}]} for m in ("R11", "F1A", "I2")]
    assert [r["metric"] for r in parse_metrics(rows)] == ["F1A", "I2", "R11"]


def test_eligibility_matching():
    aliases = {"disprot"}
    assert "homepage_domain" in matches({"name": "Database of protein disorder", "url": "http://www.disprot.org/"},
                                        "DisProt", "https://disprot.org/", aliases)
    assert "name" in matches({"name": "DisProt", "url": None}, "DisProt", "https://disprot.org/", aliases)
    assert matches({"name": "MobiDB", "url": "https://mobidb.org"}, "DisProt", "https://disprot.org/", aliases) == []


def test_container_name_match_is_strict():
    assert name_token_match("DisProt", "biocomputingup/disprot")
    assert name_token_match("DisProt", "disprot-api")
    assert not name_token_match("DisProt", "jhuguco/disprotime-devutils")
