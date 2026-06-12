"""
GraphQL client for LeetCode's unofficial API.

LeetCode does not publish an official API for submissions. This client talks
to the same GraphQL endpoint (https://leetcode.com/graphql) that the
leetcode.com website itself uses, authenticated as a logged-in user via the
LEETCODE_SESSION and csrftoken cookies (see SETUP.md for how to obtain them).

Because this is an unofficial/undocumented API, LeetCode can change its
schema or rate-limit/Cloudflare-block automated traffic at any time. If
requests start failing, check SETUP.md's troubleshooting section first.
"""

from __future__ import annotations

import time
from typing import Iterator, Optional

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

SUBMISSION_LIST_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $lastKey: String) {
  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
    lastKey
    hasNext
    submissions {
      id
      title
      titleSlug
      statusDisplay
      lang
      timestamp
    }
  }
}
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    content
  }
}
"""

SUBMISSION_DETAIL_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    lang {
      name
    }
  }
}
"""

USER_STATUS_QUERY = """
query globalData {
  userStatus {
    isSignedIn
    username
  }
}
"""


class LeetCodeAuthError(RuntimeError):
    """Raised when LeetCode rejects the configured session/csrf credentials."""


class LeetCodeClient:
    """Thin wrapper around LeetCode's GraphQL endpoint."""

    def __init__(self, session_cookie: str, csrf_token: str, request_delay: float = 1.0):
        self._delay = request_delay
        self._session = requests.Session()
        self._session.cookies.set("LEETCODE_SESSION", session_cookie, domain="leetcode.com")
        self._session.cookies.set("csrftoken", csrf_token, domain="leetcode.com")
        self._session.headers.update(
            {
                "Content-Type": "application/json",
                "Referer": "https://leetcode.com",
                "Origin": "https://leetcode.com",
                "x-csrftoken": csrf_token,
                "User-Agent": "Mozilla/5.0 (LeetCode-GitHub-Sync; +https://github.com)",
            }
        )

    def _post(self, query: str, variables: dict, retries: int = 3) -> dict:
        last_exc: Optional[Exception] = None
        for attempt in range(1, retries + 1):
            try:
                resp = self._session.post(
                    GRAPHQL_URL,
                    json={"query": query, "variables": variables},
                    timeout=30,
                )
            except requests.RequestException as exc:
                last_exc = exc
                time.sleep(self._delay * attempt)
                continue

            if resp.status_code == 200:
                payload = resp.json()
                if payload.get("errors"):
                    raise RuntimeError(f"LeetCode GraphQL error: {payload['errors']}")
                return payload["data"]

            if resp.status_code in (401, 403, 429):
                if attempt == retries:
                    raise LeetCodeAuthError(
                        f"LeetCode returned HTTP {resp.status_code} for {query.split()[1]}. "
                        "Your LEETCODE_SESSION / LEETCODE_CSRF_TOKEN secrets are likely "
                        "expired, invalid, or temporarily rate-limited - see SETUP.md."
                    )
                time.sleep(self._delay * attempt * 2)
                continue

            resp.raise_for_status()

        raise RuntimeError(f"LeetCode request failed after {retries} attempts") from last_exc

    def verify_auth(self) -> str:
        """Return the signed-in username, or raise LeetCodeAuthError."""
        data = self._post(USER_STATUS_QUERY, {})
        status = data.get("userStatus") or {}
        if not status.get("isSignedIn"):
            raise LeetCodeAuthError(
                "LeetCode session is not signed in. LEETCODE_SESSION / "
                "LEETCODE_CSRF_TOKEN secrets are missing, expired, or invalid."
            )
        return status.get("username") or "<unknown>"

    def iter_submissions(self, max_pages: Optional[int] = None, page_size: int = 20) -> Iterator[dict]:
        """
        Yield submissions newest-first.

        Stops when LeetCode reports no more pages, or once `max_pages` pages
        have been fetched - whichever comes first. `max_pages=None` means
        "fetch the entire submission history" (used for --backfill).
        """
        offset = 0
        last_key: Optional[str] = None
        page = 0
        while True:
            page += 1
            data = self._post(
                SUBMISSION_LIST_QUERY,
                {"offset": offset, "limit": page_size, "lastKey": last_key},
            )
            block = data["submissionList"]
            submissions = block.get("submissions") or []
            for sub in submissions:
                yield sub

            if not submissions or not block.get("hasNext"):
                break
            if max_pages is not None and page >= max_pages:
                break

            offset += page_size
            last_key = block.get("lastKey")
            time.sleep(self._delay)

    def get_question(self, title_slug: str) -> dict:
        data = self._post(QUESTION_QUERY, {"titleSlug": title_slug})
        question = data.get("question")
        if not question:
            raise RuntimeError(f"LeetCode returned no question data for '{title_slug}'")
        return question

    def get_submission_code(self, submission_id) -> Optional[tuple]:
        """Return (code, language_name) for a submission, or None if unavailable."""
        data = self._post(SUBMISSION_DETAIL_QUERY, {"submissionId": int(submission_id)})
        detail = data.get("submissionDetails")
        if not detail or not detail.get("code"):
            return None
        lang_name = (detail.get("lang") or {}).get("name", "")
        return detail["code"], lang_name
