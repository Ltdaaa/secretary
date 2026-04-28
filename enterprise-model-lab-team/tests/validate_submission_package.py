"""Audit the final submission folder and ZIP package.

This is intentionally broader than unit tests: it checks package structure,
security exclusions, generated work evidence, case-study links, and obvious
mojibake before a hackathon upload.
"""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "SUBMISSION_CHECKLIST.md",
    "DEPLOYMENT.md",
    "enterprise-model-lab-team/SKILL.md",
    "enterprise-model-lab-team/scripts/create_workspace.py",
    "enterprise-model-lab-team/scripts/company_os.py",
    "enterprise-model-lab-team/tests/validate_skill.py",
    "enterprise-model-lab-team/tests/validate_company_os.py",
    "enterprise-model-lab-team/tests/validate_site.py",
    "enterprise-model-lab-team/tests/validate_site_runtime.js",
    "site/index.html",
    "site/case-studies/gpo-analysis.html",
    "demo-deliveries/psych-safety-ai-company/run-report.md",
    "demo-deliveries/psych-safety-ai-company/asset-inventory.json",
    "demo-deliveries/psych-safety-ai-company/readiness-score.json",
    "demo-deliveries/psych-safety-ai-company/action-plan.json",
    "demo-deliveries/psych-safety-ai-company/work-orders.md",
    "demo-deliveries/psych-safety-ai-company/execution-status.json",
    "demo-deliveries/psych-safety-ai-company/execution-log.md",
    "demo-deliveries/psych-safety-ai-company/executed-work/01-product-product-manager-agent.md",
    "demo-deliveries/psych-safety-ai-company/client-project-status.json",
    "demo-deliveries/psych-safety-ai-company/client-project/index.html",
    "demo-deliveries/psych-safety-ai-company/client-project/project-manifest.json",
    "demo-deliveries/psych-safety-ai-company/client-project/tests/smoke_test.py",
    "case-studies/gpo-analysis/run-report.md",
    "case-studies/gpo-analysis/action-plan.json",
    "case-studies/gpo-analysis/work-orders.md",
    "case-studies/gpo-analysis/execution-status.json",
    "case-studies/gpo-analysis/execution-log.md",
    "case-studies/gpo-analysis/client-project-status.json",
    "case-studies/gpo-analysis/client-project/index.html",
]

SECRET_RE = re.compile(r"sk-[A-Za-z0-9_-]{20,}|BEGIN (RSA|OPENSSH|PRIVATE) KEY")
BAD_TEXT_RE = re.compile(r"\ufffd|涓|鍚|鐨|鈥|銆")
HREF_RE = re.compile(r'href="([^"#]+)"')


def assert_path(root: Path, relative: str) -> None:
    path = root / relative
    assert path.exists(), f"missing required package path: {relative}"


def check_no_sensitive_files(root: Path) -> None:
    hits = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        parts = {part.lower() for part in path.parts}
        if path.name == "auth.json" or ".codex" in parts or path.suffix.lower() in {".key", ".pem"}:
            hits.append(str(path))
    assert not hits, f"sensitive files must not be submitted: {hits}"


def check_secret_patterns(root: Path) -> None:
    hits = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".py", ".js", ".html", ".json", ".yaml", ".yml", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if SECRET_RE.search(text):
            hits.append(str(path))
    assert not hits, f"secret-like patterns found: {hits}"


def check_no_mojibake(root: Path) -> None:
    hits = []
    for relative in ["README.md", "SUBMISSION_CHECKLIST.md", "DEPLOYMENT.md", "site/index.html", "site/case-studies/gpo-analysis.html"]:
        path = root / relative
        text = path.read_text(encoding="utf-8", errors="ignore")
        if BAD_TEXT_RE.search(text):
            hits.append(relative)
    assert not hits, f"possible mojibake found in user-facing files: {hits}"


def check_case_links(root: Path) -> None:
    case_page = root / "site" / "case-studies" / "gpo-analysis.html"
    text = case_page.read_text(encoding="utf-8")
    missing = []
    for href in HREF_RE.findall(text):
        if href.startswith(("http:", "https:", "mailto:", "javascript:")):
            continue
        target = (case_page.parent / href).resolve()
        if not target.exists():
            missing.append(href)
    assert not missing, f"broken case-study links: {missing}"


def check_zip(zip_path: Path, root: Path) -> None:
    assert zip_path.exists(), f"missing ZIP package: {zip_path}"
    with zipfile.ZipFile(zip_path) as archive:
        names = {name.replace("\\", "/") for name in archive.namelist()}
    for relative in REQUIRED_PATHS:
        assert relative in names, f"ZIP missing required path: {relative}"
    bad_names = [name for name in names if name.endswith("auth.json") or ".codex/" in name or name.endswith((".key", ".pem"))]
    assert not bad_names, f"ZIP contains sensitive paths: {bad_names}"
    folder_files = {str(path.relative_to(root)).replace("\\", "/") for path in root.rglob("*") if path.is_file()}
    missing_from_zip = sorted(path for path in REQUIRED_PATHS if path in folder_files and path not in names)
    assert not missing_from_zip, f"folder and ZIP mismatch: {missing_from_zip}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission", default="submission-ready")
    parser.add_argument("--zip", default="enterprise-model-lab-team-submission.zip")
    args = parser.parse_args()

    root = Path(args.submission).resolve()
    zip_path = Path(args.zip).resolve()
    assert root.exists(), f"missing submission folder: {root}"

    for relative in REQUIRED_PATHS:
        assert_path(root, relative)
    check_no_sensitive_files(root)
    check_secret_patterns(root)
    check_no_mojibake(root)
    check_case_links(root)
    check_zip(zip_path, root)

    print("enterprise-model-lab-team submission package audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
