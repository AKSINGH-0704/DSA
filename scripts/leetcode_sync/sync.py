#!/usr/bin/env python3
"""
Sync accepted LeetCode submissions into this repository.

Modes
-----
Incremental (default, runs every 6h via cron):
    Loads .sync_state.json from the repo root to find the last-synced
    submission ID, then fetches submissions newest-first and stops as soon
    as an ID <= the stored value is seen.  This eliminates the 200-submission
    sliding-window assumption: no submissions are ever missed regardless of
    how many you make between runs.  If no state file exists (first run),
    falls back to scanning the most recent `--max-pages` pages.

Backfill (--backfill, run manually once via workflow_dispatch):
    Ignores the state file and paginates through the ENTIRE submission
    history.  State is saved at the end so the next incremental run starts
    from the right point.

In both modes, for every ACCEPTED submission the script:
  1. Resolves the problem's frontend ID + slug.
  2. Checks whether "<id>-<slug>/" already exists in the repo - if so, skips it.
  3. Otherwise fetches the problem statement + submission code and writes a
     new "<id>-<slug>/" folder containing README.md and the solution file.

State file (.sync_state.json) is committed alongside new problem folders by
the calling workflow, so the recorded ID and repo contents are always in sync.

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
from state import load_state, save_state

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
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Scan LeetCode and report what would be committed, but do not write any "
            "files or create commits. Fetches submission metadata only (no code download)."
        ),
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

    if args.dry_run:
        print("*** DRY RUN MODE — no files will be written, no commits will be created ***", flush=True)

    print("Credentials loaded. Connecting to LeetCode ...", flush=True)

    try:
        username = client.verify_auth()
    except LeetCodeAuthError as exc:
        print(
            f"::error title=LeetCode Auth Failed::{exc}",
            file=sys.stderr, flush=True,
        )
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        return 1
    print(f"Authenticated as LeetCode user: {username}", flush=True)

    # State-based incremental scan: load last-synced submission ID so we stop
    # exactly where the previous run left off rather than relying on a fixed
    # 200-submission window.
    last_synced_id = 0
    if not args.backfill:
        last_synced_id = load_state(args.repo_root)
        if last_synced_id:
            print(f"State loaded: will stop at submission_id <= {last_synced_id}", flush=True)
        else:
            print(f"No prior state — scanning last {args.max_pages} page(s).", flush=True)

    max_pages = None if args.backfill else (None if last_synced_id else args.max_pages)
    mode = "backfill (full history)" if args.backfill else (
        "incremental (state-based, newest-first until last synced ID)"
        if last_synced_id else
        f"incremental (page-window, last {args.max_pages} page(s))"
    )
    if args.dry_run:
        mode = f"DRY RUN / {mode}"
    print(f"Scanning submissions: {mode}", flush=True)

    added: list[str] = []
    would_add: list[str] = []
    skipped_existing: set[str] = set()
    seen_slugs: set[str] = set()
    per_problem_errors: list[str] = []
    max_seen_id: int = 0  # highest submission ID seen this run (first page, first sub)

    for sub in client.iter_submissions(max_pages=max_pages):
        sub_id = int(sub.get("id") or 0)

        # Update running max (submissions are newest-first so this triggers once).
        if sub_id > max_seen_id:
            max_seen_id = sub_id

        # State-based early termination: we've reached submissions we already processed.
        if not args.backfill and last_synced_id and sub_id <= last_synced_id:
            print(
                f"[state] Reached submission_id={sub_id} (<= last_synced_id={last_synced_id}) — stopping scan.",
                flush=True,
            )
            break

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

            lang = sub.get("lang") or "unknown"

            if args.dry_run:
                # In dry-run mode: report without fetching code or writing files.
                folder = f"{frontend_id}-{slug}"
                would_add.append(folder)
                print(f"  DRY RUN: would add {folder} ({lang})", flush=True)
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

    # Persist state after every successful (non-dry-run) scan so the next
    # incremental run knows where to stop.  Saved even when nothing was added —
    # this advances the cursor past non-accepted submissions too.
    if not args.dry_run and max_seen_id > 0:
        save_state(args.repo_root, max_seen_id, username)

    if args.dry_run:
        print(
            f"\nDRY RUN complete. Would add {len(would_add)} new problem(s); "
            f"{len(skipped_existing)} already-present problem(s) would be skipped; "
            f"{len(per_problem_errors)} error(s).",
            flush=True,
        )
        summary_lines = [f"DRY RUN: would sync {len(would_add)} new accepted LeetCode submission(s)."]
        summary_lines += [f"- {name}" for name in sorted(would_add)]
    else:
        print(
            f"\nDone. Added {len(added)} new problem(s); "
            f"{len(skipped_existing)} already-present problem(s) skipped; "
            f"{len(per_problem_errors)} error(s).",
            flush=True,
        )
        summary_lines = [f"Synced {len(added)} new accepted LeetCode submission(s)."]
        summary_lines += [f"- {name}" for name in sorted(added)]

    if per_problem_errors:
        print(f"  Problems that failed (will retry on next run): {', '.join(per_problem_errors)}", flush=True)
        print("::warning::Some problems failed to sync - see logs above for details.", flush=True)
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
            f.write(f"would_add_count={len(would_add)}\n")
            f.write(f"error_count={len(per_problem_errors)}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
