class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        P = defaultdict(int)
        P[0] = 1
        p, r = 0, 0
        for n in nums:
            p += n
            d = p - k
            r += P[d]
            P[p] += 1
        return r
        
        