class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        s = sum(nums)
        if s % k == 0:
            return True
        
        p = 0
        for i in range(len(nums)-2):
            p += nums[i]
            if (p - (s%k)) % k == 0:
                return True
        
        p = 0
        for i in range(len(nums)-1, 1, -1):
            p += nums[i]
            if (p - (s%k)) % k == 0:
                return True

        return False