class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        o = 0
        for i, n in enumerate(nums):
            if n == val:
                o += 1
            else:
                nums[i-o] = n
        return len(nums)-o