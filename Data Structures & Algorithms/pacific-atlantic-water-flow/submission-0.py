class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def coords(H, i, j, V):
            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                if 0 <= i+x < len(H) and 0 <= j+y < len(H[i]):
                    if H[i+x][j+y] >= H[i][j] and (i+x, j+y) not in V:
                        yield i+x, j+y
            
        def dfs(H, V):
            S = list(V)
            while len(S) > 0:
                i, j = S.pop()
                for x, y in coords(H, i, j, V):
                    V.add((x, y))
                    S.append((x, y))
            return V

        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n-1))  
        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m-1, j))

        pacific = dfs(heights, pacific)
        atlantic = dfs(heights, atlantic)
        return [
            list(x) for x in
            pacific.intersection(atlantic)
        ]