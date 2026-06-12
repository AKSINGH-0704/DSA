class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m = len(heights)
        n = len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def reaches_both(r0, c0):
            stack = [(r0, c0)]
            visited = set()
            visited.add((r0, c0))
            reach_pacific = False
            reach_atlantic = False

            while stack and not (reach_pacific and reach_atlantic):
                r, c = stack.pop()
                if r == 0 or c == 0:
                    reach_pacific = True
                if r == m - 1 or c == n - 1:
                    reach_atlantic = True
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if heights[nr][nc] <= heights[r][c] and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            stack.append((nr, nc))
            return reach_pacific and reach_atlantic

        result = []
        for r in range(m):
            for c in range(n):
                if reaches_both(r, c):
                    result.append([r, c])

        return result
