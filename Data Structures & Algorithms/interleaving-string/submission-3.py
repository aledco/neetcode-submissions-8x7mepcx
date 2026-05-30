class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        def dfs(s1, s2, s3, i=0, j=0, k=0):
            if k >= len(s3):
                return True

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(s1, s2, s3, i+1, j, k+1):
                    return True
            
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(s1, s2, s3, i, j+1, k+1):
                    return True
            
            return False
        
        # return dfs(s1, s2, s3)

        def dynamicProgramming(s1, s2, s3):
            # dp[i][j] is True if s1[:i] and s2[:j] successfully interleave s3[:i+j]
            m, n = len(s1), len(s2)
            dp = [[False] * (n+1) for _ in range(m+1)]
            dp[m][n] = True
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i < m and s1[i] == s3[i+j] and dp[i+1][j]:
                        dp[i][j] = True

                    if j < n and s2[j] == s3[i+j] and dp[i][j+1]:
                        dp[i][j] = True

            return dp[0][0]

        return dynamicProgramming(s1, s2, s3)
