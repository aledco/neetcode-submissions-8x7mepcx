class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        def linearSearch(N):
            S = set(N)
            n = 1
            while True:
                if n not in S:
                    return n
                else:
                    n += 1

        return linearSearch(nums)