class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        for i in range(m):
            empty_spot = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty_spot = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty_spot] = '#'
                    empty_spot -= 1
                    
        rotated_box = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = boxGrid[i][j]
                
        return rotated_box