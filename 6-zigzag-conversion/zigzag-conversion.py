class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        rows = [""] * numRows
        curr_row = 0
        step = 1
        
        for char in s:
            rows[curr_row] += char
            
            if curr_row == 0:
                step = 1
            elif curr_row == numRows - 1:
                step = -1
                
            curr_row += step
            
        return "".join(rows)