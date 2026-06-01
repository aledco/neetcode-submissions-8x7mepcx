class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def dfs(w1, w2, i=0, j=0):
            if i >= len(w1):
                return len(w2)-j
            elif j >= len(w2):
                return len(w1)-i
            
            if w1[i] == w2[j]:
                return dfs(w1, w2, i+1, j+1)
            else: 
                return 1 + min(
                    dfs(w1, w2, i+1, j),
                    dfs(w1, w2, i, j+1),
                    dfs(w1, w2, i+1, j+1)
                )

        # return dfs(word1, word2)

        def dynamicProgramming(w1, w2):
            # dp[i][j] = minmum edit distance to convert w1[:i] into w2[:j]
            m, n = len(w1), len(w2)
            dp = [[0] * (n+1) for _ in range(m+1)]
            for i in range(m+1):
                dp[i][0] = i
            for j in range(n+1):
                dp[0][j] = j
            for i in range(m):
                for j in range(n):
                    if w1[i] == w2[j]:
                        dp[i+1][j+1] = dp[i][j]
                    else:
                        dp[i+1][j+1] = 1 + min(
                            dp[i][j+1],
                            dp[i+1][j],
                            dp[i][j]
                        )
            print(dp)
            return dp[m][n]
        
        return dynamicProgramming(word1, word2)