class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        M = {}
        for j, n in enumerate(nums):
            if target-n in M:
                return [M[target-n], j]
            if n not in M:
                M[n] = j
        return [-1, -1]