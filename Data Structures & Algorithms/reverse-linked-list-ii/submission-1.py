# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr, left_node, right_node = head, None, None
        for i in range(1, right+1):
            if i == left:
                left_node = curr
            if i == right:
                right_node = curr
            curr = curr.next

        curr_left = left_node
        while curr_left != right_node:
            next_left = curr_left.next
            curr_left.next = right_node.next
            right_node.next = curr_left
            curr_left = next_left

        if left_node == head:
            return right_node
        else:
            curr = head
            while curr.next != left_node:
                curr = curr.next
            curr.next = right_node
            return head