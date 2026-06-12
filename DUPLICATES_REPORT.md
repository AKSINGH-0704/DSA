# Duplicate Folder Report

**Date:** 2026-06-12  
**Status:** Preserved (no folders removed per repository policy)

---

## Background

The initial import (performed by LeetSync, a browser extension) used the
submission's **contest-round ID** as the folder number prefix.  When the
backfill ran using the official LeetCode GraphQL API, it used the permanent
`questionFrontendId` returned by the `questionData` query — which differs
from the contest-round ID for problems that were first released in a contest
and later added to the main problem set.

This caused 8 problems to receive a second folder under the API-assigned ID
alongside the original LeetSync folder.

---

## Duplicate Pairs

Each row shows the two folders that contain the same problem and the same
solution code.

| LeetSync folder (original) | API folder (backfill) | Slug |
|---|---|---|
| `2092-find-all-people-with-secret` | `2213-find-all-people-with-secret` | find-all-people-with-secret |
| `2110-number-of-smooth-descent-periods-of-a-stock` | `2233-number-of-smooth-descent-periods-of-a-stock` | number-of-smooth-descent-periods-of-a-stock |
| `2147-number-of-ways-to-divide-a-long-corridor` | `2251-number-of-ways-to-divide-a-long-corridor` | number-of-ways-to-divide-a-long-corridor |
| `3433-count-mentions-per-user` | `3721-count-mentions-per-user` | count-mentions-per-user |
| `3531-count-covered-buildings` | `3819-count-covered-buildings` | count-covered-buildings |
| `3562-maximum-profit-from-trading-stocks-with-discounts` | `3854-maximum-profit-from-trading-stocks-with-discounts` | maximum-profit-from-trading-stocks-with-discounts |
| `3573-best-time-to-buy-and-sell-stock-v` | `3892-best-time-to-buy-and-sell-stock-v` | best-time-to-buy-and-sell-stock-v |
| `3606-coupon-code-validator` | `3934-coupon-code-validator` | coupon-code-validator |

---

## Why future duplicates cannot occur

`repo.py::problem_exists()` now performs a two-layer check:

1. **Exact match** — `{questionFrontendId}-{slug}/` directory exists and
   contains `README.md`.
2. **Slug-pattern fallback** — any directory matching `^\d+-{slug}$` that
   contains `README.md`.

Layer 2 catches any pre-existing folder regardless of which numeric prefix it
carries, so no problem can be imported twice under two different IDs.

---

## Policy

Per repository policy established during the correctness-audit session
(2026-06-12), **no existing folders have been removed**.  Both the LeetSync
folder and the API folder remain in the repository.
