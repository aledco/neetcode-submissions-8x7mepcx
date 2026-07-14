# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == key:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                self.attachToLeft(root.right, root.left)
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def attachToLeft(self, root, sub):
        curr = root
        while curr.left is not None:
            curr = curr.left
        curr.left = sub