import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        
        nums = list(sorted(nums))
        if len(nums) <= k:
            self.H = nums
        else:
            self.H = list(sorted(nums))[len(nums)-k:]
        

    def add(self, val: int) -> int:
        if len(self.H) < self.k:
            heapq.heappush(self.H, val)
        else:
            heapq.heappushpop(self.H, val)
        return self.H[0]
