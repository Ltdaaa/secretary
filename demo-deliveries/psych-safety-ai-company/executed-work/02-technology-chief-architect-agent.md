# Executed Work Order 2: Technology

Owner: Chief Architect Agent
Priority: P0

## Work Order

Keep the browser demo and local Python runner as separate, reproducible execution paths.

## Acceptance Criteria

Static website works without API keys; local runner writes machine-readable evidence files.

## Evidence Used

site/index.html, scripts/company_os.py

## Executed Output

- Runtime split implemented as static browser experience plus Python project runner.
- Browser path requires no API key, backend, GPU, database, or login.
- Python path writes machine-readable evidence files and updates company artifacts.

