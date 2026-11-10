from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        parent = [0] * n
        pref = [0] * n
        timer = 0
        chars = list(s)

        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                tin[u] = timer
                timer += 1
                parent[u] = u if p == -1 else p
                pref[u] = (pref[p] if p != -1 else 0) ^ (1 << (ord(chars[u]) - 97))
                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        LOG = n.bit_length()
        up = [parent[:]]
        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        bit = [0] * (n + 2)

        def add(i, val):
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def get(i):
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return res

        def update_subtree(u, val):
            add(tin[u] + 1, val)
            add(tout[u] + 2, val)

        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                delta = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97))
                if delta:
                    update_subtree(u, delta)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                mask_u = pref[u] ^ get(tin[u] + 1)
                mask_v = pref[v] ^ get(tin[v] + 1)
                mask = mask_u ^ mask_v ^ (1 << (ord(chars[w]) - 97))
                ans.append((mask & (mask - 1)) == 0)

        return ans