# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        if root is None:
            return False
        
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        else:
            return (
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot)
            )
            
        


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            return q is None
        elif q is None:
            return p is None
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)