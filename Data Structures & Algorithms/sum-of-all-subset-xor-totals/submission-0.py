class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        stack = [[0, 0]]
        res = 0
        while len(stack) > 0:
            i, xor = stack.pop()
            res += xor ^ nums[i]
            if i+1 < len(nums):
                stack.append([i+1, xor ^ nums[i]])
                stack.append([i+1, xor])
        return res
