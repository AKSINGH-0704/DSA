class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        n = len(mat[0])
        
        for i in range(len(mat)):
            for j in range(n):
                if i % 2 == 0:
                    
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                  
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
                        
        return True