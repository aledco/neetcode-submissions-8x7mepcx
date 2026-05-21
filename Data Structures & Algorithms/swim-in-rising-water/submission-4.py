import sys
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def adj(G, i, j):
            for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                if 0 <= i+x < len(G) and 0 <= j+y < len(G[i]):
                    yield i+x, j+y

        path_time = [[sys.maxsize for _ in range(len(grid[i]))] for i in range(len(grid))]
        pQ = []
        heapq.heappush(pQ, (grid[0][0], (0, 0)))
        while len(pQ) > 0:
            t, (i, j) = heapq.heappop(pQ)
            if t > path_time[i][j]:
                continue
            for x, y in adj(grid, i, j):
                if max(t, grid[x][y]) < path_time[x][y]:
                    path_time[x][y] = max(t, grid[x][y])
                    heapq.heappush(pQ, (path_time[x][y], (x, y)))
                if x == len(grid)-1 and y == len(grid[x]) - 1:
                    return path_time[-1][-1]
        # return path_time[-1][-1]
