class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n = len(points)
        count = 0
        for i in range(n):
            p1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                
                p2 = points[j]
                
                if p1[0] <= p2[0] and p1[1] >= p2[1]:
                    is_valid_pair = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        
                        p3 = points[k]
                        
                        if p1[0] <= p3[0] <= p2[0] and p2[1] <= p3[1] <= p1[1]:
                            is_valid_pair = False
                            break
                    
                    if is_valid_pair:
                        count += 1
                        
        return count