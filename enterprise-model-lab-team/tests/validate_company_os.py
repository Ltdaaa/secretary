"""Validate that the AI company OS can do real project work."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    repo_root = skill_dir.parent
    script = skill_dir / "scripts" / "company_os.py"
    assert script.exists(), "company_os.py must exist"

    with tempfile.TemporaryDirectory() as tmp:
        workspace = Path(tmp) / "workspace"
        create_cmd = [
            sys.executable,
            str(skill_dir / "scripts" / "create_workspace.py"),
            "--name",
            "test-ai-company",
            "--goal",
            "Build a working AI company OS test package.",
            "--output",
            str(workspace),
        ]
        subprocess.run(create_cmd, check=True, capture_output=True, text=True, encoding="utf-8")

        project_dir = workspace / "test-ai-company"
        run_cmd = [
            sys.executable,
            str(script),
            "--workspace",
            str(project_dir),
            "--source",
            str(repo_root),
        ]
        result = subprocess.run(run_cmd, check=True, capture_output=True, text=True, encoding="utf-8")
        assert "Readiness score" in result.stdout
        second_result = subprocess.run(run_cmd, check=True, capture_output=True, text=True, encoding="utf-8")
        assert "Readiness score" in second_result.stdout

        inventory = project_dir / "asset-inventory.json"
        readiness = project_dir / "readiness-score.json"
        action_plan = project_dir / "action-plan.json"
        work_orders = project_dir / "work-orders.md"
        execution_status = project_dir / "execution-status.json"
        execution_log = project_dir / "execution-log.md"
        client_project_status = project_dir / "client-project-status.json"
        client_project = project_dir / "client-project"
        capability_matrix = project_dir / "capability-matrix.md"
        acceptance_checklist = project_dir / "acceptance-checklist.md"
        next_execution_plan = project_dir / "next-execution-plan.md"
        report = project_dir / "run-report.md"
        assert inventory.exists(), "asset-inventory.json was not generated"
        assert readiness.exists(), "readiness-score.json was not generated"
        assert action_plan.exists(), "action-plan.json was not generated"
        assert work_orders.exists(), "work-orders.md was not generated"
        assert execution_status.exists(), "execution-status.json was not generated"
        assert execution_log.exists(), "execution-log.md was not generated"
        assert client_project_status.exists(), "client-project-status.json was not generated"
        assert client_project.exists(), "client-project was not generated"
        assert capability_matrix.exists(), "capability-matrix.md was not generated"
        assert acceptance_checklist.exists(), "acceptance-checklist.md was not generated"
        assert next_execution_plan.exists(), "next-execution-plan.md was not generated"
        assert report.exists(), "run-report.md was not generated"

        inventory_data = json.loads(inventory.read_text(encoding="utf-8"))
        readiness_data = json.loads(readiness.read_text(encoding="utf-8"))
        action_plan_data = json.loads(action_plan.read_text(encoding="utf-8"))
        execution_status_data = json.loads(execution_status.read_text(encoding="utf-8"))
        client_project_status_data = json.loads(client_project_status.read_text(encoding="utf-8"))
        report_text = report.read_text(encoding="utf-8")
        work_orders_text = work_orders.read_text(encoding="utf-8")
        execution_log_text = execution_log.read_text(encoding="utf-8")
        capability_text = capability_matrix.read_text(encoding="utf-8")
        acceptance_text = acceptance_checklist.read_text(encoding="utf-8")
        next_plan_text = next_execution_plan.read_text(encoding="utf-8")

        assert inventory_data["summary"]["total_files"] > 0
        assert ".py" in inventory_data["by_extension"]
        assert readiness_data["score"] >= 50
        assert len(action_plan_data) >= 6
        assert execution_status_data["status"] == "executed"
        assert execution_status_data["executed_orders"] == len(action_plan_data)
        for result_item in execution_status_data["results"]:
            assert (project_dir / result_item["artifact"]).exists(), f"missing executed artifact: {result_item['artifact']}"
        assert client_project_status_data["status"] == "passed"
        assert client_project_status_data["smoke_test"]["returncode"] == 0
        assert (client_project / "index.html").exists()
        assert (client_project / "tests" / "smoke_test.py").exists()
        assert "Run Delivery App" in (client_project / "index.html").read_text(encoding="utf-8")
        assert "Company OS Work Orders" in work_orders_text
        assert "Company OS Execution Log" in execution_log_text
        assert "Real Work Performed" in report_text
        assert "Asset Inventory" in report_text
        assert "Model Route Recommendation" in report_text
        assert "Concrete Work Orders" in report_text
        assert "Plan Execution Status" in report_text
        assert "Client Project Delivery" in report_text
        assert "Judge-Proof Summary" in report_text
        assert "Capability Matrix" in report_text
        assert "Acceptance Checklist" in report_text
        assert "Next Execution Plan" in report_text
        assert "Project asset scan" in capability_text
        assert "Runnable client delivery" in capability_text
        assert "Run client project smoke test" in acceptance_text
        assert "Judge Summary Agent" in next_plan_text

    print("enterprise-model-lab-team company_os validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
