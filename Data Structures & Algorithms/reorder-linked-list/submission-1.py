# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        
        prev, slow, fast = None, head, head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        L1, L2 = head, slow
        L2 = self.reverseList(L2)

        self.mergeTwoLists(L1, L2) 

    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        C, P = head, None
        while C is not None:
            N = C.next
            C.next = P
            P, C = C, N
        return P
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode], turn: int = 1) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if turn == 1:
                list1.next = self.mergeTwoLists(list1.next, list2, 2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next, 1)
                return list2



        
