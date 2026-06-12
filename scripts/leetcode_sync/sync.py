#!/usr/bin/env python3
"""
Sync accepted LeetCode submissions into this repository.

Modes
-----
Incremental (default, runs every 3h via cron):
    Scans the most recent `--max-pages` pages of submission history
    (default 10 pages x 20 = 200 most recent submissions, of any status).
    This comfortably covers anything submitted since the last run.

Backfill (--backfill, run manually once via workflow_dispatch):
    Paginates through the ENTIRE submission history.

In both modes, for every ACCEPTED submission the script:
  1. Resolves the problem's frontend ID + slug.
  2. Checks whether "<id>-<slug>/" already exists in the repo - if so, skips it.
  3. Otherwise fetches the problem statement + submission code and writes a
     new "<id>-<slug>/" folder containing README.md and the solution file.

No git operations happen here - the calling workflow stages/commits/pushes
only if files actually changed, which guarantees no empty/duplicate commits.

Requires env vars LEETCODE_SESSION and LEETCODE_CSRF_TOKEN (see SETUP.md).
"""

from __future__ import annotations

import argparse
import os
import sys
import time

from client import LeetCodeAuthError, LeetCodeClient
from repo import problem_exists, write_problem

ACCEPTED = "Accepted"
DEFAULT_INCREMENTAL_PAGES = 10  # 10 pages x 20/page = 200 most recent submissions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo-root", default=".", help="Path to the repo checkout (default: cwd)")
    parser.add_argument(
        "--backfill",
        action="store_true",
        help="Paginate through the FULL submission history instead of just recent pages",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=DEFAULT_INCREMENTAL_PAGES,
        help=f"Pages to scan in incremental mode (default: {DEFAULT_INCREMENTAL_PAGES}); ignored with --backfill",
    )
    parser.add_argument(
        "--request-delay",
        type=float,
        default=1.0,
        help="Seconds to sleep between LeetCode API calls (default: 1.0)",
    )
    parser.add_argument(
        "--summary-file",
        default=os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "leetcode_sync_summary.txt"),
        help="Where to write a human-readable summary of newly added problems",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    session_cookie = os.environ.get("LEETCODE_SESSION")
    csrf_token = os.environ.get("LEETCODE_CSRF_TOKEN")
    if not session_cookie or not csrf_token:
        print(
            "ERROR: LEETCODE_SESSION and LEETCODE_CSRF_TOKEN environment variables "
            "must both be set. See SETUP.md.",
            file=sys.stderr,
        )
        return 1

    client = LeetCodeClient(session_cookie, csrf_token, request_delay=args.request_delay)
    print("Credentials loaded. Connecting to LeetCode ...", flush=True)

    try:
        username = client.verify_auth()
    except LeetCodeAuthError as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        return 1
    print(f"Authenticated as LeetCode user: {username}", flush=True)

    max_pages = None if args.backfill else args.max_pages
    mode = "backfill (full history)" if args.backfill else f"incremental (last {max_pages} page(s) of submissions)"
    print(f"Scanning submissions: {mode}", flush=True)

    added: list[str] = []
    skipped_existing: set[str] = set()
    seen_slugs: set[str] = set()
    per_problem_errors: list[str] = []

    for sub in client.iter_submissions(max_pages=max_pages):
        if sub.get("statusDisplay") != ACCEPTED:
            continue

        slug = sub.get("titleSlug")
        if not slug or slug in seen_slugs:
            # Multiple accepted submissions for the same problem: only the
            # newest matters (results are newest-first, so we keep the first).
            continue
        seen_slugs.add(slug)

        try:
            question = client.get_question(slug)
            frontend_id = question["questionFrontendId"]
            time.sleep(args.request_delay)

            if problem_exists(args.repo_root, frontend_id, slug):
                skipped_existing.add(slug)
                continue

            result = client.get_submission_code(sub["id"])
            time.sleep(args.request_delay)
            if result is None:
                print(f"  WARNING: code unavailable for '{slug}' (submission {sub['id']}); will retry next run", flush=True)
                continue

            code, lang_name = result
            lang = sub.get("lang") or lang_name or "txt"
            folder = write_problem(args.repo_root, question, code, lang)
            added.append(folder)
            print(f"  + added {folder} ({lang})", flush=True)

        except Exception as exc:
            msg = f"  ERROR: could not sync '{slug}': {type(exc).__name__}: {exc}"
            print(msg, flush=True)
            per_problem_errors.append(slug)

    print(
        f"\nDone. Added {len(added)} new problem(s); "
        f"{len(skipped_existing)} already-present problem(s) skipped; "
        f"{len(per_problem_errors)} error(s).",
        flush=True,
    )
    if per_problem_errors:
        print(f"  Problems that failed (will retry on next run): {', '.join(per_problem_errors)}", flush=True)
        print("::warning::Some problems failed to sync - see logs above for details.", flush=True)

    summary_lines = [f"Synced {len(added)} new accepted LeetCode submission(s)."]
    summary_lines += [f"- {name}" for name in sorted(added)]
    if per_problem_errors:
        summary_lines += ["", f"Errors ({len(per_problem_errors)} problem(s) skipped - will retry):"]
        summary_lines += [f"- {slug}" for slug in per_problem_errors]
    summary = "\n".join(summary_lines) + "\n"

    summary_dir = os.path.dirname(args.summary_file)
    if summary_dir:
        os.makedirs(summary_dir, exist_ok=True)
    with open(args.summary_file, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"Summary written to {args.summary_file}", flush=True)

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"added_count={len(added)}\n")
            f.write(f"error_count={len(per_problem_errors)}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
