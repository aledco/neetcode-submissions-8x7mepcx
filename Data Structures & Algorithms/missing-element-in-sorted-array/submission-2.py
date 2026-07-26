class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def divide(nums, i, j, k):
            if j - i + 1 == 2:
                # kth must be in between nums[i] and nums[j]
                res = nums[i] + k
                if res >= nums[j]: # if kth is after the end of nums, need to account for nums[j] existing in the range of nums[i] to kth
                    res += 1
                return res

            m = (i + j) // 2
            missing_left = (nums[m] - nums[i] + 1) - (m - i + 1)
            if missing_left >= k:
                return divide(nums, i, m, k)
            else:
                return divide(nums, m, j, k - missing_left)


        return divide(nums, 0, len(nums)-1, k)