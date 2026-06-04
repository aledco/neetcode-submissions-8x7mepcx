class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def matches(s, p, i, j):
            return i < len(s) and (s[i] == p[j] or p[j] == '.')

        def dfs(s, p, i=0, j=0):
            if j >= len(p):
                return i >= len(s)
            
            if j+1 < len(p) and p[j+1] == '*':
                return (
                    dfs(s, p, i, j+2) or # try zero matches
                    (
                        matches(s, p, i, j) and dfs(s, p, i+1, j)
                    ) # try 1 or more matches
                )
            elif matches(s, p, i, j):
                return dfs(s, p, i+1, j+1)
            else:
                return False
        
        # return dfs(s, p)

        def dynamicProgramming(s, p):
            # dp[i][j] = True if s[:i] matches p[:j]
            m, n = len(s), len(p)
            dp = [[False] * (n+1) for _ in range(m+1)]
            dp[m][n] = True # base case: "" matches ""
            for i in range(m, -1, -1):
                for j in range(n-1, -1, -1):
                    if j+1 < len(p) and p[j+1] == '*':
                        dp[i][j] = (
                            dp[i][j+2]
                            or (
                                matches(s, p, i, j) and
                                dp[i+1][j] 
                            ) # one or more matches
                        )
                    elif matches(s, p, i, j):
                        dp[i][j] = dp[i+1][j+1]
            # print(dp)
            return dp[0][0]
        
        return dynamicProgramming(s, p)

            

            