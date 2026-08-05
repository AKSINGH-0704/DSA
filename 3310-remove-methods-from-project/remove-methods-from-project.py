class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in invocations:
            g[a].append(b)

        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            u = stack.pop()
            for v in g[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    stack.append(v)

        for a, b in invocations:
            if suspicious[b] and not suspicious[a]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]