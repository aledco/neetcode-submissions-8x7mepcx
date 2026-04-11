class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        def canEat(P, h, k):
            for p in P:
                h -= math.ceil(p / k)
                if h < 0:
                    return False
            return True

        

        def binSearch(P, h, i, j, M):
            if i >= j:
                return M
            
            m = (j + i) // 2
            if canEat(P, h, m):
                return binSearch(P, h, i, m, m)
            else:
                return binSearch(P, h, m+1, j, M)
        
        M = max(piles)
        return binSearch(piles, h, 1, M+1, M)
