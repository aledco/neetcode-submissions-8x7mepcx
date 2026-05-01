# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        M = None

        def dfs(root):
            nonlocal M

            root_sums = [root.val]
            if root.left is None:
                L = 0
            else:
                L = dfs(root.left)
                root_sums.append(L + root.val)
            if root.right is None:
                R = 0
            else:
                R = dfs(root.right)
                root_sums.append(R + root.val)

            S = max(L + R + root.val, L + root.val, R + root.val, root.val)

            if M is None:
                M = S
            else:
                M = max(M, S)
            
            return max(root_sums)

        dfs(root)
        return M
