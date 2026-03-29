class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def solve(P):
            m = 0
            i, j = 0, 1
            while j < len(P):
                if P[j] <= P[i]:
                    i = j
                else:
                    p = P[j] - P[i]
                    m = max(m, p)
                j += 1
            return m
        
        return solve(prices)
                