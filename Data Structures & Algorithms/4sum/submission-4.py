class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = list(sorted(nums))
        print(nums)
        res = []
        # i, j = 0, len(nums)-1
        # while i < j-2: # need at least four elements between i and j
        for i in range(len(nums)-3):
            print(i, len(nums)-3)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+3, len(nums)):
                print(i, j)
                if j < len(nums)-1 and nums[j] == nums[j+1]:
                    continue

                # skip over duplicate elements
                # while i > 0 and i < j-2 and nums[i] == nums[i-1]:
                #     i += 1
                # while j < len(nums)-1 and i < j-2 and nums[j] == nums[j+1]:
                #     j -= 1

                print(nums[i:j+1], i, j, target - nums[i] - nums[j])

                for a, b in self.twoSum(nums, i+1, j-1, target - nums[i] - nums[j]):
                    res.append([nums[i], a, b, nums[j]])
                # i += 1
                # j -= 1
        return res

    def twoSum(self, nums: List[int], i: int, j: int, target: int) -> List[int]:
        print(nums[i:j+1], i, j, target)
        print()
        k = i
        while k < j:
            while k > i and k < j and nums[k] == nums[k-1]:
                k += 1
            l = self.binSearch(nums, k+1, j, target-nums[k])
            if l != -1:
                yield [nums[k], nums[l]]
            k += 1
    
    def binSearch(self, nums: List[int], i: int, j: int, target: int) -> int:
        if i > j:
            return -1

        m = (i + j) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binSearch(nums, m+1, j, target)
        else:
            return self.binSearch(nums, i, m-1, target)

        