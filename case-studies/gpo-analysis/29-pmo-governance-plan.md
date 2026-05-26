# 29 Pmo Governance Plan

Project: gpo-analysis

Goal: Analyze the local GPO computer vision project as an AI company delivery case.

Owner: PMO Governance Agent

Purpose: Cross-functional roadmap, meeting cadence, risk tracking, and decision governance.

## Executive Decision

| Decision | Conservative Starter Choice | Evidence Needed | Owner |
| --- | --- | --- | --- |
| Primary direction | Build a stable CPU-first demo and evidence package before heavy infrastructure | User goal, constraints, generated artifacts | PMO Governance Agent |

## Required Analysis

- What this function must decide.
- What evidence it needs.
- What artifact or metric proves progress.
- What risk blocks release.
- What next team receives as handoff.

## Handoff Contract

| Sends To | Handoff |
| --- | --- |
| Executive Command | Decision summary and blockers |
| Product & Market | User, value, launch, or support implications |
| AI R&D Platform | Data, model, evaluation, release, or safety implications |
| Delivery & Story | Judge-facing proof and demo evidence |

## Completion Gate

This artifact is complete only when a reviewer can identify the decision, evidence, owner, blocker, and next action.

<!-- COMPANY_OS:Action Plan:START -->
## Company OS Findings: Action Plan

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
<!-- COMPANY_OS:Action Plan:END -->

<!-- COMPANY_OS:Executed Work:START -->
## Company OS Findings: Executed Work

| department | owner | priority | status | artifact |
| --- | --- | --- | --- | --- |
| Product | Product Manager Agent | P0 | executed | executed-work\01-product-product-manager-agent.md |
| Technology | Chief Architect Agent | P0 | executed | executed-work\02-technology-chief-architect-agent.md |
| Data | Data Governance Agent | P1 | executed | executed-work\03-data-data-governance-agent.md |
| AI Platform | Model Analyst Agent | P0 | executed | executed-work\04-ai-platform-model-analyst-agent.md |
| AI Platform | Training Architect Agent | P1 | executed | executed-work\05-ai-platform-training-architect-agent.md |
| MLOps | MLOps Platform Agent | P2 | executed | executed-work\06-mlops-mlops-platform-agent.md |
| Security | Legal & Compliance Counsel | P1 | executed | executed-work\07-security-legal-compliance-counsel.md |
| Submission | Judge Summary Agent | P0 | executed | executed-work\08-submission-judge-summary-agent.md |
<!-- COMPANY_OS:Executed Work:END -->



