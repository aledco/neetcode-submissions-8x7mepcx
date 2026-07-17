class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(n, k, i=1):
            if k == 0:
                yield []
            
            for j in range(i, n+1):
                for arr in dfs(n, k-1, j+1):
                    yield [j] + arr
        
        return [x for x in dfs(n, k)]

