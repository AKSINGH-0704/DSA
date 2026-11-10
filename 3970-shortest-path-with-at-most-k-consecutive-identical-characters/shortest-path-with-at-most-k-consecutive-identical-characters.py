import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            d, u, cnt = heapq.heappop(pq)

            if d != dist[u][cnt]:
                continue

            if u == n - 1:
                return d

            for v, w in adj[u]:
                new_cnt = cnt + 1 if labels[u] == labels[v] else 1

                if new_cnt <= k and d + w < dist[v][new_cnt]:
                    dist[v][new_cnt] = d + w
                    heapq.heappush(pq, (d + w, v, new_cnt))

        return -1