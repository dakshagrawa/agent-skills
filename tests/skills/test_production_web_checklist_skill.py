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
    assert frontmatter["version"] == "0.3.0"
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


def test_skill_preserves_explicit_original_requirements():
    content, _, body = read_skill()
    content = " ".join(content.split())
    required_phrases = [
        "purple gradients",
        "blue-purple gradients",
        "aurora backgrounds",
        "glassmorphism",
        "floating analytics dashboards",
        "generic abstract 3D shapes",
        "pill-shaped buttons",
        "Framer-style startup hero sections",
        "generic feature-card grids",
        "bento box layouts",
        "cursor animations",
        "raw emojis as UI icons",
        "fake customer counters",
        "fake metrics",
        "fake reviews",
        "fake urgency",
        "stock imagery that implies an untrue",
        "Do not treat a visual trend as a requirement",
        "Made with AI",
        "default framework titles",
        "em dash punctuation",
        "Unlock",
        "Supercharge",
        "Streamline",
        "Seamless",
        "Revolutionise",
        "Leverage",
        "Transform your business",
        "Cutting-edge",
        "All-in-one platform",
        "Powerful solution",
        "Next-generation",
        "Elevate your workflow",
        "We help businesses grow",
        "exactly one clear, compelling primary CTA above the fold",
        "unique page title",
        "unique meta description",
        "canonical tag",
        "canonical tags across all pages",
        "LocalBusiness",
        "Organization",
        "BreadcrumbList",
        "sitemap.xml",
        "robots.txt",
        "llm.txt",
        "Twitter Card",
        "1200x630",
        "visible breadcrumb navigation",
        "Privacy Policy",
        "Terms & Conditions",
        "Terms and Conditions",
        "Cookie Policy",
        "Refund Policy",
        "form-consent opt-in checkboxes",
        "cookie-consent banner",
        "Google Analytics",
        "physical address",
        "business registration information",
        "copyright licenses",
        "Force HTTPS",
        "honeypot",
        "CAPTCHA",
        "XSS",
        "SQL-injection",
        "bcrypt",
        "Argon2",
        "RBAC",
        "Content Security Policy",
        "HSTS",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "strict CORS",
        "Case Study",
        "FAQ",
        "Team with real team photos",
        "Location, Map, and Directions",
        "Thank You page",
        "response-time promise",
        "sticky CTA bar",
        "WCAG 2.1 AA",
        "descriptive `alt` text",
        "custom-domain",
        "custom, helpful 404",
        "WebP or AVIF",
        "production source maps",
        "browser console errors",
        "mobile, tablet, and desktop",
        "Strategy Snapshot",
        "Three Creative Directions",
        "Chosen Direction",
        "Complete Website Build",
        "durable product brief",
        "smallest useful workflow",
        "AI-assisted",
        "human-reviewed",
        "handoff contracts",
        "idempotency",
        "kill switch",
        "prompt or user-content transfer",
        "generated HTML",
        "human-correction rate",
        "sample `curl` request",
        "visual references",
        "spacing rhythm",
        "real 404",
        "copy-to-clipboard",
        "UTM handling",
        "crawlable rendering",
        "cold response",
        "remove accidental `noindex` tags",
        "one H1 per page",
        "fix the broken links",
        "compress images",
        "Core Web Vitals",
        "Google Search Console",
        "ethical, quality-led backlink strategy",
        "AI feature theater",
        "Small-detail theater",
    ]
    missing = [phrase for phrase in required_phrases if phrase.lower() not in content.lower()]
    assert not missing, f"requirements missing from skill: {missing}"

    procedure = body[body.index("## Procedure") : body.index("## Output Contract")]
    matches = list(re.finditer(r"^\s*(\d+)\. \*\*[^\n]+", procedure, flags=re.MULTILINE))
    steps = {
        int(match.group(1)): procedure[match.start() : matches[index + 1].start() if index + 1 < len(matches) else None]
        for index, match in enumerate(matches)
    }
    assert set(steps) == set(range(1, 13))

    requirements_by_step = {
        1: ["durable product brief", "critique missing assumptions", "smallest useful workflow"],
        2: ["Business name", "Target audience", "Brand personality", "Available proof", "Design constraints", "smallest useful workflow"],
        3: ["Do not use the following patterns", "Never use em dash punctuation", "generic abstract 3D shapes", "cursor animations", "fake urgency", "stock imagery that implies an untrue", "Do not treat a visual trend as a requirement", "visual references", "spacing rhythm"],
        4: ["success, loading, empty", "exactly one clear, compelling primary CTA above", "sticky CTA bar", "content or task does not justify", "document the specific rationale", "input/output contract", "handoff contracts", "idempotency", "real 404", "copy-to-clipboard", "UTM handling"],
        5: ["Hero headline", "Case Study", "FAQ", "Team with real team photos", "Thank You page", "smallest useful flow", "input-to-output walkthrough"],
        6: ["Exactly one clear `<h1>` tag per page", "unique page title", "unique meta description", "canonical tags across all pages", "remove accidental `noindex` tags", "one H1 per page", "fix the broken links", "compress images", "Core Web Vitals", "Google Search Console", "ethical, quality-led backlink strategy", "LocalBusiness", "BreadcrumbList", "Generate valid `sitemap.xml`", "crawlable rendering", "cold response"],
        7: ["build standalone Privacy Policy", "form-consent opt-in checkboxes", "cookie-consent banner", "Properly set up and verify analytics tracking", "copyright licenses", "provider, model, API key boundary", "prompt or user-content transfer"],
        8: ["Force HTTPS", "client and server", "bcrypt or Argon2", "strict RBAC", "Content Security Policy", "HSTS", "X-Frame-Options", "X-Content-Type-Options", "generated HTML", "kill switch"],
        9: ["WCAG 2.1 AA", "Keyboard operation", "Every image has an intentional alt value", "44 by 44 CSS-pixel"],
        10: ["custom-domain", "custom, helpful 404", "WebP or AVIF", "production source maps", "browser console errors", "full custom favicon set", "mobile, tablet, and desktop", "human-correction rate"],
        12: ["Strategy Snapshot", "Three Creative Directions", "Chosen Direction", "Complete Website Build and Verification", "A. Direction Name", "F. Risks and Tradeoffs"],
    }
    for step_number, phrases in requirements_by_step.items():
        step_text = " ".join(steps[step_number].split()).lower()
        missing_in_step = [phrase for phrase in phrases if phrase.lower() not in step_text]
        assert not missing_in_step, f"requirements misplaced or weakened in step {step_number}: {missing_in_step}"

    assert "Do not use" in steps[3]
    assert all("Complete when:" in text for text in steps.values())
