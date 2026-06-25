"""
Persistent state for incremental LeetCode sync.

The state file (.sync_state.json at the repo root) records the highest
submission ID seen in the last successful sync.  On each incremental run
the script fetches submissions from the LeetCode API, newest first, and
stops as soon as it sees a submission ID <= the stored value.  This means:

  - Only genuinely new submissions are processed each run.
  - The 200-submission sliding-window limitation is eliminated.
  - API quota usage is proportional to activity, not to history size.

The file is committed alongside any new problem folders, so the stored ID
and the repo contents are always in sync.  If a push fails, the next
checkout restores the old state file, and the next run re-scans from the
correct point.

If the state file is absent or unreadable the sync falls back to the
page-window behaviour (--max-pages) so first runs work without setup.
"""

from __future__ import annotations

import datetime
import json
import os

STATE_FILE = ".sync_state.json"


def load_state(repo_root: str) -> int:
    """
    Return the last successfully-synced submission ID, or 0.

    0 means "no prior state" — caller should fall back to the page window.
    """
    path = os.path.join(repo_root, STATE_FILE)
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        sid = int(data.get("last_submission_id", 0))
        return max(sid, 0)
    except FileNotFoundError:
        return 0
    except (json.JSONDecodeError, ValueError, KeyError, TypeError, OSError) as exc:
        print(
            f"WARNING: state file {path} is unreadable ({type(exc).__name__}: {exc}); "
            "falling back to page-window scan.",
            flush=True,
        )
        return 0


def save_state(repo_root: str, submission_id: int, username: str) -> None:
    """
    Persist the last-seen submission ID after a successful sync.

    Only writes the file when submission_id has actually advanced — if the
    ID is unchanged the file is left untouched so git sees no diff and the
    workflow skips an empty commit.

    Written via a temp-file + atomic rename so a mid-write crash never
    leaves a partially-written (corrupt) state file.
    """
    if load_state(repo_root) == submission_id:
        print(f"State unchanged (last_submission_id={submission_id}) — skipping write.", flush=True)
        return

    path = os.path.join(repo_root, STATE_FILE)
    tmp = path + ".tmp"
    data = {
        "last_submission_id": submission_id,
        "synced_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "synced_by": username,
    }
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    os.replace(tmp, path)
    print(f"State saved: last_submission_id={submission_id}", flush=True)
