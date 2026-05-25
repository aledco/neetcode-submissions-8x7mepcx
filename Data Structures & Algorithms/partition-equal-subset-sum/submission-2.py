class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfs(N, i=0, s1=0, s2=0):
            
            if i >= len(N):
                return s1 == s2
            
            return (
                dfs(N, i+1, s1 + N[i], s2) or
                dfs(N, i+1, s1, s2 + N[i])
            )

        # return dfs(nums)

        def dfs_optmized(N, t, i=0, s=0):
            if t % 2 == 1:
                return False
            if s > t//2:
                return False
            if i >= len(N):
                return s == t//2
            
            return (
                dfs_optmized(N, t, i+1, s + N[i]) or
                dfs_optmized(N, t, i+1, s)
            )

        # return dfs_optmized(nums, sum(nums))

        def dynamicProgramming(N):
            t = sum(N)
            if t % 2 == 1:
                return False
            
            t = t // 2
            n = len(N)
            dp = [[False] * (t + 1) for _ in range(n + 1)]

            for i in range(n+1):
                dp[i][0] = True
            
            for i in range(1, n+1):
                for j in range(1, t+1):
                    if N[i-1] <= j:
                        dp[i][j] = (
                            dp[i-1][j] or # don't take N[i]
                            dp[i-1][j - nums[i-1]] # take N[i]
                        )
                    else:
                        dp[i][j] = dp[i-1][j]
            
            return dp[n][t]
            
        return dynamicProgramming(nums)

        