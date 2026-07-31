"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque
        
        if root is None:
            return None
        
        queue = deque([[root]])
        while len(queue) > 0:
            level = queue.popleft()
            for i in range(1, len(level)):
                level[i-1].next = level[i]
            
            next_level = []
            for n in level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            
            if len(next_level) > 0:
                queue.append(next_level)
        return root
        