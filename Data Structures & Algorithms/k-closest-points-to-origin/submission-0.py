import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        H = []
        for [x, y] in points:
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            heapq.heappush(H, (d, [x, y]))
        
        return [heapq.heappop(H)[1] for i in range(k)]