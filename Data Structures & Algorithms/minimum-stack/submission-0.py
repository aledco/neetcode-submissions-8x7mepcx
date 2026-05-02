class MinStack:

    def __init__(self):
       self.S = []
       self.M = [] 

    def push(self, val: int) -> None:
        self.S.append(val)
        if len(self.M) == 0:
            self.M.append(val)
        else:
            self.M.append(min(val, self.M[-1]))

    def pop(self) -> None:
        self.M.pop()
        return self.S.pop()
        

    def top(self) -> int:
        return self.S[-1]

    def getMin(self) -> int:
        return self.M[-1]
