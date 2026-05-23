class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # def dfs(C, c, i):
        #     if i >= len(C):
        #         return c
        #     c += C[i]
        #     return min(
        #         dfs(C, c, i+1),
        #         dfs(C, c, i+2),
        #     )
        
        # return min(
        #     dfs(cost, 0, 0),
        #     dfs(cost, 0, 1),
        # )

        def dynamic_programming(cost):
            dp = [0] * (len(cost) + 1)
            for i in range(2, len(cost)+1):
                dp[i] = min(
                    cost[i-1] + dp[i-1],
                    cost[i-2] + dp[i-2],
                )
            return dp[-1]
        
        return dynamic_programming(cost)
