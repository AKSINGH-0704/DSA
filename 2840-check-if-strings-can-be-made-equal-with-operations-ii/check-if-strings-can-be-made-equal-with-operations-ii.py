class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_s1 = []
        odd_s1 = []
        
        even_s2 = []
        odd_s2 = []
        
        for i in range(len(s1)):
            if i % 2 == 0:
                even_s1.append(s1[i])
                even_s2.append(s2[i])
            else:
                odd_s1.append(s1[i])
                odd_s2.append(s2[i])
                
        even_s1.sort()
        even_s2.sort()
        
        odd_s1.sort()
        odd_s2.sort()
        
        if even_s1 == even_s2 and odd_s1 == odd_s2:
            return True
        else:
            return False