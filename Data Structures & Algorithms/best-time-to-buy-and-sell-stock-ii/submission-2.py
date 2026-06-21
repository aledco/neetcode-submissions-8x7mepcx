class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(P, i=0, o=False):
            if i >= len(P):
                return 0
            
            if o:
                return max(
                    dfs(P, i+1, True), # did not sell
                    P[i] + dfs(P, i+1, False), # did sell
                )
            else:
                return max(
                    dfs(P, i+1, False), # did not buy
                    dfs(P, i+1, True) - P[i] # did buy
                )
            
        # return dfs(prices)

        def dynamicProgramming(P):
            # dp[i][0] = max amount if buying on day i
            # dp[i][1] = max amount if selling on day i
            n = len(P)
            dp = [[0, 0] for _ in range(n+1)]
            for i in range(n-1, -1, -1):
                dp[i][0] = max(
                    dp[i+1][0],
                    dp[i+1][1] - P[i], 
                )
                dp[i][1] = max(
                    dp[i+1][1],
                    dp[i+1][0] + P[i] 
                )
                
            return dp[0][0]

        return dynamicProgramming(prices)
