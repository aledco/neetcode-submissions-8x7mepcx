import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(M):
            m, n = len(M), len(M[0])
            for i in range(math.ceil(m / 2)):
                if n-i-1 < i:
                    continue
                for j in range(i, n-i):
                    yield M[i][j]

                if m-i-1 < i+1:
                    continue
                for j in range(i+1, m-i):
                    yield M[j][n-i-1]

                if i > n-i-2:
                    continue
                for j in range(n-i-2, i-1, -1):
                    yield M[m-i-1][j]

                if i+1 > m-i-2:
                    continue
                for j in range(m-i-2, i, -1):
                    yield M[j][i]
        
        return [x for x in spiral(matrix)]

