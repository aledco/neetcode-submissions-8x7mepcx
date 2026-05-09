class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def coords(G, i, j):
            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                if 0 <= i+x < len(G) and 0 <= j+y < len(G[i]):
                    yield i+x, j+y

        def multiSource_bfs(G):
            Q = deque([])
            V = set()
            for i in range(len(G)):
                for j in range(len(G[i])):
                    if G[i][j] == 2:
                        Q.append((i, j))
                        V.add((i, j))
            
            d = 0
            while True:
                nQ = deque([])
                while len(Q) > 0:
                    (i, j) = Q.popleft()
                    G[i][j] = 2
                    for x, y in coords(G, i, j):
                        if G[x][y] == 0:
                            continue
                        if (x, y) in V:
                            continue
                        nQ.append((x, y))
                        V.add((x, y))
                if len(nQ) == 0:
                    break
                
                Q = nQ
                d += 1

            for i in range(len(G)):
                for j in range(len(G[i])):
                    if G[i][j] == 1:
                        return -1
            
            return d
        
        return multiSource_bfs(grid)