class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        from functools import cache

        def adj(heights, i, j):
            for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if 0 <= i+di < len(heights) and 0 <= j+dj < len(heights[i]):
                    yield i+di, j+dj

        @cache    
        def dfs(heights, i=0, j=0, visited=None):
            if i == len(heights)-1 and j == len(heights[0])-1:
                return 0

            if visited is None:
                visited = set()

            res = sys.maxsize
            for x, y in adj(heights, i, j):
                if (x, y) in visited:
                    continue
                
                res = min(
                    res,
                    max(
                        abs(heights[i][j] - heights[x][y]),
                        dfs(heights, x, y, visited | {(x, y)})
                    )
                )
            return res
        
        # return dfs(heights)

        # idea: convert into shortest path with weights, using abs difference between edges as weights

        def dijkstra(heights):
            import heapq

            if len(heights) == 0:
                return 0
            
            m, n = len(heights), len(heights[0])
            dist = [[sys.maxsize] * n for _ in range(m)]
            dist[0][0] = 0

            heap = []
            heapq.heappush(heap, (0, (0, 0)))

            while len(heap) > 0:
                d, (i, j) = heapq.heappop(heap)
                if d > dist[i][j]:
                    continue
                
                for x, y in adj(heights, i, j):
                    if max(dist[i][j], abs(heights[i][j] - heights[x][y])) < dist[x][y]:
                        dist[x][y] = max(dist[i][j], abs(heights[i][j] - heights[x][y]))
                        heapq.heappush(heap, (dist[x][y], (x, y)))
            return dist[m-1][n-1]
        
        return dijkstra(heights)

                    