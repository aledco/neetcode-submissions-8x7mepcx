# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        M = 0

        def helper(root):
            nonlocal M

            if root is None:
                return
            
            L = self.maxDepth(root.left)
            R = self.maxDepth(root.right)
            M = max(M, L + R)
            # print(root.val, L, R, L+R, M)

            helper(root.left)
            helper(root.right)
        
        helper(root)
        return M

    


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        L = self.maxDepth(root.left)
        R = self.maxDepth(root.right)
        return max(L, R) + 1