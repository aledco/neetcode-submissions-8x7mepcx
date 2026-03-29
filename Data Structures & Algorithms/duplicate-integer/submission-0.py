class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        C = defaultdict(int)
        for n in nums:
            C[n] += 1
            if C[n] > 1:
                return True
        return False