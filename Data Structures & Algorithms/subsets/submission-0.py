class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(N, S, i):
            if i >= len(N):
                return [S]
            return backtrack(N, S, i+1) + backtrack(N, S + [N[i]], i+1)
        
        return backtrack(nums, [], 0)
