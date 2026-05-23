class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)

        # def dfs(N, i=0):
        #     if i >= len(N):
        #         return 0
            
        #     return max(
        #         N[i] + dfs(N, i+2),
        #         dfs(N, i+1)
        #     )
        
        # return dfs(nums)

        def dynamic_programming(N):
            dp = [0] * len(N)
            dp[0] = N[0]
            dp[1] = max(N[0], N[1])
            for i in range(2, len(N)):
                dp[i] = max(
                    dp[i-2] + N[i],
                    dp[i-1]
                )
            return dp[-1]
        
        return max(
            dynamic_programming(nums[:-1]),
            dynamic_programming(nums[1:])
        )
