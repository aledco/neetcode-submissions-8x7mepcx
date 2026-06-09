class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # [
        #     [x, y, z],
        #     [a, b, c],
        #     [u, v, w] 
        # ]

        # [
        #     [u, a, x],
        #     [v, b, y],
        #     [w, c, z]
        # ]

        # (0, 0) -> (0, 2) (i, j) -> (j, n-1-i)
        # (0, 1) -> (1, 2),
        # (0, 2) -> (2, 2),
        # (1, 0) -> (0, 1),
        # (1, 1) -> (1, 1),
        # (1, 2) -> (2, 1)
        # (2, 0) -> (0, 0)
        # (2, 1) -> (1, 0)
        # (2, 2) -> (2, 0)

        # [               (i = 0, j = 1)  
        #     [5,1,9,11], (0, 1) -> (2, 0) (n-j-1 = 4-1-1 = 2, i =9)
        #     [2,4,8,10],
        #     [13,3,6,7], (2, 0) -> (3, 2) -> (n-i-1 = 4-0-1 = 3, n-j-1 = 4-1-1 = 2)
        #     [15,14,12,16] (3, 2) -> (1, 3) -> (j = 1, n-i-1 = 4-0-1 = 3)
        # ]

        # [
        #     [15,13,2,5],
        #     [14,3,4,1],
        #     [12,6,8,9],
        #     [16,7,10,11]
        # ]

        # mc = [r.copy() for r in matrix] # TODO do in place, not with copy
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(n):
        #         matrix[j][n-1-i] = mc[i][j]

        import math

        # [.           (i = 0, j = 1)
        #     [1,2,3], (0, 1) -> (1, 0) (n-j-1 = 3-1-1 = 1, i = 0)
        #     [4,5,6], (1, 0) -> (2, 1) (n-i-1 = 3-0-1 = 2, n-j-1 = 3-1-1 = 1)
        #              (1, 2) -> (0, 1) (i = 0, j = 1) 
        #     [7,8,9]  (2, 1) -> (1, 2) (j, n-i-1 = 3-0-1 = 2)
        # ]

        # [
        #     [7,4,1],
        #     [8,5,2],
        #     [9,6,3]
        # ]

        n = len(matrix)
        m_floor = math.floor(n / 2)
        m_ceil = math.ceil(n / 2)

        # print(m)
        for i in range(m_floor): 
            for j in range(m_ceil):
                # print(
                #     i, j, n-i-1, n-j-1, "\n",
                #     "\t", matrix[i][j], "->", matrix[n-j-1][i], "\n",
                #     "\t", matrix[n-j-1][i], "->", matrix[n-i-1][n-j-1], "\n",
                #     "\t", matrix[n-i-1][n-j-1], "->", matrix[j][n-i-1], "\n",
                #     "\t", matrix[j][n-i-1], "->", matrix[i][j], "\n",
                # )
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = temp
        
        # [
        #     [1,2,3,4,5],
        #     [6,7,8,9,10],
        #     [11,12,13,14,15],
        #     [16,17,18,19,20],
        #     [21,22,23,24,25]
        # ]

        # [
        #     [21,16,11,6,1],
        #     [22,17,12,7,2],
        #     [23,18,13,8,3],
        #     [24,19,14,9,4],
        #     [25,20,15,10,5]
        # ]

        # if n % 2 == 1:
        #     temp = matrix[0][m]
        #     matrix[0][m] = matrix[m][0]
        #     matrix[m][0] = matrix[n-1][m]
        #     matrix[n-1][m] = matrix[m][n-1] 
        #     matrix[m][n-1] = temp
