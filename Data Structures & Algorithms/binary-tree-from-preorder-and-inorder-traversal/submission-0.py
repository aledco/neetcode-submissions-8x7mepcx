# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root_val = preorder[0]
        inorder_mid = inorder.index(root_val)
        
        inorder_left = inorder[:inorder_mid]
        preorder_left = preorder[1:inorder_mid+1]

        inorder_right = inorder[inorder_mid+1:]
        preorder_right = preorder[inorder_mid+1:]

        return TreeNode(
            root_val,
            self.buildTree(preorder_left, inorder_left),
            self.buildTree(preorder_right, inorder_right)
        )
