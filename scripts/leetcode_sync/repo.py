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
import re

# Matches any folder whose name is {digits}-{anything}, i.e. a valid problem folder.
_PROBLEM_DIR_RE = re.compile(r"^\d+-.+$")

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


def _is_complete_problem_dir(path: str) -> bool:
    """A folder is only 'complete' if it contains README.md.

    If a prior run was interrupted after os.makedirs() but before the files
    were flushed, the directory exists but is empty or partial.  Without this
    guard, problem_exists() would return True and the broken folder would
    never be repaired.
    """
    return os.path.isfile(os.path.join(path, "README.md"))


def problem_exists(repo_root: str, frontend_id: str, title_slug: str) -> bool:
    """
    True if a complete folder for this problem already exists in the repo.

    Two checks are performed in order:

    1. Exact match: {frontend_id}-{title_slug} directory exists and contains
       README.md (the completion sentinel written last by write_problem).

    2. Slug-pattern fallback: any complete directory matching r'^[0-9]+-{title_slug}$'.
       This handles the case where a pre-existing folder (e.g. imported by
       LeetSync) used a different numeric ID than the one LeetCode's
       questionFrontendId returns today. Without this check, the backfill
       would create a second folder for the same problem under the API ID,
       producing silent duplicates (which is exactly what happened to the
       8 contest-problem pairs already in this repo).
    """
    exact = os.path.join(repo_root, folder_name(frontend_id, title_slug))
    if os.path.isdir(exact) and _is_complete_problem_dir(exact):
        return True
    slug_suffix = f"-{title_slug}"
    try:
        for entry in os.listdir(repo_root):
            if (entry.endswith(slug_suffix)
                    and _PROBLEM_DIR_RE.match(entry)):
                candidate = os.path.join(repo_root, entry)
                if os.path.isdir(candidate) and _is_complete_problem_dir(candidate):
                    return True
    except OSError:
        pass
    return False


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

    Files are written atomically: code is flushed to a .tmp sibling and
    renamed into place; README.md is written last so it acts as a completion
    sentinel — problem_exists() checks for README.md to distinguish complete
    folders from ones that were interrupted mid-write.

    Returns the folder name, e.g. "23-merge-k-sorted-lists".
    """
    frontend_id = question["questionFrontendId"]
    slug = question["titleSlug"]
    name = folder_name(frontend_id, slug)
    folder = os.path.join(repo_root, name)
    os.makedirs(folder, exist_ok=True)

    ext = LANGUAGE_EXTENSIONS.get((lang or "").lower(), (lang or "txt").lower())
    sol_path = os.path.join(folder, f"{slug}.{ext}")
    sol_tmp = sol_path + ".tmp"
    with open(sol_tmp, "w", encoding="utf-8") as f:
        f.write(code)
    os.replace(sol_tmp, sol_path)

    readme_path = os.path.join(folder, "README.md")
    readme_tmp = readme_path + ".tmp"
    with open(readme_tmp, "w", encoding="utf-8") as f:
        f.write(_readme_content(question))
    os.replace(readme_tmp, readme_path)

    return name
