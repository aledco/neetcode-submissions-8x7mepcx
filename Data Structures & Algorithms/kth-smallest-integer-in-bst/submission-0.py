# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(root, i=0):
            if root is None:
                return [None, 0]
            
            L = dfs(root.left, i)
            if L[0] is not None:
                return L
            
            i = i + L[1] + 1
            if i == k:
                return [root.val, 0]
            
            R = dfs(root.right, i)
            if R[0] is not None:
                return R
            
            return [None, L[1] + R[1] + 1]

        res = dfs(root)
        assert res[0] is not None
        return res[0]