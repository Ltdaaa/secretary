"""Create an Enterprise Model Lab Team delivery workspace.

This script has no third-party dependencies. It creates a reproducible folder
with the standard artifacts required by the Fortune-500-style AI company skill.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ARTIFACTS = [
    ("00-company-charter.md", "CEO Strategy Commander", "Company mission, strategic bet, constraints, success metrics, and executive decision log."),
    ("01-market-opportunity.md", "Market Intelligence Agent", "Target market, buyer, competitor map, positioning, and why-now argument."),
    ("02-product-requirements.md", "Product Manager Agent", "PRD, user workflow, feature priority, acceptance criteria, and non-goals."),
    ("03-user-research.md", "User Research Agent", "Personas, jobs-to-be-done, pain points, assumptions, and validation tasks."),
    ("23-ux-design-plan.md", "UX Design Agent", "Interaction design, information architecture, accessibility, and demo usability."),
    ("20-technology-architecture.md", "Chief Architect Agent", "System architecture, module boundaries, integration contracts, and technical tradeoffs."),
    ("21-product-engineering-plan.md", "Full-stack Product Engineer Agent", "Web app, API surface, frontend/backend handoff, and user workflow implementation plan."),
    ("22-platform-reliability-plan.md", "Platform Reliability Agent", "Runtime reliability, observability, deployment, incident response, and operational readiness."),
    ("24-api-integration-plan.md", "API Integration Engineer Agent", "External API, local tool, data connector, and integration contract plan."),
    ("04-data-map.md", "Data Intelligence Agent", "Candidate data sources, licenses, fields, volume, quality, and gaps."),
    ("05-data-card.md", "Data Governance Agent", "Schema, cleaning rules, dedupe rules, splits, labels, and data risks."),
    ("06-model-selection.md", "Model Analyst Agent", "Candidate model matrix, baseline choice, cost, latency, and risk."),
    ("07-training-design.md", "Training Architect Agent", "Training route, experiment matrix, compute budget, rollback plan."),
    ("08-finetune-plan.md", "Fine-tuning Engineer Agent", "SFT/LoRA/DPO decision, data mix, hyperparameters, expected gains."),
    ("09-evaluation-protocol.md", "Evaluation & Test Agent", "Metrics, test sets, red-team cases, thresholds, regression checks."),
    ("10-mlops-release-plan.md", "MLOps Platform Agent", "Model registry, release, monitoring, incident response, and rollback plan."),
    ("11-risk-register.md", "Safety & Responsible AI Agent", "Privacy, IP, bias, misuse, and model safety risks with mitigations."),
    ("12-agent-product-spec.md", "Agent Engineer Agent", "Skill/tool interface, commands, dependencies, and user workflow."),
    ("13-growth-operations-plan.md", "Growth & Operations Agent", "Launch motion, activation, retention, analytics, and feedback loop."),
    ("25-media-communications-plan.md", "Media & Communications Agent", "Press narrative, social media content, community updates, and public communication plan."),
    ("26-sales-business-plan.md", "Sales & Business Development Agent", "Buyer map, sales motion, partnerships, pricing hypothesis, and pilot conversion plan."),
    ("27-partnerships-ecosystem-plan.md", "Partnerships & Ecosystem Agent", "Technology partners, data partners, ecosystem channels, and co-build opportunities."),
    ("14-customer-success-plan.md", "Customer Success Agent", "Onboarding, support, user education, feedback routing, and escalation."),
    ("28-hr-talent-plan.md", "HR & Talent Agent", "Team roles, hiring plan, capability gaps, and operating rituals."),
    ("29-pmo-governance-plan.md", "PMO Governance Agent", "Cross-functional roadmap, meeting cadence, risk tracking, and decision governance."),
    ("15-finance-resource-plan.md", "CFO Resource Analyst", "API, GPU, storage, engineering budget, unit economics, and ROI assumptions."),
    ("16-legal-compliance-review.md", "Legal & Compliance Counsel", "Data license, privacy, copyright, regulatory, and submission compliance review."),
    ("17-brand-demo-playbook.md", "Brand & Demo Agent", "Brand narrative, website copy, demo script, judge Q&A, and presentation arc."),
    ("18-executive-dashboard.md", "Executive Dashboard Agent", "Company KPI dashboard, milestone health, risks, and board-level status."),
    ("19-judge-summary.md", "Judge Summary Agent", "Submission story, proof points, limitations, and next roadmap."),
]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff_-]+", "-", value.strip()).strip("-")
    return slug or "ai-company-project"


def render_template(text: str, name: str, goal: str) -> str:
    return text.replace("{{PROJECT_NAME}}", name).replace("{{PROJECT_GOAL}}", goal)


def write_if_missing(path: Path, content: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def artifact_content(filename: str, owner: str, purpose: str, project_name: str, goal: str) -> str:
    title = filename.removesuffix(".md").replace("-", " ").title()
    return f"""# {title}

Project: {project_name}

Goal: {goal}

Owner: {owner}

Purpose: {purpose}

## Executive Decision

| Decision | Conservative Starter Choice | Evidence Needed | Owner |
| --- | --- | --- | --- |
| Primary direction | Build a stable CPU-first demo and evidence package before heavy infrastructure | User goal, constraints, generated artifacts | {owner} |

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
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an Enterprise Model Lab Team workspace.")
    parser.add_argument("--name", required=True, help="Project name, for example psych-safety-ai-company.")
    parser.add_argument("--goal", required=True, help="One-sentence project goal.")
    parser.add_argument("--output", default="model-lab-delivery", help="Output root directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    project_name = slugify(args.name)
    root = Path(args.output) / project_name
    root.mkdir(parents=True, exist_ok=True)

    skill_dir = Path(__file__).resolve().parents[1]
    template_dir = skill_dir / "templates"

    created = []
    for template_name in ["project-brief.yaml", "delivery-board.md", "evaluation-rubric.md"]:
        template = (template_dir / template_name).read_text(encoding="utf-8")
        if write_if_missing(root / template_name, render_template(template, project_name, args.goal), args.force):
            created.append(template_name)

    for filename, owner, purpose in ARTIFACTS:
        content = artifact_content(filename, owner, purpose, project_name, args.goal)
        if write_if_missing(root / filename, content, args.force):
            created.append(filename)

    print(f"Workspace: {root}")
    print(f"Created or updated: {len(created)} file(s)")
    for item in created:
        print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
