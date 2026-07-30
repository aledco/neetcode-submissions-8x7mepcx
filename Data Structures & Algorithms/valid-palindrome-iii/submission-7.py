class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        from functools import cache

        @cache
        def dfs(i, j):
            nonlocal s
            if i > j:
                return 0
            
            if s[i] == s[j]:
                return dfs(i+1, j-1)

            return 1 + min(
                    dfs(i+1, j),
                    dfs(i, j-1)
                )
        
        # return dfs(0, len(s)-1) <= k

        def longestCommonSubsequence(s, r):
            m, n = len(s), len(r)
            dp = [[0] * (n+1) for _ in range(m+1)]
            
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if s[i-1] == r[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(
                            dp[i-1][j],
                            dp[i][j-1]
                        )
            return dp[m][n]
        

        def dynamicProgramming(s):
            return len(s) - longestCommonSubsequence(s, s[::-1])

        
        return dynamicProgramming(s) <= k