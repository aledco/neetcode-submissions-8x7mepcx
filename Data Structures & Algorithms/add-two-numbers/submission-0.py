# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s_head, s_tail = None, None
        c1, c2 = l1, l2
        over = 0
        while c1 is not None or c2 is not None:
            x = (
                c1.val if c1 else 0
            ) + (
                c2.val if c2 else 0
            ) + over
            if x >= 10:
                x -= 10
                over = 1
            else:
                over = 0
            
            n = ListNode(x)
            if s_head is None:
                s_head = n
            if s_tail is not None:
                s_tail.next = n
            s_tail = n

            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
        
        if over:
            s_tail.next = ListNode(over)
    
        return s_head