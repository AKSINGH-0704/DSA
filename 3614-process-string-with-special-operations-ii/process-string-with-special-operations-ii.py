class Solution:
    def processStr(self, s: str, k: int) -> str:
        ops = []
        curr_len = 0
        
        for char in s:
            if char == '*':
                if curr_len > 0: curr_len -= 1
                ops.append('*')
            elif char == '#':
                curr_len *= 2
                ops.append('#')
            elif char == '%':
                ops.append('%')
            else:
                curr_len += 1
                ops.append(('a', char))
                
        if k >= curr_len:
            return "."
            
        for op in reversed(ops):
            if op == '*':
                curr_len += 1
            elif op == '#':
                if k >= curr_len // 2:
                    k -= curr_len // 2
                curr_len //= 2
            elif op == '%':
                k = curr_len - 1 - k
            else:
                if k == curr_len - 1:
                    return op[1]
                curr_len -= 1
                
        return "."