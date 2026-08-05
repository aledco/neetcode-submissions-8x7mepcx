class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # first find the points in the two islands, keeping track of the perimiters.
        # then find the two points on the perimeters that are closest in the two islands
        # then return the distance
        perimeters = []
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                if (i, j) in visited:
                    continue
                
                perimeter = self.traverseIsland(grid, i, j, visited)
                perimeters.append(perimeter)
        
        assert len(perimeters) == 2

        m = sys.maxsize
        for x1, y1 in perimeters[0]:
            for x2, y2 in perimeters[1]:
                d = abs(x2 - x1) + abs(y2 - y1) - 1
                m = min(m, d)
        return m
    
    def traverseIsland(self, grid: List[List[int]], i: int, j: int, visited: Set[Tuple[int]]) -> List[Tuple[int]]:
        from collections import deque

        def adj(grid, i, j):
            for d, e in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                x, y = i+d, j+e
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]):
                    yield x, y

        def isShore(grid, i, j):
            for x, y in adj(grid, i, j):
                if grid[x][y] == 0:
                    return True
            return False

        perimeter = []
        queue = deque([(i, j)])
        visited.add((i, j))
        while len(queue) > 0:
            i, j = queue.popleft()
            if isShore(grid, i, j):
                perimeter.append((i, j))
            for x, y in adj(grid, i, j):
                if grid[x][y] == 0 or (x, y) in visited:
                    continue
                queue.append((x, y))
                visited.add((x, y))
        return perimeter

