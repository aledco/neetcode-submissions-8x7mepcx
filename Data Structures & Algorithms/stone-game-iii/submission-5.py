class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        from functools import cache

        def winner(score):
            if score > 0:
                return "Alice"
            elif score < 0:
                return "Bob"
            else:
                return "Tie"

        # @cache
        # def dfs(i=0):
        #     if i >= len(stoneValue):
        #         return (0, 0)
            
        #     maxa, maxb = 0, 0
        #     for j in range(1, 4):
        #         for k in range(1, 4):
        #             a, b = dfs(i+j+k)
        #             a += sum(stoneValue[i:i+j])
        #             b += sum(stoneValue[i+j:i+j+k])
        #             print(i, j, k, stoneValue[i:i+j], stoneValue[i+j:i+j+k], a, b, maxa, maxb)
        #             if a > maxa or b > maxb:
        #                 maxa, maxb = a, b
        #     return (maxa, maxb)

        def dfs(i=0, alice=1):
            if i >= len(stoneValue):
                return 0
            
            res = -sys.maxsize if alice == 1 else sys.maxsize
            s = 0
            for j in range(i, min(i+3, len(stoneValue))):
                s += stoneValue[j]
                if alice == 1: 
                    res = max(res, dfs(j+1, 0) + s)
                else:
                    res = min(res, dfs(j+1, 1) - s)
            return res
        
        # score = dfs()
        # return winner(score)

        def dynamicProgramming(S):
            n = len(S)
            dp = [[sys.maxsize, -sys.maxsize] for _ in range(n+1)]
            dp[n] = (0, 0)
            for i in range(n-1, -1, -1):
                for alice in (0, 1):
                    s = 0
                    for j in range(i, min(i+3, len(S))):
                        s += S[j]
                        if alice == 1:
                            dp[i][1] = max(dp[i][1], dp[j+1][0] + s)
                        else:
                            dp[i][0] = min(dp[i][0], dp[j+1][1] - s)
            return dp[0][1]
        
        score = dynamicProgramming(stoneValue)
        return winner(score)
                        