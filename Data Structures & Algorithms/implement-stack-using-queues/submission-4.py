from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        self._rotate()

    def _rotate(self):
        for _ in range(len(self.q)-1):
            self.q.append(
                self.q.popleft()
            )
        
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