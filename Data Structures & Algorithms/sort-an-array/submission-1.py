class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def pivot(nums, l, r):
            m = (l + r) // 2
            _, p = sorted([
                    (nums[l], l),
                    (nums[m], m),
                    (nums[r], r)
                ])[1]
            nums[r], nums[p] = nums[p], nums[r]
            return nums[r]
            
        def partition(nums, l, r):
            p = pivot(nums, l, r)
            i = l
            for j in range(l, r):
                if nums[j] <= p:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quickSort(nums, l, r):
            if l >= r:
                return
            p = partition(nums, l, r)
            quickSort(nums, l, p-1)
            quickSort(nums, p+1, r)
        
        quickSort(nums, 0, len(nums)-1)
        return nums
