class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def traverse(G, i, j, V):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return 0
            if grid[i][j] == 0:
                return 0
            if (i, j) in V:
                return 0
            
            V.add((i, j))

            A = 1
            A += traverse(G, i+1, j, V)
            A += traverse(G, i-1, j, V)
            A += traverse(G, i, j+1, V)
            A += traverse(G, i, j-1, V)
            return A


        visited = set()
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                if (i, j) in visited:
                    continue
                area = traverse(grid, i, j, visited)
                max_area = max(max_area, area)
        return max_area