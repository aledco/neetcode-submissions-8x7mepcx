class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        
        c, s = 0, 0
        while c < n:
            i = s
            p = nums[i]
            while True:
                j = (i + k) % n
                nums[j], p = p, nums[j]
                i = j
                c += 1

                if i == s:
                    break
            s += 1
