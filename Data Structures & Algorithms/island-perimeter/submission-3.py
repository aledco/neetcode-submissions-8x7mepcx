class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def water(G, i, j):
            if i < 0 or i >= len(G) or j < 0 or j >= len(G[i]):
                return 1
            return 1 - G[i][j]

        def shores(G, i, j):
            if water(G, i, j) == 1:
                return 0
            return (
                water(G, i-1, j) +
                water(G, i+1, j) +
                water(G, i, j-1) +
                water(G, i, j+1)
            )

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j])
                res += shores(grid, i, j)
        return res