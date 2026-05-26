# Company OS Work Orders

| department | owner | priority | action | acceptance |
| --- | --- | --- | --- | --- |
| Product | Product Manager Agent | P0 | Convert the target workflow into demo acceptance criteria and non-goals. | A judge can run one primary workflow end to end without reading source code. |
| Technology | Chief Architect Agent | P0 | Keep the browser demo and local Python runner as separate, reproducible execution paths. | Static website works without API keys; local runner writes machine-readable evidence files. |
| Data | Data Governance Agent | P1 | Create a schema/data-card update from profiled data and mark missing label or text columns. | Text column, label column, empty counts, and split strategy are explicit before training claims. |
| AI Platform | Model Analyst Agent | P0 | Execute the recommended route: Product workflow and data acquisition first. | Baseline choice, metric, failure mode, and rollback rule are written before fine-tuning. |
| AI Platform | Training Architect Agent | P1 | Turn training into an experiment matrix with data version, command, metric, budget, and rollback. | Every experiment row has a reproducible command or is explicitly marked as future work. |
| MLOps | MLOps Platform Agent | P2 | Register detected model artifacts and connect them to configs, metrics, and release status. | Each model/checkpoint has owner, source, metric, version, and rollback notes. |
| Security | Legal & Compliance Counsel | P1 | Review and remove secret patterns or private files before submission. | Submission package contains no auth.json, .codex folder, API key, private key, or private dataset. |
| Submission | Judge Summary Agent | P0 | Prepare the judge walkthrough around the website, GPO case, run-report, readiness score, and work orders. | A 3-minute path shows input, multi-agent work, real evidence, and downloadable outputs. |
