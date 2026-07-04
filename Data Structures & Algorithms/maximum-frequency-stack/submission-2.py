import heapq
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.stacks = []
        self.counts = defaultdict(int)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1
        if self.counts[val] > self.max_count:
            self.max_count = self.counts[val]
            self.stacks.append([])
        self.stacks[self.counts[val]-1].append(val)

    def pop(self) -> int:
        stack = self.stacks.pop()
        val = stack.pop()
        self.counts[val] -= 1
        if len(stack) == 0:
            self.max_count -= 1
        else:
            self.stacks.append(stack)
        return val

    # def __init__(self):
    #     self.heap = []
    #     self.counts = defaultdict(int)
    #     self.index = 0

    # def push(self, val: int) -> None:
    #     self.counts[val] += 1
    #     heapq.heappush_max(
    #         self.heap,
    #         (self.counts[val], self.index, val)
    #     )
    #     self.index += 1

    # def pop(self) -> int:
    #     _, _, v = heapq.heappop_max(self.heap)
    #     self.counts[v] -= 1
    #     return v


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()