"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}
        
        curr = head
        copy_head, copy_tail = None, None
        while curr is not None:
            copy = Node(curr.val, None, curr.random)
            if copy_head is None:
                copy_head = copy
            if copy_tail is not None:
                copy_tail.next = copy
            copy_tail = copy
            mapping[curr] = copy
            curr = curr.next
        
        curr = copy_head
        while curr is not None:
            if curr.random is not None:
                curr.random = mapping[curr.random]
            curr = curr.next
        
        return copy_head

        
