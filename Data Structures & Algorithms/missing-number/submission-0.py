class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for i in range(1, n+1):
            s += i

        for x in nums:
            s -= x
        return s