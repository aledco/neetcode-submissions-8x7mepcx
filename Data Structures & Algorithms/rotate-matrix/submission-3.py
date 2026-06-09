class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # mc = [r.copy() for r in matrix] # TODO do in place, not with copy
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(n):
        #         matrix[j][n-1-i] = mc[i][j]

        import math

        n = len(matrix)
        m_floor = math.floor(n / 2)
        m_ceil = math.ceil(n / 2)
        for i in range(m_floor): 
            for j in range(m_ceil):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = temp
        
