class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i, n in enumerate(nums):
            s += (i + 1) - n
        return s