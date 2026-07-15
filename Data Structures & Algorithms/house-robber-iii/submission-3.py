# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root is None:
                return 0

            res = root.val
            if root.left is not None:
                res += dfs(root.left.left) + dfs(root.left.right)
            if root.right is not None:
                res += dfs(root.right.left) + dfs(root.right.right)
            
            return max(
                res,
                dfs(root.left) + dfs(root.right)
            )
        
        # return dfs(root)

        def dynamicProgramming(root):
            if root is None:
                return [0, 0]
            
            withL, withoutL = dynamicProgramming(root.left)
            withR, withoutR = dynamicProgramming(root.right)

            withRoot = withoutL + withoutR + root.val
            withoutRoot = max(withL, withoutL) + max(withR, withoutR)
            return [withRoot, withoutRoot]
        
        return max(dynamicProgramming(root))