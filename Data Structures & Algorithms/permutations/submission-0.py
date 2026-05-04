class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(N, P, I):
            if len(I) == 0:
                return [P]
            A = []
            for i in I:
                A += backtrack(N, P + [N[i]], I - {i})
            return A
        
        return backtrack(nums, [], set(range(len(nums))))