"""Lightweight validation for the Enterprise Model Lab Team skill."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path


REQUIRED_ARTIFACTS = [
    "project-brief.yaml",
    "delivery-board.md",
    "evaluation-rubric.md",
    "00-company-charter.md",
    "01-market-opportunity.md",
    "02-product-requirements.md",
    "03-user-research.md",
    "23-ux-design-plan.md",
    "20-technology-architecture.md",
    "21-product-engineering-plan.md",
    "22-platform-reliability-plan.md",
    "24-api-integration-plan.md",
    "04-data-map.md",
    "05-data-card.md",
    "06-model-selection.md",
    "07-training-design.md",
    "08-finetune-plan.md",
    "09-evaluation-protocol.md",
    "10-mlops-release-plan.md",
    "11-risk-register.md",
    "12-agent-product-spec.md",
    "13-growth-operations-plan.md",
    "25-media-communications-plan.md",
    "26-sales-business-plan.md",
    "27-partnerships-ecosystem-plan.md",
    "14-customer-success-plan.md",
    "28-hr-talent-plan.md",
    "29-pmo-governance-plan.md",
    "15-finance-resource-plan.md",
    "16-legal-compliance-review.md",
    "17-brand-demo-playbook.md",
    "18-executive-dashboard.md",
    "19-judge-summary.md",
]


REQUIRED_TERMS = [
    "CEO Strategy Commander",
    "Product Manager Agent",
    "User Research Agent",
    "UX Design Agent",
    "Growth & Operations Agent",
    "Media & Communications Agent",
    "Sales & Business Development Agent",
    "Partnerships & Ecosystem Agent",
    "Customer Success Agent",
    "HR & Talent Agent",
    "PMO Governance Agent",
    "Chief Architect Agent",
    "Full-stack Product Engineer Agent",
    "Platform Reliability Agent",
    "API Integration Engineer Agent",
    "CFO Resource Analyst",
    "Legal & Compliance Counsel",
    "Data Intelligence Agent",
    "Model Analyst Agent",
    "Fine-tuning Engineer Agent",
    "Evaluation & Test Agent",
    "MLOps Platform Agent",
]


def parse_frontmatter(skill_text: str) -> dict[str, str]:
    match = re.match(r"---\n(.*?)\n---", skill_text, flags=re.S)
    if not match:
        raise AssertionError("SKILL.md is missing YAML frontmatter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    skill_file = skill_dir / "SKILL.md"
    skill_text = skill_file.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_text)

    assert (skill_dir / "scripts" / "company_os.py").exists()
    assert frontmatter.get("name") == "enterprise-model-lab-team"
    assert frontmatter.get("description", "").startswith("Use when")
    assert re.fullmatch(r"[A-Za-z0-9-]+", frontmatter["name"])
    for term in REQUIRED_TERMS:
        assert term in skill_text, f"Missing required role: {term}"

    with tempfile.TemporaryDirectory() as tmp:
        cmd = [
            sys.executable,
            str(skill_dir / "scripts" / "create_workspace.py"),
            "--name",
            "psych-safety-ai-company",
            "--goal",
            "Design a Fortune-500-style AI company workflow.",
            "--output",
            tmp,
        ]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True, encoding="utf-8")
        assert "Created or updated" in result.stdout
        workspace = Path(tmp) / "psych-safety-ai-company"
        missing = [name for name in REQUIRED_ARTIFACTS if not (workspace / name).exists()]
        assert not missing, f"Missing generated files: {missing}"

    print("enterprise-model-lab-team validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
