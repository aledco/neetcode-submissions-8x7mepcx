import sys

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(N, i=0, j=-1):
            if i >= len(N):
                return 0
            
            if j == -1 or N[i] > N[j]:
                return max(
                    dfs(N, i+1, i) + 1,
                    dfs(N, i+1, j)
                )
            return dfs(N, i+1, j)
        
        # return dfs(nums)

        def dynamicProgramming_topDown(N):
           
            cache = [[-1] * len(N) for _ in N]

            def dfs(N, i=0, j=-1):
                nonlocal cache

                if i >= len(N):
                    return 0

                if j > -1 and cache[j][i] > -1:
                    return cache[j][i]
                
                if j == -1 or N[i] > N[j]:
                    cache[j][i] = max(
                        dfs(N, i+1, i) + 1,
                        dfs(N, i+1, j)
                    )
                else:
                    cache[j][i] = dfs(N, i+1, j)
                return cache[j][i]
            
            return dfs(N)
        
        # return dynamicProgramming_topDown(nums)

        def dynamicProgramming_bottomUp(N):
            
            dp = [[0] * (len(N)+1) for _ in range(len(N)+1)]
            
            for i in range(len(N)-1, -1, -1):
                for j in range(i-1, -2, -1):
                    r = dp[i+1][j+1]

                    if j == -1 or N[i] > N[j]:
                        r = max(
                            r,
                            dp[i+1][i+1] + 1
                        )

                    dp[i][j+1] = r
            return dp[0][0]
        
        return dynamicProgramming_bottomUp(nums)