class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def dfs(i, j, alice):
            if i > j:
                return 0
            
            if alice == 1:
                res = max(
                    dfs(i+1, j, 0) + piles[i],
                    dfs(i, j+1, 0) + piles[j]
                )
            else:
                res = min(
                    dfs(i+1, j, 1) - piles[i],
                    dfs(i, j+1, 1) - piles[j]
                )
            return res

        # return dfs(0, len(piles)-1, 1)

        return True
            

