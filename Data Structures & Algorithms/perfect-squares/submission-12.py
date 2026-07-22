class Solution:
    def numSquares(self, n: int) -> int:
        import math
        from functools import cache

        @cache
        def dfs(n):
            if n == 0:
                return 0
            
            r = int(math.sqrt(n))
            q = int(math.sqrt(r))
            res = sys.maxsize
            for i in range(r, q-1, -1):
                res = min(
                    res,
                    1 + dfs(n-i*i)
                )
            return res
        
        return dfs(n)
        
        def dynamicProgramming(n):
            dp = [n] * (n+1)
            dp[0] = 0

            for i in range(1, n+1):
                q = int(math.sqrt(i))
                for r in range(q, i+1):
                    s = r*r
                    if s <= n:
                        dp[i] = min(dp[i], 1 + dp[i-s])
            return dp[n]
        
        return dynamicProgramming(n)

                
            
