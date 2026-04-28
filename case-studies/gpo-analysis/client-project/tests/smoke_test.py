from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = ["index.html", "README.md", "DEPLOYMENT.md", "ACCEPTANCE.md", "project-manifest.json"]
missing = [name for name in required if not (root / name).exists()]
assert not missing, f"missing files: {missing}"
html = (root / "index.html").read_text(encoding="utf-8")
assert "Run Delivery App" in html
assert "downloadDelivery" in html
assert "client-delivery.json" in html
assert "requires_api_key" in (root / "project-manifest.json").read_text(encoding="utf-8")
print("client project smoke test passed")
