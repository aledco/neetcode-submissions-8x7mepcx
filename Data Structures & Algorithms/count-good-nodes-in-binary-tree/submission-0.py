# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, m=None):
            res = 0

            if root is None:
                return res
            
            if m is None:
                m = root.val
                res += 1
            else:
                if root.val >= m:
                    res += 1
                m = max(m, root.val)

            res += dfs(root.left, m)
            res += dfs(root.right, m)
            return res
        
        return dfs(root)