class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.')))
    
        max_length = max(len(v1_parts), len(v2_parts))
    
        for i in range(max_length):
        
            v1_val = v1_parts[i] if i < len(v1_parts) else 0
            v2_val = v2_parts[i] if i < len(v2_parts) else 0
        
            if v1_val < v2_val:
                return -1
            elif v1_val > v2_val:
                return 1
        return 0


        