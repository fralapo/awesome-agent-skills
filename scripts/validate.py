#!/usr/bin/env python3
"""Validate every skill in this repo. Standard library only (PyYAML used if present).

Run from the repo root:  python3 scripts/validate.py
Exit code 1 if any error is found. Warnings do not fail the run.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

MAX_DESCRIPTION = 1024
MAX_NAME = 64
MAX_SKILL_LINES = 500

# Files whose relative links are examples or vendored docs, not navigation.
LINK_CHECK_SKIP = ("ffmpeg/reference/", "awesome-readme/references/")
# Skills allowed to contain video-site URLs (they teach embedding or cite public talks).
VIDEO_URL_ALLOW = ("awesome-readme", "ffmpeg", "creative-director")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    raw = m.group(1)
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(raw)
        return data if isinstance(data, dict) else None
    except ImportError:
        pass
    except Exception as exc:  # invalid YAML
        err(f"{path.relative_to(ROOT)}: invalid YAML frontmatter ({exc})")
        return {}
    # Fallback: single-line `key: value` pairs only.
    data = {}
    for line in raw.splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            value = km.group(2).strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            data[km.group(1)] = value
    return data


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def check_skill(skill: Path) -> None:
    name = skill.name
    skill_md = skill / "SKILL.md"
    if not skill_md.is_file():
        err(f"{name}: missing SKILL.md")
        return

    fm = parse_frontmatter(skill_md)
    if fm is None:
        err(f"{name}: SKILL.md has no frontmatter block")
        fm = {}
    fm_name = str(fm.get("name", "")).strip()
    desc = str(fm.get("description", "")).strip()

    if fm_name != name:
        err(f"{name}: frontmatter name '{fm_name}' does not match the folder name")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > MAX_NAME:
        err(f"{name}: folder name must be lowercase-hyphenated and at most {MAX_NAME} characters")
    if not desc:
        err(f"{name}: empty description")
    elif len(desc) > MAX_DESCRIPTION:
        err(f"{name}: description is {len(desc)} characters (max {MAX_DESCRIPTION})")
    if "<" in desc or ">" in desc:
        err(f"{name}: description contains angle brackets")
    if desc and not re.search(r"\b(use|trigger)", desc, re.I):
        warn(f"{name}: description never says when to use the skill")

    lines = skill_md.read_text(encoding="utf-8").count("\n") + 1
    if lines > MAX_SKILL_LINES:
        warn(f"{name}: SKILL.md is {lines} lines (aim for {MAX_SKILL_LINES} or fewer)")

    md_files = sorted(skill.rglob("*.md"))
    texts = {f: f.read_text(encoding="utf-8", errors="replace") for f in md_files}

    for f, text in texts.items():
        rel = f.relative_to(SKILLS).as_posix()
        if not rel.startswith(LINK_CHECK_SKIP):
            for target in re.findall(r"\]\(([^)\s]+)\)", strip_code(text)):
                target = target.split("#", 1)[0]
                if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue
                if not (f.parent / target).exists():
                    err(f"{rel}: broken link -> {target}")
        if name not in VIDEO_URL_ALLOW and re.search(r"youtube\.com|youtu\.be", text, re.I):
            err(f"{rel}: contains a video URL (skills hold theory, not source links)")

    # Every file should be reachable: its name (or stem) must appear in another file of the skill.
    for f in md_files:
        if f == skill_md or f.name.lower() == "readme.md":
            continue
        if not any(f.stem in text for other, text in texts.items() if other != f):
            warn(f"{f.relative_to(SKILLS).as_posix()}: not referenced by any other file in the skill")


def check_repo(skill_names: list[str]) -> None:
    # Codex symlinks
    agents = ROOT / ".agents" / "skills"
    present = {p.name for p in agents.iterdir()} if agents.is_dir() else set()
    for name in skill_names:
        link = agents / name
        if name not in present:
            err(f".agents/skills/{name}: missing symlink")
        elif not (link / "SKILL.md").is_file():
            err(f".agents/skills/{name}: does not resolve to a skill folder")
    for extra in sorted(present - set(skill_names)):
        err(f".agents/skills/{extra}: no matching folder in skills/")

    # Manifests
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    versions = {
        "plugin.json": plugin.get("version"),
        "marketplace.json metadata": market.get("metadata", {}).get("version"),
        "marketplace.json plugin entry": market.get("plugins", [{}])[0].get("version"),
    }
    if len(set(versions.values())) != 1:
        err(f"version mismatch across manifests: {versions}")
    elif not re.fullmatch(r"\d+\.\d+\.\d+", str(plugin.get("version"))):
        err(f"plugin.json version '{plugin.get('version')}' is not semver")

    # README
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in skill_names:
        if f"skills/{name}/" not in readme:
            err(f"README.md: skill '{name}' is not listed")
    badge = re.search(r"badge/skills-(\d+)-", readme)
    if not badge:
        err("README.md: skills count badge not found")
    elif int(badge.group(1)) != len(skill_names):
        err(f"README.md: badge says {badge.group(1)} skills, repo has {len(skill_names)}")

    changelog = ROOT / "CHANGELOG.md"
    if changelog.is_file() and f"## {plugin.get('version')}" not in changelog.read_text(encoding="utf-8"):
        err(f"CHANGELOG.md: no entry for version {plugin.get('version')}")


def main() -> int:
    skills = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for skill in skills:
        check_skill(skill)
    check_repo([s.name for s in skills])

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"\n{len(skills)} skills checked, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
