class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        s_tl = [[0] * (m + 2) for _ in range(n + 2)]
        s_tr = [[0] * (m + 2) for _ in range(n + 2)]
        s_bl = [[0] * (m + 2) for _ in range(n + 2)]
        s_br = [[0] * (m + 2) for _ in range(n + 2)]
        
        v_tl = [[0] * (m + 2) for _ in range(n + 2)]
        v_tr = [[0] * (m + 2) for _ in range(n + 2)]
        v_bl = [[0] * (m + 2) for _ in range(n + 2)]
        v_br = [[0] * (m + 2) for _ in range(n + 2)]

        def check(length, value):
            if length == 1:
                return value == 1
            if length > 1:
                return value == 2 if length % 2 == 0 else value == 0
            return False

        max_len = 0

        for r in range(1, n + 1):
            for c in range(1, m + 1):
                val = grid[r - 1][c - 1]
                prev_len = s_tl[r - 1][c - 1]
                if check(prev_len + 1, val):
                    s_tl[r][c] = prev_len + 1
                elif check(1, val):
                    s_tl[r][c] = 1
                max_len = max(max_len, s_tl[r][c])
        
        for r in range(1, n + 1):
            for c in range(m, 0, -1):
                val = grid[r - 1][c - 1]
                prev_len = s_tr[r - 1][c + 1]
                if check(prev_len + 1, val):
                    s_tr[r][c] = prev_len + 1
                elif check(1, val):
                    s_tr[r][c] = 1
                max_len = max(max_len, s_tr[r][c])

        for r in range(n, 0, -1):
            for c in range(1, m + 1):
                val = grid[r - 1][c - 1]
                prev_len = s_bl[r + 1][c - 1]
                if check(prev_len + 1, val):
                    s_bl[r][c] = prev_len + 1
                elif check(1, val):
                    s_bl[r][c] = 1
                max_len = max(max_len, s_bl[r][c])

        for r in range(n, 0, -1):
            for c in range(m, 0, -1):
                val = grid[r - 1][c - 1]
                prev_len = s_br[r + 1][c + 1]
                if check(prev_len + 1, val):
                    s_br[r][c] = prev_len + 1
                elif check(1, val):
                    s_br[r][c] = 1
                max_len = max(max_len, s_br[r][c])
        
        for r in range(1, n + 1):
            for c in range(1, m + 1):
                val = grid[r-1][c-1]
                cand1, cand2 = 0, 0
                prev_v = v_tl[r - 1][c - 1]
                if prev_v > 0 and check(prev_v + 1, val):
                    cand1 = prev_v + 1
                prev_s_turn = s_bl[r - 1][c - 1]
                if prev_s_turn > 0 and check(prev_s_turn + 1, val):
                    cand2 = prev_s_turn + 1
                v_tl[r][c] = max(cand1, cand2)
                max_len = max(max_len, v_tl[r][c])

        for r in range(1, n + 1):
            for c in range(m, 0, -1):
                val = grid[r-1][c-1]
                cand1, cand2 = 0, 0
                prev_v = v_tr[r - 1][c + 1]
                if prev_v > 0 and check(prev_v + 1, val):
                    cand1 = prev_v + 1
                prev_s_turn = s_tl[r - 1][c + 1]
                if prev_s_turn > 0 and check(prev_s_turn + 1, val):
                    cand2 = prev_s_turn + 1
                v_tr[r][c] = max(cand1, cand2)
                max_len = max(max_len, v_tr[r][c])

        for r in range(n, 0, -1):
            for c in range(1, m + 1):
                val = grid[r-1][c-1]
                cand1, cand2 = 0, 0
                prev_v = v_bl[r + 1][c - 1]
                if prev_v > 0 and check(prev_v + 1, val):
                    cand1 = prev_v + 1
                prev_s_turn = s_br[r + 1][c - 1]
                if prev_s_turn > 0 and check(prev_s_turn + 1, val):
                    cand2 = prev_s_turn + 1
                v_bl[r][c] = max(cand1, cand2)
                max_len = max(max_len, v_bl[r][c])

        for r in range(n, 0, -1):
            for c in range(m, 0, -1):
                val = grid[r-1][c-1]
                cand1, cand2 = 0, 0
                prev_v = v_br[r + 1][c + 1]
                if prev_v > 0 and check(prev_v + 1, val):
                    cand1 = prev_v + 1
                prev_s_turn = s_tr[r + 1][c + 1]
                if prev_s_turn > 0 and check(prev_s_turn + 1, val):
                    cand2 = prev_s_turn + 1
                v_br[r][c] = max(cand1, cand2)
                max_len = max(max_len, v_br[r][c])
        
        return max_len