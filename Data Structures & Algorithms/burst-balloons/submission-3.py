class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums_padded = [1] + nums + [1]

        def dfs(N, l, r):
            if l > r:
                return 0
            
            m = 0
            for i in range(l, r+1):
                c = N[l-1] * N[i] * N[r+1]
                c += dfs(N, l, i-1) + dfs(N, i+1, r)
                m = max(m, c)
            return m

        
        # return dfs(nums_padded, 1, len(nums_padded)-2)
        
        def dynamicProgramming(N):
            # dp[l][r] = maximum coins for the subproblem nums[l:r+1]

            n = len(N)
            dp = [[0] * n for _ in range(n)]
            for s in range(0, n-2):
                for l in range(1, n-1-s):
                    r = l + s
                    # print(l, r)
                    for i in range(l, r+1):
                        c = N[l-1] * N[i] * N[r+1]
                        c += dp[l][i-1] + dp[i+1][r]
                        dp[l][r] = max(dp[l][r], c)
            # print(dp)
            return dp[1][n-2]

        return dynamicProgramming(nums_padded)