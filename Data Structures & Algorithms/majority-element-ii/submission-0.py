class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        def count(N):
            from collections import Counter

            C = Counter(nums)
            n = len(nums)
            for v, c in C.items():
                if c > n // 3:
                    yield v
        
        return [n for n in count(nums)]