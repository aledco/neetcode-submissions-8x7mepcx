class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = set(nums)
        S = [n for n in nums if n-1 not in N]
        m = 0
        for s in S:
            l = 1
            while s+1 in N:
                s += 1
                l += 1
            m = max(m, l)
        return m