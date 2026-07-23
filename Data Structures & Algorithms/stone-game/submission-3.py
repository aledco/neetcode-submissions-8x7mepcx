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

        def greedy(piles):
            from collections import deque
            res, i = [0, 0], 0

            piles = deque(piles)
            while len(piles) > 0:
                if piles[0] > piles[-1]:
                    res[i] += piles.popleft()
                else:
                    res[i] += piles.pop()
            return res[0] > res[1]
        
        return greedy(piles)


        # return True
            

