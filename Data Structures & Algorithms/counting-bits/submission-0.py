import math

class Solution:
    def countBits(self, n: int) -> List[int]:
        def dynamicProgramming(n):
            p = 1
            dp = [0] * (n+1)
            for i in range(1, n+1):
                if i == p * 2:
                    p *= 2
                dp[i] = dp[i-p] + 1
            return dp
        
        return dynamicProgramming(n)
            