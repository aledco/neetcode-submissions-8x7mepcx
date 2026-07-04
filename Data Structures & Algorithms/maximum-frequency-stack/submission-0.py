class FreqStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        from collections import defaultdict

        mc, mv = 0, 0
        counts = defaultdict(int)
        for v in self.stack:
            counts[v] += 1
            if counts[v] >= mc:
                mc, mv = counts[v], v
        
        i = len(self.stack)-1
        while i >= 0 and self.stack[i] != mv:
            i -= 1
        self.stack.pop(i)
        return mv


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()