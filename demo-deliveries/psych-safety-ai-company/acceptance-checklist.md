# Acceptance Checklist

| check | status | evidence | acceptance |
| --- | --- | --- | --- |
| Open the web demo | pass | site/index.html | Reviewer can run the 31-agent workflow without login, API key, backend, or GPU. |
| Inspect real project analysis | pass | asset-inventory.json, readiness-score.json, run-report.md | Report includes scanned assets, data profile, model route, readiness gates, and risks. |
| Verify work was executed | pass | execution-status.json, execution-log.md, executed-work/ | Every work order has owner, priority, artifact, and acceptance criteria. |
| Run client project smoke test | pass | client-project-status.json, client-project/tests/smoke_test.py | Generated client project opens and passes its deterministic smoke test. |
| Review AI delivery readiness | pass | readiness-score.json | Score, status, and each gate explain what is ready and what still needs work. |
| Confirm no unsafe training claim | pass | run-report.md, 07-training-design.md, 08-finetune-plan.md | Training or fine-tuning is only claimed when logs, commands, metrics, and data versions exist. |
