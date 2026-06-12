class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        for _ in range(9):
            rows.append(set())

        cols = []
        for _ in range(9):
            cols.append(set())

        boxes = []
        for _ in range(9):
            boxes.append(set())

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                if value in rows[i]:
                    return False
                rows[i].add(value)

                if value in cols[j]:
                    return False
                cols[j].add(value)

                box_index = (i // 3) * 3 + (j // 3)
                if value in boxes[box_index]:
                    return False
                boxes[box_index].add(value)

        return True
