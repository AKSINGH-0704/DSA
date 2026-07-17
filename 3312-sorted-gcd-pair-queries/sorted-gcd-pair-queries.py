class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1
            
        gcd_c = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            m_c = sum(cnt[g::g])
            if m_c < 2:
                continue
            
            pairs = m_c * (m_c - 1) // 2
            
            for m in range(2 * g, mx + 1, g):
                pairs -= gcd_c[m]
            gcd_c[g] = pairs
            
        pre = [0] * (mx + 1)
        for i in range(1, mx + 1):
            pre[i] = pre[i-1] + gcd_c[i]
            
        return [bisect.bisect_right(pre, q) for q in queries]