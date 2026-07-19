from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.total = 0
        self.window = deque()
        

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            last = self.window.popleft()
            self.total -= last

        self.total += val
        self.window.append(val)
        return self.total / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
