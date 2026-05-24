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

        return bruteForce(nums)

        # S = [1] * len(nums)
        # for i, n in enumerate(nums):
        #     S[i] = S[i-1] * n

        # P = [1] * len(nums)
        # for i, n in enumerate(reversed(nums)):
        #     P[i] = P[i-1] * n
        # P = list(reversed(P))

        # m = min(nums)
        # for s, p in zip(S, P):
        #     m = max(m, s*p)
        # return m