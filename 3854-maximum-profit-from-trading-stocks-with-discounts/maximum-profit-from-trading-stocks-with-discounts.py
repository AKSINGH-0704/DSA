class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u-1].append(v-1)

        def combine(dp_acc, dp_child):
            new_dp = [-float('inf')] * (budget + 1)
            for w1 in range(budget + 1):
                if dp_acc[w1] == -float('inf'): continue
                for w2 in range(budget - w1 + 1):
                    if dp_child[w2] == -float('inf'): continue
                    
                    if dp_acc[w1] + dp_child[w2] > new_dp[w1 + w2]:
                        new_dp[w1 + w2] = dp_acc[w1] + dp_child[w2]
            return new_dp

        def dfs(u):
            acc_no_buy = [-float('inf')] * (budget + 1)
            acc_yes_buy = [-float('inf')] * (budget + 1)
            acc_no_buy[0] = 0
            acc_yes_buy[0] = 0
            
            for v in adj[u]:
                child_res = dfs(v)
                acc_no_buy = combine(acc_no_buy, child_res[0])
                acc_yes_buy = combine(acc_yes_buy, child_res[1])
            
            res0 = list(acc_no_buy)
            cost = present[u]
            profit = future[u] - present[u]
            if cost <= budget:
                for w in range(budget - cost + 1):
                    if acc_yes_buy[w] != -float('inf'):
                        res0[w + cost] = max(res0[w + cost], acc_yes_buy[w] + profit)

            res1 = list(acc_no_buy)
            cost = present[u] // 2
            profit = future[u] - cost
            if cost <= budget:
                for w in range(budget - cost + 1):
                    if acc_yes_buy[w] != -float('inf'):
                        res1[w + cost] = max(res1[w + cost], acc_yes_buy[w] + profit)
            
            return res0, res1

        final_dp = dfs(0)[0]
        
        return max(0, max(final_dp))