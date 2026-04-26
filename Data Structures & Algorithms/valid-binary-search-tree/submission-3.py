# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, m, n):
            if root is None:
                return True
            
            if root.val <= m or root.val >= n:
                return False
            
            if root.left is not None and root.left.val >= root.val:
                return False
            
            if root.right is not None and root.right.val <= root.val:
                return False
            
            return dfs(root.left, m, root.val) and dfs(root.right, root.val, n)
        
        return dfs(root, -1001, 1001)