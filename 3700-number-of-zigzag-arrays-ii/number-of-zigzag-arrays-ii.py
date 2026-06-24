class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        size = 2 * k

        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k_idx in range(size):
                    if A[i][k_idx] == 0: continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k_idx] * B[k_idx][j]) % MOD
            return C

        def power(A, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size): res[i][i] = 1
            while p > 0:
                if p % 2 == 1: res = multiply(res, A)
                A = multiply(A, A)
                p //= 2
            return res

        matrix = [[0] * size for _ in range(size)]
        for v in range(k):
            for u in range(k):
                if u < v: # Going down
                    matrix[v][k + u] = 1
                if u > v: # Going up
                    matrix[k + v][u] = 1
        
        # We need n-1 transitions for n elements
        final_matrix = power(matrix, n - 1)
        
        total = 0
        # Summing all transitions from initial state to all valid end states
        for i in range(size):
            for j in range(size):
                total = (total + final_matrix[i][j]) % MOD
                
        return total