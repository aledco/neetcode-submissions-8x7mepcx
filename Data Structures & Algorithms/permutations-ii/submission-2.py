class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        
        def backtrack(nums, counts, perm):
            if len(perm) == len(nums):
                return [perm.copy()]
            
            res = []
            for i in range(len(counts)):
                if counts[i][1] > 0:
                    counts[i][1] -= 1
                    perm.append(counts[i][0])
                    res += backtrack(nums, counts, perm)
                    perm.pop()
                    counts[i][1] += 1
            return res
        
        counts = [list(x) for x in Counter(nums).items()]
        return backtrack(nums, counts, [])