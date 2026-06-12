"""
Helpers for reading/writing problem folders in the DSA repository.

Matches the existing repository layout:

    <questionFrontendId>-<title-slug>/
        README.md           - LeetCode problem statement (HTML) + difficulty badge
        <title-slug>.<ext>   - accepted submission source code

e.g. "23-merge-k-sorted-lists/README.md" and
     "23-merge-k-sorted-lists/merge-k-sorted-lists.py"
"""

from __future__ import annotations

import os

DIFFICULTY_COLORS = {
    "Easy": "green",
    "Medium": "orange",
    "Hard": "red",
}

# LeetCode submission "lang" slugs -> file extension. Extend as new
# languages are encountered.
LANGUAGE_EXTENSIONS = {
    "python": "py",
    "python3": "py",
    "java": "java",
    "cpp": "cpp",
    "c": "c",
    "csharp": "cs",
    "javascript": "js",
    "typescript": "ts",
    "golang": "go",
    "go": "go",
    "kotlin": "kt",
    "swift": "swift",
    "rust": "rs",
    "scala": "scala",
    "ruby": "rb",
    "php": "php",
    "dart": "dart",
    "racket": "rkt",
    "erlang": "erl",
    "elixir": "ex",
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
    "postgresql": "sql",
}


def folder_name(frontend_id: str, title_slug: str) -> str:
    return f"{frontend_id}-{title_slug}"


def problem_exists(repo_root: str, frontend_id: str, title_slug: str) -> bool:
    """True if a folder for this problem already exists in the repo."""
    return os.path.isdir(os.path.join(repo_root, folder_name(frontend_id, title_slug)))


def _readme_content(question: dict) -> str:
    difficulty = question.get("difficulty", "")
    color = DIFFICULTY_COLORS.get(difficulty, "blue")
    title = question["title"]
    slug = question["titleSlug"]
    content = question.get("content") or ""
    return (
        f'<h2><a href="https://leetcode.com/problems/{slug}">{title}</a></h2> '
        f"<img src='https://img.shields.io/badge/Difficulty-{difficulty}-{color}' "
        f"alt='Difficulty: {difficulty}' /><hr>{content}"
    )


def write_problem(repo_root: str, question: dict, code: str, lang: str) -> str:
    """
    Create a new problem folder containing README.md and the solution file.

    Caller must have already verified the folder does not exist (via
    `problem_exists`) so this never silently overwrites prior work.

    Returns the folder name, e.g. "23-merge-k-sorted-lists".
    """
    frontend_id = question["questionFrontendId"]
    slug = question["titleSlug"]
    name = folder_name(frontend_id, slug)
    folder = os.path.join(repo_root, name)
    os.makedirs(folder, exist_ok=False)

    with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as f:
        f.write(_readme_content(question))

    ext = LANGUAGE_EXTENSIONS.get((lang or "").lower(), (lang or "txt").lower())
    with open(os.path.join(folder, f"{slug}.{ext}"), "w", encoding="utf-8") as f:
        f.write(code)

    return name
