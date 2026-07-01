from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        # if len(self.q) == 0:
        #     self.q.append(x)
        # else:
        #     y = self.q.popleft()
        #     self.push(x)
        #     self.q.append(y)

        self._reverse()
        self.q.append(x)
        self._reverse()

    def _reverse(self):
        if len(self.q) > 0:
            x = self.q.popleft()
            self._reverse()
            self.q.append(x) 
        
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return len(self.q) == 0

# class MyStack:
#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()

#     def push(self, x: int) -> None:
#         self.q2.append(x)
#         while len(self.q1) > 0:
#             self.q2.append(
#                 self.q1.popleft()
#             )
#         self.q1, self.q2 = self.q2, self.q1

#     def pop(self) -> int:
#         return self.q1.popleft()

#     def top(self) -> int:
#         return self.q1[0]
        
#     def empty(self) -> bool:
#         return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()