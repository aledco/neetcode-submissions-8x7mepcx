class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        def dfs(S, T, i=0, j=0):
            if j >= len(T):
                return 1
            elif i >= len(S):
                return 0
            
            r = dfs(S, T, i+1, j)
            if S[i] == T[j]:
                r += dfs(S, T, i+1, j+1)
            return r
        
        # return dfs(s, t)

        def dynamicProgramming(S, T):
            # dp[i][j] = subsequences of S[:i] which are equal to T[:j]
            m, n = len(S), len(T)
            dp = [[0] * (n+1) for _ in range(m+1)]
            for i in range(m+1):
                dp[i][0] = 1
            for i in range(m):
                for j in range(n):
                    dp[i+1][j+1] = dp[i][j+1]
                    if S[i] == T[j]:
                        dp[i+1][j+1] += dp[i][j]
            return dp[m][n]
        
        # return dynamicProgramming(s, t)

        def dynamicProgramming_spaceOptimized(S, T):
            m, n = len(S), len(T)
            dp = [0] * (n+1)
            dp[0] = 1
            for i in range(m):
                p = 1
                for j in range(n):
                    r = dp[j+1]
                    if S[i] == T[j]:
                        r += p
                    p = dp[j+1]
                    dp[j+1] = r
            return dp[n]

        return dynamicProgramming_spaceOptimized(s, t)