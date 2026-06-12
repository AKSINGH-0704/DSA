# LeetCode → GitHub Sync — Setup

Automatically pulls your **accepted** LeetCode submissions into this repo,
every 1 hour, in the same `<id>-<slug>/README.md` + `<id>-<slug>/<slug>.<ext>`
format already used here.

## 1. Files in this bundle

Copy this entire tree into the **root** of `AKSINGH-0704/DSA`:

```
.github/workflows/leetcode-sync.yml   <- scheduled + manual workflow
scripts/leetcode_sync/client.py       <- LeetCode GraphQL client
scripts/leetcode_sync/repo.py         <- folder/README/code writer
scripts/leetcode_sync/sync.py         <- main entrypoint
requirements.txt                       <- Python deps (requests)
SETUP.md                                <- this file
```

If `requirements.txt` already exists in the repo, merge the `requests` line
into it instead of overwriting.

Commit and push these files to `AKSINGH-0704/DSA` (e.g. on `main`) - the
workflow only runs once it's on the default branch (or whichever branch
your repo's Actions run against).

## 2. Get your LeetCode session credentials

LeetCode has no official API, so this uses the same authenticated GraphQL
endpoint the website itself uses. You need two cookie values from a
logged-in browser session:

1. Log in to https://leetcode.com in Chrome/Firefox/Edge.
2. Open DevTools (`F12` or `Ctrl+Shift+I`) → **Application** (Chrome) or
   **Storage** (Firefox) tab → **Cookies** → `https://leetcode.com`.
3. Copy the **Value** of these two cookies:
   - `LEETCODE_SESSION`
   - `csrftoken`

Keep these secret - they grant access to your LeetCode account.

## 3. Add GitHub Secrets

In `AKSINGH-0704/DSA` on GitHub:

1. Go to **Settings → Secrets and variables → Actions → New repository secret**.
2. Add:
   - `LEETCODE_SESSION` = the cookie value from step 2
   - `LEETCODE_CSRF_TOKEN` = the `csrftoken` cookie value from step 2

## 4. Allow the workflow to push commits

The workflow uses the built-in `GITHUB_TOKEN` to commit/push, which requires
write access:

1. **Settings → Actions → General → Workflow permissions**.
2. Select **"Read and write permissions"**.
3. Save.

(If this repo has branch protection on `main` that blocks bot pushes,
you'll need to either allow the `github-actions[bot]` actor as an exception,
or use a personal access token stored as a secret and substitute it for
`GITHUB_TOKEN` in the checkout/push steps.)

## 5. How it runs

- **Schedule**: `0 * * * *` → every 1 hour (at the top of every hour UTC).
- **Incremental mode** (default, every scheduled run): scans the 10 most
  recent pages of submission history (200 submissions of any status). For
  each *accepted* one, it checks whether `<id>-<slug>/` already exists in
  the repo. If not, it fetches the problem statement + your code and creates
  the folder.
- **Backfill mode**: go to **Actions → LeetCode Sync → Run workflow**, tick
  **"Backfill ALL historical accepted submissions"**, and run. This paginates
  through your *entire* submission history once. Re-run it any time you
  suspect older problems are missing - already-present folders are skipped,
  so it's safe to re-run.
- **Incremental window**: runs every 1 hour and scans the 10 most recent
  pages (200 submissions), which always covers anything submitted since the
  last hourly tick.

## 6. Duplicate / no-op protection

- **Skip already-solved problems**: existence of `<id>-<slug>/` in the repo
  is the single source of truth. No separate state file to get out of sync.
- **No empty commits**: the workflow runs `git diff --cached --quiet` after
  the sync script; if nothing changed, it skips the commit/push step
  entirely. A run that finds nothing new produces **zero** commits.
- **No duplicate problems per run**: if you have multiple accepted
  submissions for the same problem, only the most recent is used.
- **Concurrency**: the workflow uses a concurrency group so two runs can
  never push at the same time.

## 7. What gets stored per problem

```
<questionFrontendId>-<title-slug>/
  README.md        <- problem title (linked), difficulty badge, full HTML statement
  <title-slug>.<ext> <- your accepted submission's source code
```

The file extension is derived from the submission's language (e.g. `python3`
→ `.py`, `cpp` → `.cpp`, `java` → `.java`). See `LANGUAGE_EXTENSIONS` in
`scripts/leetcode_sync/repo.py` to add more mappings if you submit in a
language not yet listed.

## 8. Running locally (optional)

```bash
pip install -r requirements.txt
export LEETCODE_SESSION="..."
export LEETCODE_CSRF_TOKEN="..."

# Run from the repo root so "<id>-<slug>/" existence checks are correct
python scripts/leetcode_sync/sync.py --repo-root .          # incremental
python scripts/leetcode_sync/sync.py --repo-root . --backfill  # full history
```

## 9. Troubleshooting / known limitations

- **"LeetCode session is not signed in" / HTTP 401/403/429**: your
  `LEETCODE_SESSION` cookie has expired or was invalidated (e.g. you logged
  out, changed your password, or LeetCode rotated sessions). Repeat step 2-3
  to refresh both secrets. LeetCode session cookies typically last weeks to
  months but aren't guaranteed.
- **This relies on an unofficial/undocumented LeetCode API.** It can change
  without notice, and LeetCode occasionally rate-limits or Cloudflare-blocks
  automated traffic, including from GitHub Actions IP ranges. If a run fails
  for this reason, it's usually transient - re-running the workflow
  (manually or at the next hourly tick) typically succeeds. The script retries
  each request a few times with backoff before giving up.
- **Code unavailable for old submissions**: if `submissionDetails` returns no
  code for a given submission (rare, but happens for very old or restricted
  submissions), that problem is skipped with a warning and retried on the
  next run (it won't have created a folder, so it isn't marked "done").
- **Root README badge ("Problems Solved: 130+")**: this is **not**
  auto-updated, to avoid fragile text-replacement on a hand-formatted file.
  Update it manually if you want the count to stay current.
