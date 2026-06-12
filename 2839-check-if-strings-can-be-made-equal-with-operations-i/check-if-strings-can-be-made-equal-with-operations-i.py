class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        g1_s1 = sorted([s1[0], s1[2]])
        g1_s2 = sorted([s2[0], s2[2]])
        
        g2_s1 = sorted([s1[1], s1[3]])
        g2_s2 = sorted([s2[1], s2[3]])
        
        return g1_s1 == g1_s2 and g2_s1 == g2_s2