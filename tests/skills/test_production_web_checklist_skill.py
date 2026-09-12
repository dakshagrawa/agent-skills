from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "production-web-checklist" / "SKILL.md"


def read_skill():
    return read_skill_file(SKILL)


def read_skill_file(path):
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(?P<frontmatter>.*?)\n---\n(?P<body>.+)\Z", content, re.DOTALL)
    assert match, f"{path} must have YAML frontmatter at byte zero"
    frontmatter = yaml.safe_load(match.group("frontmatter"))
    assert isinstance(frontmatter, dict)
    return content, frontmatter, match.group("body")


def test_frontmatter_has_repository_contract():
    _, frontmatter, body = read_skill()

    assert frontmatter["name"] == "production-web-checklist"
    description = frontmatter["description"]
    assert description.endswith(".")
    assert len(description) <= 60
    assert frontmatter["version"] == "0.2.0"
    assert frontmatter["author"].startswith("Daksh Agrawal")
    assert frontmatter["license"] == "MIT"
    assert frontmatter["platforms"] == ["linux", "macos", "windows"]
    hermes = frontmatter["metadata"]["hermes"]
    assert hermes["tags"] == ["web", "design", "accessibility", "seo", "security", "performance"]
    assert hermes["related_skills"] == []
    assert body.strip()


def test_description_stays_self_contained_before_catalog_truncation():
    description = read_skill()[1]["description"]
    assert len(description) <= 57
    assert description.endswith("security.")


def test_body_contains_actionable_sections_in_order():
    body = read_skill()[2]
    sections = [
        "## When to Use",
        "## Prerequisites",
        "## How to Run",
        "## Quick Reference",
        "## Procedure",
        "## Output Contract",
        "## Pitfalls",
        "## Verification",
    ]
    positions = [body.index(section) for section in sections]
    assert positions == sorted(positions)

    procedure = body[body.index("## Procedure") : body.index("## Output Contract")]
    steps = re.findall(r"^\d+\. \*\*[^\n]+", procedure, flags=re.MULTILINE)
    assert len(steps) == 12
    assert procedure.count("**Complete when:**") == len(steps)


def test_skill_does_not_include_machine_paths_or_em_dash():
    content = read_skill()[0]
    assert "—" not in content
    assert not re.search(r"(?:/home/|/Users/|[A-Za-z]:\\\\)", content)
    assert len(content) <= 100_000


def test_repository_docs_and_test_entrypoint_exist():
    assert (ROOT / "README.md").is_file()
    assert (ROOT / "CONTRIBUTING.md").is_file()
    assert (ROOT / "SECURITY.md").is_file()
    assert (ROOT / "CHANGELOG.md").is_file()
    assert (ROOT / "scripts" / "run_tests.sh").is_file()
    assert (ROOT / ".github" / "workflows" / "ci.yml").is_file()


def test_ci_uses_immutable_actions_and_checks_the_change_range():
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert re.search(r"uses: actions/checkout@[0-9a-f]{40}", workflow)
    assert re.search(r"uses: actions/setup-python@[0-9a-f]{40}", workflow)
    assert 'git diff --check "$BASE_SHA" HEAD' in workflow
    assert 'BEFORE_SHA: ${{ github.event.before }}' in workflow
    assert 'git diff --check "$BEFORE_SHA" HEAD' in workflow
    assert 'ROOT_SHA="$(git rev-list --max-parents=0 HEAD | tail -n 1)"' in workflow
    assert 'git diff-tree --check --root -r "$ROOT_SHA"' in workflow
    assert 'git diff --check "$ROOT_SHA" HEAD' in workflow


def test_every_top_level_skill_has_a_valid_contract():
    skill_files = sorted(ROOT.glob("*/SKILL.md"))
    assert skill_files
    skill_names = {path.parent.name for path in skill_files}

    for path in skill_files:
        content, frontmatter, body = read_skill_file(path)
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", frontmatter["name"])
        assert frontmatter["name"] == path.parent.name
        assert re.fullmatch(r"\d+\.\d+\.\d+", str(frontmatter["version"]))
        assert isinstance(frontmatter["description"], str)
        assert len(frontmatter["description"]) <= 60
        assert frontmatter["description"].endswith(".")
        assert frontmatter["author"]
        assert frontmatter["license"]
        assert frontmatter["platforms"]
        hermes = frontmatter["metadata"]["hermes"]
        assert hermes["tags"]
        assert set(hermes.get("related_skills", [])) <= skill_names
        assert body.strip()
        assert len(content) <= 100_000
