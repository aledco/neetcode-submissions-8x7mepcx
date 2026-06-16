class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for c in nums:
            if c == 0:
                red += 1
            elif c == 1:
                white += 1
            elif c == 2:
                blue += 1
        
        i = 0
        while i < red:
            nums[i] = 0
            i += 1
        while i < red+white:
            nums[i] = 1
            i += 1
        while i < red+white+blue:
            nums[i] = 2
            i += 1