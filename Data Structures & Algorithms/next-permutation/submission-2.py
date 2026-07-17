class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # for i in range(len(nums)-1, 0, -1):
        #     for j in range(i-1, -1, -1):
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             for k, v in enumerate(sorted(nums[j+1:])):
        #                 nums[j+k+1] = v
        #             return

        for i in range(len(nums)-2, -1, -1):
            sj, sv = -1, sys.maxsize
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i] and nums[j] < sv:
                    sj, sv = j, nums[j]
            if sj == -1:
                continue
                
            nums[i], nums[sj] = nums[sj], nums[i]
            for k, v in enumerate(sorted(nums[i+1:])):
                nums[i+k+1] = v
            return
        nums.sort()
