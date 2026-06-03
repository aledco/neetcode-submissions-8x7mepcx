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
            dp[0][0] = True # base case: "" matches ""
            for i in range(m):
                for j in range(n):
                    if p[j] == '*':
                        dp[i+1][j+1] = dp[i+1][j]
                        continue
                    
                    if j+1 < len(p) and p[j+1] == '*': # TODO this case is wrong
                        dp[i+1][j+1] = (
                            dp[i+1][j] # zero matches
                            or (matches(s, p, i, j) and dp[i][j+1]) # one or more matches
                        )
                    elif matches(s, p, i, j):
                        dp[i+1][j+1] = dp[i][j]
            print(dp)
            return dp[m][n]
        
        return dynamicProgramming(s, p)

            

            