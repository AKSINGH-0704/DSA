class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        depth = [0] * (n + 1)
        LOG = 18
        up = [[0] * LOG for _ in range(n + 1)]
        
        def dfs(u, p, d):
            depth[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                up[u][i] = up[up[u][i-1]][i-1]
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
        
        dfs(1, 1, 0)
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
            
        res = []
        mod = 10**9 + 7
        for u, v in queries:
            lca = get_lca(u, v)
            l = depth[u] + depth[v] - 2 * depth[lca]
            if l == 0:
                res.append(0)
            else:
                res.append(pow(2, l - 1, mod))
        return res