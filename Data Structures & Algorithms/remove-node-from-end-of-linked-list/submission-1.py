# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L = self.getLen(head)
        return self.removeNth(head, L-n+1)

    
    def removeNth(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr, i = None, head, 1
        while curr is not None and i < n:
            prev = curr
            curr = curr.next
            i += 1
        
        if prev is None and curr is None:
            return None
        elif prev is None:
            head = curr.next
            curr.next = None
            return head
        elif curr is None:
            prev.next = None
            return head
        else:
            prev.next = curr.next
            curr.next = None
            return head
    
    
    def getLen(self, head: Optional[ListNode]) -> int:
        curr, l = head, 0
        while curr is not None:
            curr = curr.next
            l += 1
        return l
        