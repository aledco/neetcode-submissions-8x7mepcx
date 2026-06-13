from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.xaxis = defaultdict(set) # (x, y): self.xaxis[x] = {y}
        self.yaxis = defaultdict(set) # (x, y): self.yaxis[y] = {x}
        self.duplicates = defaultdict(int) # counts how many of each point have been added

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xaxis[x].add(y)
        self.yaxis[y].add(x)
        self.duplicates[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point

        c = 0
        for y2 in self.xaxis[x]:
            # (x, y) -> (x, y2) form a vertical line
            if y == y2: # skip squares of length 0
                continue
            
            
            for x2 in self.yaxis[y]:
                # (x, y) -> (x2, y) form a horizonal line of same length as (x, y) -> (x, y2)
                if abs(x2 - x) != abs(y2 - y): # skip rectangles
                    continue
                
                if y2 in self.xaxis[x2]:
                    # (x, y) -> (x, y2) -> (x2, y) -> (x2, y2) forms a square
                    # add the square to the count, accounting for duplicate points
                    d = (
                        max(
                            1,
                            self.duplicates[(x, y)]
                        ) 
                        * self.duplicates[(x, y2)]
                        * self.duplicates[(x2, y)]
                        * self.duplicates[(x2, y2)]
                    )
                    c += d
        return c


