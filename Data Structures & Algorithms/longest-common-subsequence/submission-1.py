class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(S, T, i=0, j=0):
            if i >= len(S) or j >= len(T):
                return 0
            
            r = max(
                dfs(S, T, i+1, j),
                dfs(S, T, i, j+1)
            )
            if S[i] == T[j]:
                r  = max(r, 1 + dfs(S, T, i+1, j+1))
            return r

        # return dfs(text1, text2)

        def dynamicProgramming(S, T):
            # dp[i][j] represents the longest common subsequence of the prefix of S with length i and prefix of T with length j
            dp = [[0] * (len(T)+1) for _ in range(len(S)+1)]
            for i in range(len(S)):
                for j in range(len(T)):
                    dp[i+1][j+1] = max(
                        dp[i][j+1],
                        dp[i+1][j]
                    )
                    if S[i] == T[j]:
                        dp[i+1][j+1] = max(
                            dp[i+1][j+1],
                            1 + dp[i][j]
                        )
            return dp[len(S)][len(T)]
        
        return dynamicProgramming(text1, text2)