import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        # add num to heaps
        if len(self.left) == 0 or num <= self.left[0]:
            heapq.heappush_max(self.left, num)
        elif len(self.right) == 0 or num >= self.right[0]:
            heapq.heappush(self.right, num)
        else:
            if len(self.left) <= len(self.right):
                heapq.heappush_max(self.left, num)
            else:
                heapq.heappush(self.right, num)
        
        # balance heaps
        if len(self.left) < len(self.right)-1:
            while len(self.left) < len(self.right)-1:
                t = heapq.heappop(self.right)
                heapq.heappush_max(self.left, t)
        elif len(self.right) < len(self.left)-1:
            while len(self.right) < len(self.left)-1:
                t = heapq.heappop_max(self.left)
                heapq.heappush(self.right, t)

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 1:
            if len(self.left) > len(self.right):
                return self.left[0]
            else:
                return self.right[0]
        else:
            return (self.left[0] + self.right[0]) / 2
        