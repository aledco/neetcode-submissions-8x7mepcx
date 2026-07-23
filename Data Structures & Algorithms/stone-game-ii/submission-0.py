class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        from functools import cache

        @cache
        def dfs(i=0, m=1, alice=1):
            if i >= len(piles):
                return 0
            
            res = 0 if alice == 1 else sys.maxsize
            turn = 0
            for x in range(1, 2*m+1):
                if i+x > len(piles):
                    break
                turn += piles[i+x-1]
                if alice == 1:
                    res = max(
                        res,
                        turn + dfs(i+x, max(m, x), 0)
                    )
                else:
                    res = min(
                        res,
                        dfs(i+x, max(m, x), 1)
                    )
            return res
        
        score = dfs()
        return score

