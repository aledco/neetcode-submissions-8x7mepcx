# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    DELIMITER = ","

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = self.levelOrder_deconstruct(root)
        return self.DELIMITER.join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        L = data.split(self.DELIMITER)
        return self.levelOrder_reconstruct(L)
    

    def levelOrder_reconstruct(self, L: List[str]) -> Optional[TreeNode]:
        if len(L) == 0 or L[0] == "":
            return None

        root = TreeNode(int(L[0]))
        Q = deque([root])
        i = 1
        while len(Q) > 0:
            n = Q.popleft()
            if L[i] != "":
                n.left = TreeNode(int(L[i]))
                Q.append(n.left)
            i += 1
            if L[i] != "":
                n.right = TreeNode(int(L[i]))
                Q.append(n.right)
            i += 1
        return root
        
    def levelOrder_deconstruct(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        
        L = []
        Q = deque([root])
        while len(Q) > 0:
            n = Q.popleft()
            if n is None:
                L.append("")
            else:
                L.append(str(n.val))
                Q.append(n.left)
                Q.append(n.right)
        return L
        
        # level_vals = []
        # level = [root]
        # while level != []:
        #     vals = []
        #     next_level = []
        #     for node in level:
        #         vals.append(node.val)
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     level_vals.append(vals)
        #     level = next_level
        # return level_vals