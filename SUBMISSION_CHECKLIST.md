# Submission Checklist

## 必交内容

- [x] `enterprise-model-lab-team/SKILL.md`
- [x] `enterprise-model-lab-team/scripts/create_workspace.py`
- [x] `enterprise-model-lab-team/scripts/company_os.py`
- [x] `enterprise-model-lab-team/templates/`
- [x] `enterprise-model-lab-team/examples/`
- [x] `enterprise-model-lab-team/tests/validate_skill.py`
- [x] `enterprise-model-lab-team/tests/validate_company_os.py`
- [x] `enterprise-model-lab-team/tests/validate_site.py`
- [x] `enterprise-model-lab-team/tests/validate_site_runtime.js`
- [x] `enterprise-model-lab-team/tests/validate_submission_package.py`
- [x] `demo-deliveries/psych-safety-ai-company/`
- [x] `demo-deliveries/psych-safety-ai-company/run-report.md`
- [x] `demo-deliveries/psych-safety-ai-company/asset-inventory.json`
- [x] `demo-deliveries/psych-safety-ai-company/readiness-score.json`
- [x] `demo-deliveries/psych-safety-ai-company/action-plan.json`
- [x] `demo-deliveries/psych-safety-ai-company/work-orders.md`
- [x] `demo-deliveries/psych-safety-ai-company/execution-status.json`
- [x] `demo-deliveries/psych-safety-ai-company/execution-log.md`
- [x] `demo-deliveries/psych-safety-ai-company/executed-work/`
- [x] `demo-deliveries/psych-safety-ai-company/client-project-status.json`
- [x] `demo-deliveries/psych-safety-ai-company/client-project/`
- [x] `site/index.html`
- [x] `site/case-studies/gpo-analysis.html`
- [x] `DEPLOYMENT.md`
- [x] `docs/hackathon/champion-execution-plan.md`
- [x] `README.md`

## 提交前检查

```powershell
python enterprise-model-lab-team\tests\validate_skill.py
python enterprise-model-lab-team\tests\validate_company_os.py
python enterprise-model-lab-team\tests\validate_site.py --site site
node enterprise-model-lab-team\tests\validate_site_runtime.js site
python enterprise-model-lab-team\tests\validate_submission_package.py --submission submission-ready --zip enterprise-model-lab-team-submission.zip
rg -n "auth.json|api_key|API_KEY|sk-|token" README.md SUBMISSION_CHECKLIST.md enterprise-model-lab-team docs demo-deliveries
```

第二条命令不应出现真实密钥或认证文件内容。

## 不要上传

- `C:\Users\10084\.codex\auth.json`
- `.codex/`
- `__pycache__/`
- `*.pyc`
- 私人 API key
- 未脱敏数据

## 推荐提交名称

`enterprise-model-lab-team`

## 推荐一句话介绍

一支模拟世界 500 强科技公司运作方式的多 Agent AI 公司团队，可自动生成战略、产品、用户研究、数据、模型、训练、微调、测试、MLOps、安全、法务、财务、运营、客户成功和展示交付包。
