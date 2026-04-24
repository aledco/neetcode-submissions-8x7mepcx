# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = None
        last_k_tail = None
        curr = head
        while True:
            last = self.getLastInKGroup(curr, k)
            if last is None:
                if new_head is None:
                    return head
                else:
                    if last_k_tail is not None:
                        last_k_tail.next = curr
                    return new_head
                
            if new_head is None:
                new_head = last
            
            k_next = self.reverseK(curr, last)
            if last_k_tail is not None:
                last_k_tail.next = last
            last_k_tail = curr
            curr = k_next
    
    def getLastInKGroup(seld, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 1
        last = head
        while last is not None and i < k:
            last = last.next
            i += 1
        
        return last

    def reverseK(self, head: Optional[ListNode], last: Optional[ListNode]) -> Optional[ListNode]: #Tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
        prev, curr = None, head
        while True:
            temp = curr.next
            curr.next = prev
            if curr == last:
                return temp # last, head, temp
            prev, curr = curr, temp