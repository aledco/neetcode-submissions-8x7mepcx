"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        old_to_new = {}
        new = set()

        def clone(node):
            nonlocal old_to_new
            nonlocal new

            if node is None:
                return node
                
            if node in new:
                return node
            
            if node in old_to_new:
                return old_to_new[node]
            
            cloned_node = Node(node.val)
            old_to_new[node] = cloned_node
            new.add(cloned_node)

            cloned_node.neighbors = [clone(n) for n in node.neighbors]
            
            return cloned_node
        
        return clone(node)
