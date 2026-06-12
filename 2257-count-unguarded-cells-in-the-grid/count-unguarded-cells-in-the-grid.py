class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guard_set: Set[Tuple[int,int]] = { (r,c) for r,c in guards }
        wall_set: Set[Tuple[int,int]] = { (r,c) for r,c in walls }
        guarded: Set[Tuple[int,int]] = set()

        # helper to scan in one direction from a guard
        def scan(r: int, c: int, dr: int, dc: int) -> None:
            r += dr
            c += dc
            while 0 <= r < m and 0 <= c < n:
                if (r,c) in wall_set or (r,c) in guard_set:
                    break
                guarded.add((r,c))
                r += dr
                c += dc

        for r, c in guard_set:
            scan(r, c, -1, 0)  # up
            scan(r, c, 1, 0)   # down
            scan(r, c, 0, -1)  # left
            scan(r, c, 0, 1)   # right

        total_cells = m * n
        occupied = len(guard_set) + len(wall_set)
        unoccupied = total_cells - occupied
        # guarded only contains unoccupied cells by construction
        unguarded = unoccupied - len(guarded)
        return unguarded
