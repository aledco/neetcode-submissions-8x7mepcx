import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        H = []
        for n in nums:
            if len(H) < k:
                heapq.heappush(H, n)
            else:
                heapq.heappushpop(H, n)
        
        return heapq.heappop(H)