# Company OS Run Report

Generated: 2026-04-28T13:50:25.261266+00:00

## Real Work Performed

- Scanned source project files and categorized code, docs, data, and model assets.
- Profiled local CSV/spreadsheet data where available.
- Recommended a model route based on detected data and assets.
- Computed submission readiness with artifact, data, model, and security checks.
- Generated concrete cross-functional work orders with owners and acceptance criteria.
- Executed work orders into concrete files under `executed-work/`.
- Generated a runnable client project under `client-project/` and executed its smoke test.
- Wrote machine-readable evidence files for judge review.

## Asset Inventory

Total files: 314

By category:

```json
{
  "code": 158,
  "docs": 55,
  "model": 80,
  "other": 21
}
```

Notable assets:

| path | category | extension | size_bytes |
| --- | --- | --- | --- |
| evaluate_FSS.py | code | .py | 9413 |
| evaluate_VOC.py | code | .py | 10158 |
| evaluate_segmentation.py | code | .py | 6631 |
| feature_matching\dinov2\run\train\train.py | code | .py | 1665 |
| feature_matching\dinov2\train\train.py | code | .py | 10681 |
| feature_matching\test.py | code | .py | 3786 |
| feature_matching\train.py | code | .py | 10681 |
| test.sh | code | .sh | 934 |
| train_DQN.py | code | .py | 15731 |
| train\20250417_2229\episode_results\training_log.txt | docs | .txt | 47838 |
| train\20250420_1947\episode_results\training_log.txt | docs | .txt | 15433 |
| train\20250420_2053\episode_results\training_log.txt | docs | .txt | 10742 |
| train\20250420_2054\episode_results\training_log.txt | docs | .txt | 31745 |
| train\20250420_2316\episode_results\training_log.txt | docs | .txt | 31185 |
| train\20250422_0908\episode_results\training_log.txt | docs | .txt | 276883 |


## Data Profiling

No rows.


## Model Route Recommendation

Primary route: **Product workflow and data acquisition first**

Reason: No clearly profiled text dataset was found.

Fine-tune position: Not first step; local model artifacts detected

```json
{
  "has_labeled_text_data": false,
  "sampled_rows": 0,
  "labeled_text_rows": 0,
  "model_assets_detected": true,
  "training_scripts_detected": true
}
```

## Readiness Score

Score: **85/100**

Status: **strong**

| check | score | detail |
| --- | --- | --- |
| company_artifacts | 20 | 30/30 numbered company artifacts exist |
| placeholder_cleanliness | 15 | no placeholders found |
| real_asset_inventory | 15 | 158 code files and 55 docs detected |
| data_profile | 0 | no profileable data file found |
| model_route | 15 | Product workflow and data acquisition first |
| security_scan | 20 | no secret patterns detected |


## Concrete Work Orders

| department | owner | priority | action |
| --- | --- | --- | --- |
| Product | Product Manager Agent | P0 | Convert the target workflow into demo acceptance criteria and non-goals. |
| Technology | Chief Architect Agent | P0 | Keep the browser demo and local Python runner as separate, reproducible execution paths. |
| Data | Data Governance Agent | P1 | Create a schema/data-card update from profiled data and mark missing label or text columns. |
| AI Platform | Model Analyst Agent | P0 | Execute the recommended route: Product workflow and data acquisition first. |
| AI Platform | Training Architect Agent | P1 | Turn training into an experiment matrix with data version, command, metric, budget, and rollback. |
| MLOps | MLOps Platform Agent | P1 | Register detected model artifacts and connect them to configs, metrics, and release status. |
| Security | Legal & Compliance Counsel | P1 | Review and remove secret patterns or private files before submission. |
| Submission | Judge Summary Agent | P0 | Prepare the judge walkthrough around the website, GPO case, run-report, readiness score, and work orders. |


## Plan Execution Status

Execution status: **executed**

| department | owner | status | artifact |
| --- | --- | --- | --- |
| Product | Product Manager Agent | executed | executed-work\01-product-product-manager-agent.md |
| Technology | Chief Architect Agent | executed | executed-work\02-technology-chief-architect-agent.md |
| Data | Data Governance Agent | executed | executed-work\03-data-data-governance-agent.md |
| AI Platform | Model Analyst Agent | executed | executed-work\04-ai-platform-model-analyst-agent.md |
| AI Platform | Training Architect Agent | executed | executed-work\05-ai-platform-training-architect-agent.md |
| MLOps | MLOps Platform Agent | executed | executed-work\06-mlops-mlops-platform-agent.md |
| Security | Legal & Compliance Counsel | executed | executed-work\07-security-legal-compliance-counsel.md |
| Submission | Judge Summary Agent | executed | executed-work\08-submission-judge-summary-agent.md |


## Client Project Delivery

Client project status: **passed**

Entry: `client-project/index.html`

Smoke test: `C:\Users\10084\anaconda3\python.exe tests/smoke_test.py` returned `0`.
