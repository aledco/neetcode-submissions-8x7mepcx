# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        from collections import deque

        Q = deque([([root], True)])
        while len(Q) > 0:
            level, complete = Q.popleft()
            next_level, next_complete = [], True
            for node in level:
                if node.left:
                    if not next_complete:
                        return False
                    next_level.append(node.left)     
                else:
                    next_complete = False
                
                if node.right:
                    if not next_complete:
                        return False
                    next_level.append(node.right)
                else:
                    next_complete = False

            if len(next_level) == 0:
                break

            if not complete:
                return False
            
            Q.append((next_level, next_complete))
        return True

