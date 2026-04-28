"""Validate the static web demo has the required usable features."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_SNIPPETS = [
    "启动 31-Agent 完整公司团队",
    "Agent 队列",
    "实时协作日志",
    "部门作战室",
    "部门详情",
    "交付物详情",
    "交付物工作台",
    "artifactDetailView",
    "showArtifactDetail",
    "downloadArtifactDoc",
    "artifactDoc",
    "department-card",
    "showDepartment",
    "departmentAgents",
    "下载总报告",
    "下载交付包",
    "下载证据 JSON",
    "运行功能自检",
    "落地自检",
    "执行能力",
    "客户成品",
    "client-project-status.json",
    "execution-status.json",
    "csvParse",
    "analyzeRows",
    "selfTestChecks",
    "buildEvidence",
    "buildArtifacts",
    "artifactRecommendation",
    "case-studies/gpo-analysis.html",
    "Media & Communications Agent",
    "Sales & Business Development Agent",
    "HR & Talent Agent",
    "PMO Governance Agent",
    "Chief Architect Agent",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="site")
    args = parser.parse_args()

    site = Path(args.site)
    index = site / "index.html"
    case = site / "case-studies" / "gpo-analysis.html"
    assert index.exists(), f"missing {index}"
    assert case.exists(), f"missing {case}"

    html = index.read_text(encoding="utf-8")
    missing = [snippet for snippet in REQUIRED_SNIPPETS if snippet not in html]
    assert not missing, f"missing web demo features: {missing}"

    assert html.count("artifact:") >= 30, "expected at least 30 agent artifact definitions"
    assert "new Blob([\"\\ufeff\" + content]" in html, "downloads must include UTF-8 BOM"
    assert "type=\"file\"" in html, "CSV upload input missing"
    assert "window.location.href = \"case-studies/gpo-analysis.html\"" in html, "GPO case link missing"
    assert "escapeHtml" in html, "uploaded CSV values must be HTML-escaped before rendering"
    assert "agent-company-evidence.json" in html, "JSON evidence export missing"
    case_html = case.read_text(encoding="utf-8")
    assert "work-orders.md" in case_html, "GPO case should expose concrete work orders"
    assert "execution-log.md" in case_html, "GPO case should expose executed work evidence"
    assert "client-project/index.html" in case_html, "GPO case should expose generated client project"

    print("enterprise-model-lab-team site validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
