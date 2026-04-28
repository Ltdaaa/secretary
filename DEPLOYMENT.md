# Deployment Guide

## What To Submit

Submit the ZIP file:

```text
enterprise-model-lab-team-submission.zip
```

Submit the website URL after deploying:

```text
submission-ready/site/index.html
```

## Static Website Deployment

The web demo is a pure static site. It does not require a backend, API key, GPU, database, or Python runtime.

Deploy the `submission-ready/site/` folder with one of these:

- GitHub Pages
- Vercel
- Netlify
- Any static file host

The entry file is:

```text
index.html
```

## Local Preview

```powershell
cd submission-ready\site
python -m http.server 8088 --bind 127.0.0.1
```

Open:

```text
http://127.0.0.1:8088/
```

## What Works In The Browser

- 31-Agent company cockpit visualization.
- CSV upload and browser-side parsing.
- Text/label column detection.
- Label distribution and data quality summary.
- Model route recommendation.
- Agent handoff logs.
- Downloadable Markdown report.
- Downloadable company deliverables.
- Downloadable JSON evidence file.
- Browser-side function self-test.
- GPO real-analysis case page.

## What Requires Local Python

Deep project scanning requires:

```powershell
python enterprise-model-lab-team\scripts\company_os.py --workspace demo-deliveries\psych-safety-ai-company --source .
```

This creates:

- `run-report.md`
- `asset-inventory.json`
- `readiness-score.json`
- `action-plan.json`
- `work-orders.md`
- `execution-status.json`
- `execution-log.md`
- `executed-work/`
- `client-project-status.json`
- `client-project/`

## Final Verification

```powershell
python enterprise-model-lab-team\tests\validate_skill.py
python enterprise-model-lab-team\tests\validate_company_os.py
python enterprise-model-lab-team\tests\validate_site.py --site site
node enterprise-model-lab-team\tests\validate_site_runtime.js site
python enterprise-model-lab-team\tests\validate_submission_package.py --submission submission-ready --zip enterprise-model-lab-team-submission.zip
```
