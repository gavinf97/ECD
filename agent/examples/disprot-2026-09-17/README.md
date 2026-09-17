# Worked example — DisProt (17 September 2026)

End-to-end run of the ECD Agent Skill on https://disprot.org, produced to test the skill:

- `run_pipeline.py`
- Claude's review patch
- `answers.py validate`
- `render_outputs.py`

The applicant Q&A (Phase 6) was **not** run, so 28 items remain `[Applicant to complete]`.

**Result:** 23 verified, 17 inferred and 28 needing applicant input.

**Eligibility:** DisProt already holds **ELIXIR Deposition Database (EDD)** status. That makes Section 1 item 4 "Not met", a Hub-level rejection under Process Appendix 3, so DisProt would not be eligible for ECD. It stays a good test case because it is thoroughly registered.

| File | What |
|---|---|
| `digest.md` | Evidence digest Claude reviewed (Phase 4) |
| `ECD_disprot_checklist.{md,html,docx,pdf,json}` | Rendered checklist with evidence |
| `fairchecker.png` | FAIR-Checker result screenshot (91.67 %) |
