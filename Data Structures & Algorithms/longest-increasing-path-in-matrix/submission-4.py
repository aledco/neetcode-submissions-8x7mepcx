class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def adj(M, i, j):
            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                if 0 <= i+x < len(M) and 0 <= j+y < len(M[i]):
                    yield i+x, j+y

        def dfs_solution(M):

            def dfs(M, i, j):
                d = 1
                for x, y in adj(M, i, j):
                    if M[x][y] > M[i][j]:
                        d = max(d, 1 + dfs(M, x, y))
                return d
            
            d = 0
            for i in range(len(M)):
                for j in range(len(M[i])):
                    d = max(
                        d,
                        dfs(M, i, j)
                    )
            return d

        # return dfs_solution(matrix)

        def dynamicProgramming_topDown_solution(M):
            
            dp = {}

            def dfs(M, i, j):
                nonlocal dp

                if (i, j) in dp:
                    return dp[(i, j)]
                
                d = 1
                for x, y in adj(M, i, j):
                    if M[x][y] > M[i][j]:
                        d = max(d, 1 + dfs(M, x, y))
                
                dp[(i, j)] = d
                return d
            
            d = 0
            for i in range(len(M)):
                for j in range(len(M[i])):
                    d = max(
                        d,
                        dfs(M, i, j)
                    )
            return d

        # return dynamicProgramming_topDown_solution(matrix)

        def topSort_solution(M):
            from collections import deque

            m, n = len(M), len(M[0])
            I = [[0] * n for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    for x, y in adj(M, i, j):
                        if M[x][y] < M[i][j]:
                            I[i][j] += 1

            Q = deque()
            for i in range(m):
                for j in range(n):
                    if I[i][j] == 0:
                        Q.append((i, j))
            
            d = 0
            while len(Q) > 0:
                nQ = deque()
                while len(Q) > 0:
                    i, j = Q.popleft()
                    for x, y in adj(M, i, j):
                        if M[x][y] > M[i][j]:
                            I[x][y] -= 1
                            if I[x][y] == 0:
                                nQ.append((x, y))
                Q = nQ
                d += 1
            return d

        return topSort_solution(matrix)


