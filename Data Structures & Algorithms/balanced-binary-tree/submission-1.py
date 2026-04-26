# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = True

        def dfs(root):
            nonlocal res

            if root is None:
                return 0
            
            L = dfs(root.left)
            R = dfs(root.right)
            if abs(L - R) > 1:
                res = False
            return max(L + 1, R + 1)
        
        dfs(root)
        return res