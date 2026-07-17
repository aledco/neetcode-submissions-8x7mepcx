class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # def backtrack(N, P, I):
        #     if len(I) == 0:
        #         return [P]
        #     A = []
        #     for i in I:
        #         A += backtrack(N, P + [N[i]], I - {i})
        #     return A
        
        # return backtrack(nums, [], set(range(len(nums))))

        def backtrack(nums, pick, perm):
            if len(perm) == len(nums):
                return [perm.copy()]
            
            res = []
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    res += backtrack(nums, pick, perm)
                    perm.pop()
                    pick[i] = False
            return res
        
        return backtrack(nums, [False] * len(nums), [])