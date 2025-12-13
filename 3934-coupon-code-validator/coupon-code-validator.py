class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        valid_coupons = []
        priority = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        
        for i in range(len(code)):
            c = code[i]
            b = businessLine[i]
            a = isActive[i]
            
            if not a:
                continue
            
            if b not in priority:
                continue
                
            if len(c) == 0:
                continue
                
            valid_char = True
            for char in c:
                if not char.isalnum() and char != '_':
                    valid_char = False
                    break
            
            if valid_char:
                valid_coupons.append([priority[b], c])
        
        valid_coupons.sort()
        
        result = []
        for item in valid_coupons:
            result.append(item[1])
            
        return result