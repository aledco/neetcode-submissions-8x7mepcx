# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traversal(root):
            if root is None:
                return []
            
            return (
                traversal(root.left)
                + [root.val]
                + traversal(root.right)
            )
        
        return traversal(root)