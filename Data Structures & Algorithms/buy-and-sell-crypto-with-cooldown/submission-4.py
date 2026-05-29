class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(P, i=0, p=False):
            if i >= len(P):
                return 0
            
            if p: # NeetCoin has been purchased and can be sold
                return max(
                    dfs(P, i+1, True), # not sold
                    dfs(P, i+2, False) + P[i] # sold 
                )
            else: # NeetCoin can be purchased
                return max(
                    dfs(P, i+1, False), # not purchased
                    dfs(P, i+1, True) - P[i] # purchased 
                )

        # return dfs(prices)

        def dynamicProgramming(P):
            # dp[i][1] = maximum profit starting day i if we can buy
            # dp[i][0] = maximum profit starting day i if we own

            n = len(P)
            dp = [[0, 0] for _ in range(n+1)]
            for i in range(n-1, -1, -1):
                dp[i][1] = max( # Max when buying
                    dp[i+1][0] - P[i],
                    dp[i+1][1]
                )
                dp[i][0] = max( # Max when selling
                    P[i] if i+2 > n else dp[i+2][1] + P[i],
                    dp[i+1][0]
                )
            return dp[0][1]
        
        return dynamicProgramming(prices)
    
