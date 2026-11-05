"""Offline checks for the collection's scope and honest catalog."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def test_scope_covers_web_and_broader_software_without_claiming_packages():
    scope = (ROOT / "SCOPE.md").read_text(encoding="utf-8").lower()
    for topic in ["web", "security", "testing", "deployment", "performance",
                  "operations", "backend", "infrastructure", "non-web"]:
        assert topic in scope
    assert "not shipped skills" in scope
    assert "media scout" in scope
    assert "a distinct, reusable, independently callable workflow" in scope
    assert "no change" in scope


def test_readme_catalog_links_only_real_packages_and_keeps_web_identity():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "dakshagrawa/production-checklist" in readme
    assert "package name, path, version and behavior are unchanged" in readme
    catalog = readme.split("## Current skill catalog", 1)[1].split("## ", 1)[0]
    listed = set(re.findall(r"\]\(([^)]+/SKILL\.md)\)", catalog))
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.glob("*/SKILL.md")}
    assert listed == actual
    assert "production-web-checklist/SKILL.md" in listed


def test_repository_guides_resolve_and_require_reviewed_new_skills():
    for name in ["README.md", "CONTRIBUTING.md", "MIGRATION.md", "SCOPE.md"]:
        path = ROOT / name
        source = path.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", source):
            if not link.startswith(("https:", "http:", "#")):
                assert (path.parent / link.split("#", 1)[0]).is_file(), (name, link)
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "SCOPE.md" in contributing
    assert "focused tests" in contributing
    assert "Preserve authorship" in contributing
    assert "Media Scout machinery stays separate" in contributing
