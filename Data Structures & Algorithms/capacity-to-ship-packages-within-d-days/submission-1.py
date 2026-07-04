import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(W, d, m):
            c, s = 0, 1
            for w in W:
                if c + w > m:
                    s += 1
                    if s > d:
                        return False
                    c = 0
                c += w
            return s <= d
        
        max_weight = max(weights)
        if len(weights) <= days:
            return max_weight
        else:
            i, j = max_weight, max_weight * len(weights)
            res = j
            while i <= j:
                m = (i + j) // 2
                if canShip(weights, days, m):
                    res = m
                    j = m-1
                else:
                    i = m+1
            return res
