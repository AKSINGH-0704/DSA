class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_land = min(s + d for s, d in zip(landStartTime, landDuration))
        min_water = min(s + d for s, d in zip(waterStartTime, waterDuration))
        
        ans1 = min(max(min_land, s) + d for s, d in zip(waterStartTime, waterDuration))
        ans2 = min(max(min_water, s) + d for s, d in zip(landStartTime, landDuration))
        
        return min(ans1, ans2)