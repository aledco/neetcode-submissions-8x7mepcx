class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(N, S, i):
            if i >= len(N):
                return [S]
            R1 = backtrack(N, S + [N[i]], i+1)
            while i+1 < len(N) and N[i+1] == N[i]:
                i += 1
            R2 = backtrack(N, S, i+1)
            return R1 + R2
        
        
        return backtrack(list(sorted(nums)), [], 0)