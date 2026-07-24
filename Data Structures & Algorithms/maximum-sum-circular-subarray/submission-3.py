class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def dynamicProgramming_linear(nums):
            # dp[j] = maximum sum that ends at element i in the linear array
            n = len(nums)
            dp = [0 for _ in range(n)]
            for j in range(n):
                if j-1 >= 0 and dp[j-1] > 0:
                    dp[j] = dp[j-1] + nums[j]
                else:
                    dp[j] = nums[j]
            return max(dp)
        
        def circularSum(nums):
            n = len(nums)
            prefix = [[0, 0] for _ in range(n)]
            for i, x in enumerate(nums):
                if i-1 >= 0:
                    prefix[i][0] = prefix[i-1][0] + x
                    prefix[i][1] = max(prefix[i-1][1], prefix[i][0])
                else:
                    prefix[i] = [x, x]
                
            suffix = [[0, 0] for _ in range(n)]
            for i in range(n-1, -1, -1):
                x = nums[i]
                if i+1 < n:
                    suffix[i][0] = suffix[i+1][0] + x
                    suffix[i][1] = max(suffix[i+1][1], suffix[i][0])
                else:
                    suffix[i] = [x, x]
            
            res = -sys.maxsize
            for i in range(n-1):
                res = max(res, prefix[i][1] + suffix[i+1][1])
            return res

        linear_max = dynamicProgramming_linear(nums)
        circular_max = circularSum(nums)
        return max(linear_max, circular_max)