# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_index_map = {v: i for i, v in enumerate(inorder)}
        preorder_index = 0

        def dfs(l, r):
            nonlocal preorder_index

            if l > r:
                return None
            
            root_val = preorder[preorder_index]
            preorder_index += 1
            mid = inorder_index_map[root_val]
            return TreeNode(
                root_val,
                dfs(l, mid-1),
                dfs(mid+1, r)
            )

        return dfs(0, len(preorder) - 1)
