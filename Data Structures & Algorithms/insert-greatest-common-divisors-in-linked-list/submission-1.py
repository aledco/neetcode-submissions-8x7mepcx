# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math

        if head is None:
            return None
        
        curr = head
        while curr.next is not None:
            g = math.gcd(curr.val, curr.next.val)
            n = ListNode(g, curr.next)
            curr.next = n
            curr = n.next
        return head