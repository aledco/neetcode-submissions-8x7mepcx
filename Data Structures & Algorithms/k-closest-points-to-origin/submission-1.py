import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        H = []
        for [x, y] in points:
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            if len(H) < k:
                heapq.heappush_max(H, (d, [x, y]))
            else:
                heapq.heappushpop_max(H, (d, [x, y]))
        
        return [p for _, p in H]