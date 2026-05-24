import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def bruteForce(N):
            m = min(N)
            for i in range(len(N)):
                p = 1
                for j in range(i, len(N)):
                    p *= N[j]
                    m = max(m, p)
            return m

        # return bruteForce(nums)

        def dynamicProgramming(N):
            dp = [[0, 0] for _ in N]
            dp[0] = [N[0], N[0]]
            m = min(N)
            for i in range(1, len(N)):
                dp[i][0] = max(
                    dp[i-1][0] * N[i],
                    dp[i-1][1] * N[i],
                    N[i]
                )
                dp[i][1] = min(
                    dp[i-1][0] * N[i],
                    dp[i-1][1] * N[i],
                    N[i]
                )
                m = max(m, dp[i][0])
            return m

        return dynamicProgramming(nums)