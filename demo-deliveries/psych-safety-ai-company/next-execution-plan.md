# Next Execution Plan

| step | owner | command_or_action | expected_output |
| --- | --- | --- | --- |
| 1 | PMO Governance Agent | Review acceptance-checklist.md and close any review/blocker items. | Signed acceptance status and updated delivery-board.md |
| 2 | Data Governance Agent | If data is missing, add a labeled CSV with text and label columns, then rerun company_os.py. | Updated data-card, route evidence, and readiness score |
| 3 | Model Analyst Agent | Execute route decision: Product workflow and data acquisition first | Baseline metric table and failure analysis before any fine-tune decision |
| 4 | Full-stack Product Engineer Agent | Open client-project/index.html and verify the generated customer workflow. | Runnable customer artifact and deployment handoff |
| 5 | Judge Summary Agent | Use run-report.md, capability-matrix.md, and execution-status.json for the final walkthrough. | Three-minute judge narrative backed by generated evidence |
| 6 | COO Program Officer | Resolve capability blockers: Data profiling | Readiness moves beyond current 85/100 score |
