class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def traverse(G, i, j, V):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return
            if grid[i][j] == "0":
                return
            if (i, j) in V:
                return
            V.add((i, j))
            traverse(G, i+1, j, V)
            traverse(G, i-1, j, V)
            traverse(G, i, j+1, V)
            traverse(G, i, j-1, V)


        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                if (i, j) in visited:
                    continue
                traverse(grid, i, j, visited)
                count += 1
        return count
                
                
