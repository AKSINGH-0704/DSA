class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        full_lakes = {}
        dry_days = []

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
            else:
                ans[i] = -1
                if lake in full_lakes:
                    last_rain_day = full_lakes[lake]
                    
                    j = bisect.bisect_right(dry_days, last_rain_day)
                    
                    if j == len(dry_days):
                        return []
                    
                    day_to_use = dry_days.pop(j)
                    ans[day_to_use] = lake
                    full_lakes[lake] = i
                else:
                    full_lakes[lake] = i
        
        return ans