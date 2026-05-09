from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # at each land, do a bfs for treasure, and count the distance

        INF = 2147483647

        def coords(G, i, j):
            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                if 0 <= i+x < len(G) and 0 <= j+y < len(G[i]):
                    yield i+x, j+y
                
        def bfs(G, i, j):
            Q = deque([(i, j, 0)])
            V = {(i, j)}
            while len(Q) > 0:
                i, j, d = Q.popleft()
                for x, y in coords(G, i, j):
                    if G[x][y] == -1:
                        continue
                    if (x, y) in V:
                        continue
                    if G[x][y] == 0:
                        return d+1
                    Q.append((x, y, d+1))
                    V.add((x, y))
            
            return INF
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in (-1, 0):
                    continue
                grid[i][j] = bfs(grid, i, j)
        