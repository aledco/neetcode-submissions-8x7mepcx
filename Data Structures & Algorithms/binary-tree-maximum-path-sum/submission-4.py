# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        M = root.val

        def dfs(root):
            nonlocal M

            if root is None:
                return 0
            
            L = max(
                dfs(root.left),
                0
            )
            R = max(
                dfs(root.right),
                0
            )

            M = max(M, root.val + L + R)
            return root.val + max(L, R)

        dfs(root)
        return M
