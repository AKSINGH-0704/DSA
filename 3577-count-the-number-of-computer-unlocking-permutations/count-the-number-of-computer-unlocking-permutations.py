#aksingh
class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)

        vals = sorted(set(complexity))
        comp = [0]*n
        mp = {v:i for i,v in enumerate(vals)}
        for i,x in enumerate(complexity):
            comp[i] = mp[x]
        m = len(vals)

        INF = 10**9
        size = 1
        while size < m:
            size <<= 1
        seg = [INF] * (2*size)
        def seg_update(pos, val):
            i = pos + size
            if val < seg[i]:
                seg[i] = val
                i >>= 1
                while i:
                    seg[i] = seg[2*i] if seg[2*i] < seg[2*i+1] else seg[2*i+1]
                    i >>= 1
        def seg_query(l, r):
            if l > r:
                return INF
            l += size
            r += size
            res = INF
            while l <= r:
                if (l & 1) == 1:
                    if seg[l] < res:
                        res = seg[l]
                    l += 1
                if (r & 1) == 0:
                    if seg[r] < res:
                        res = seg[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        parent = [-1]*n
        seg_update(comp[0], 0)
        parent[0] = -1
        for i in range(1, n):
            q = seg_query(0, comp[i]-1)
            if q == INF:
                return 0
            parent[i] = q
            seg_update(comp[i], i)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        fact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % MOD
        invfact = [1]*(n+1)
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n,0,-1):
            invfact[i-1] = invfact[i]*i % MOD

        def dfs(u):
            total = 0
            ways = 1
            for v in children[u]:
                sz, w = dfs(v)
                total += sz
                ways = ways * w % MOD
            ways = ways * fact[total] % MOD
            for v in children[u]:
                sz, _ = dfs_cache[v]
                ways = ways * invfact[sz] % MOD
            dfs_cache[u] = (total+1, ways)
            return dfs_cache[u]

        dfs_cache = [None]*n
        dfs(0)
        return dfs_cache[0][1] % MOD
