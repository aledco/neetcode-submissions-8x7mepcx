# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while True:
            node, i = self.getMin(lists)
            if node is None:
                return dummy.next
            else:
                curr.next = node
                curr = node

                lists[i] = lists[i].next


    def getMin(self, lists: List[Optional[ListNode]]) -> Tuple[Optional[ListNode], int]:
        min_node, min_i = None, -1
        for i, node in enumerate(lists):
            if node is not None and (min_node is None or node.val < min_node.val):
                min_node, min_i = node, i
        return min_node, min_i
            

