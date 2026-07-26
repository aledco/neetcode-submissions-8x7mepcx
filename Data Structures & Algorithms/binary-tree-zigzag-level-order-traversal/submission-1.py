# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if root is None:
            return []
        
        res = []
        queue = deque([([root], 1)])
        while len(queue) > 0:
            level, d = queue.popleft()
            # if d == -1:
            #     level = reversed(level)

            res.append([n.val for n in level])

            next_level = []
            def add(node):
                nonlocal next_level
                if node:
                    next_level.append(node)

            for node in level:
                #if d == 1:
                add(node.left)
                add(node.right)
                #else:
                    # add(node.right)
                    # add(node.left)

            if len(next_level) > 0:
                queue.append((next_level, -d))

        for i in range(1, len(res), 2):
            res[i] = list(reversed(res[i]))
        return res