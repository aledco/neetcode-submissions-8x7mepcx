# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        def dfs(head, val):
            if head is None:
                return None
            
            head.next = dfs(head.next, val)
            if head.val == val:
                return head.next
            return head
        
        return dfs(head, val)