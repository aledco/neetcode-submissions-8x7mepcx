from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def coords(G, i, j):
            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                if 0 <= i+x < len(G) and 0 <= j+y < len(G[i]):
                    yield i+x, j+y

        def multiSource_bfs(G):
            Q = deque([])
            V = set()
            for i in range(len(G)):
                for j in range(len(G[i])):
                    if G[i][j] == 0:
                        Q.append((i, j))
                        V.add((i, j))
            
            d = 0
            while len(Q) > 0:
                nQ = deque([])
                while len(Q) > 0:
                    (i, j) = Q.popleft()
                    G[i][j] = d
                    for x, y in coords(G, i, j):
                        if G[x][y] == -1:
                            continue
                        if (x, y) in V:
                            continue
                        nQ.append((x, y))
                        V.add((x, y))
                Q = nQ
                d += 1
        
        multiSource_bfs(grid)


        # # at each land, do a bfs for treasure, and count the distance

        # INF = 2147483647
                
        # def bfs(G, i, j):
        #     Q = deque([(i, j, 0)])
        #     V = {(i, j)}
        #     while len(Q) > 0:
        #         i, j, d = Q.popleft()
        #         for x, y in coords(G, i, j):
        #             if G[x][y] == -1:
        #                 continue
        #             if (x, y) in V:
        #                 continue
        #             if G[x][y] == 0:
        #                 return d+1
        #             Q.append((x, y, d+1))
        #             V.add((x, y))
            
        #     return INF
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] in (-1, 0):
        #             continue
        #         grid[i][j] = bfs(grid, i, j)
        