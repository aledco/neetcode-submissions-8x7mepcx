class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0:
            return []
        
        m, n = len(matrix), len(matrix[0])
        tmatrix = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                tmatrix[j][i] = matrix[i][j]
        return tmatrix