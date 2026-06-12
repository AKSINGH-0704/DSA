from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    empty_cells.append((i, j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(idx=0):
            if idx == len(empty_cells):
                return True

            r, c = empty_cells[idx]
            box_index = (r // 3) * 3 + (c // 3)

            for ch in map(str, range(1, 10)):
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_index]:
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_index].add(ch)

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_index].remove(ch)

            return False

        backtrack()
