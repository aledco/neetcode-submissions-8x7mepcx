class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        s, m = 0, len(nums)+1
        i = 0
        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                m = min(m, j-i+1)
                s -= nums[i]
                i += 1
        if m > len(nums):
            return 0
        return m
