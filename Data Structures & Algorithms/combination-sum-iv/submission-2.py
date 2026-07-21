class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def dfs(nums, target, i=0, s=0):
            if i >= len(nums) or s > target:
                return 0
            elif s == target:
                return 1
            
            return (
                dfs(nums, target, 0, s+nums[i]) + 
                dfs(nums, target, i+1, s)
            )
        
        # return dfs(nums, target)

        def dynamicProgramming(nums, target):
            # dp[i] = number of ways to sum to i
            dp = [0] * (target+1)
            dp[0] = 1
            for total in range(1, target+1):
                for n in nums:
                    if total-n >= 0:
                        dp[total] += dp[total-n]
            return dp[target]
        
        return dynamicProgramming(nums, target)



            
