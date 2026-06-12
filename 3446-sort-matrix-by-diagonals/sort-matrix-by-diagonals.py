import collections

class Solution:
  def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    diagonals = collections.defaultdict(list)

    for r in range(n):
      for c in range(n):
        diagonals[r - c].append(grid[r][c])

    for d in diagonals:
      if d >= 0:
        diagonals[d].sort(reverse=True)
      else:
        diagonals[d].sort()

    for r in range(n):
      for c in range(n):
        grid[r][c] = diagonals[r - c].pop(0)

    return grid