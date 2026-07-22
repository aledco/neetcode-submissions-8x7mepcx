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
        
        # def dynamicProgramming(n):
            