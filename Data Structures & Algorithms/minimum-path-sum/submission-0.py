class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def dynamicProgramming(G):
            if len(G) == 0:
                return 0
            
            m, n = len(G), len(G[0])
            dp1 = [0] * n
            for i, x in enumerate(G[0]):
                dp1[i] = (dp1[i-1] if i > 0 else 0) + G[0][i]

            dp2 = [0] * n
            for i in range(1, m):
                for j in range(n):
                    dp2[j] = G[i][j] + dp1[j]
                    if j > 0:
                        dp2[j] = min(dp2[j], G[i][j] + dp2[j-1])
                dp1 = dp2
                dp2 = [0] * n
            return dp1[n-1]
        
        return dynamicProgramming(grid)