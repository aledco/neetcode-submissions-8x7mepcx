class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def dfs(C, a):
            if a == 0:
                return 1
            elif a < 0:
                return 0
            
            r = 0
            while len(C) > 0:
                c = C.pop()
                ac = a - c
                while ac >= 0:
                    r += dfs(C.copy() , ac)
                    ac -= c
            return r
        
        # return dfs(coins, amount)

        def dynamicProgramming(C, a):
            # dp[i][j] = with the coins C[:i], how many combinations sum to j
            n = len(C)
            dp = [[0] * (a+1) for _ in range(n+1)]
            for i in range(n+1):
                dp[i][0] = 1
            for i in range(1, n+1):
                c = C[i-1]
                for j in range(1, a+1):
                    dp[i][j] = dp[i-1][j]
                    if j-c >= 0:
                        dp[i][j] += dp[i][j-c]
            # print(dp)
            return dp[n][a]
        
        return dynamicProgramming(coins, amount)