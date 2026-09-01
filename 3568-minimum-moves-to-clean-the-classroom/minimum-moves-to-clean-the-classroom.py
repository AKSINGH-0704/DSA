from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = {}
        start = None
        count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = count
                    count += 1

        if count == 0:
            return 0

        target = (1 << count) - 1

        queue = deque([(start[0], start[1], energy, 0, 0)])
        visited = {(start[0], start[1], energy, 0)}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, e, mask, moves = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X' or e == 0:
                    continue

                ne = e - 1
                nmask = mask

                if (nr, nc) in litter:
                    nmask |= 1 << litter[(nr, nc)]

                if nmask == target:
                    return moves + 1

                if classroom[nr][nc] == 'R':
                    ne = energy

                state = (nr, nc, ne, nmask)

                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, ne, nmask, moves + 1))

        return -1