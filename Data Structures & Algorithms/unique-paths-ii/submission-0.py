class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def dynamicProgramming(G):
            # dp[i][j] = # of unique paths to G[i][j]
            # dp[i][j] = dp[i-1][j] + dp[i][j-1]
            if G[0][0] == 1:
                return 0

            m, n = len(G), len(G[0])
            dp1 = [0] * n
            dp2 = [0] * n
            
            # i = 0
            # while i < n and dp1[i] == 0:
            #     dp1[i] = 1
            #     i += 1
            
            dp1[0] = 1
            for i in range(0, m):
                for j in range(n):
                    if G[i][j] == 1:
                        dp2[j] = 0
                    else:
                        dp2[j] = dp1[j]
                        if j-1 >= 0:
                            dp2[j] += dp2[j-1]
                dp1 = dp2
                dp2 = [0] * n
            return dp1[n-1]
        
        return dynamicProgramming(obstacleGrid)
                    

            

            

