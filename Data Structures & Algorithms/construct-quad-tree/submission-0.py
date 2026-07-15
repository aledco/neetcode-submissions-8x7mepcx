"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def divide(grid, r1, c1, r2, c2):
            if r1 == r2 and c1 == c2:
                return Node(grid[r1][c1] == 1, True, None, None, None, None)
            
            rm = (r1 + r2) // 2
            cm = (c1 + c2) // 2

            tl = divide(grid, r1, c1, rm, cm)
            tr = divide(grid, r1, cm+1, rm, c2)
            bl = divide(grid, rm+1, c1, r2, cm)
            br = divide(grid, rm+1, cm+1, r2, c2)

            # if all leaf nodes with the same val, combine into one large leaf node
            if (
                tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
                and tl.val == tr.val == bl.val == br.val
            ):
                return Node(tl.val, True, None, None, None, None)
            # else return parent node
            else:
                return Node(False, False, tl, tr, bl, br)
        
        if len(grid) == 0:
            return None
        return divide(grid, 0, 0, len(grid)-1, len(grid[0])-1)