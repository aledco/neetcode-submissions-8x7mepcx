class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        seen = set()

        def backtrack(N, t, S, s, i):
            if tuple(S) in seen:
                return []
            if s == t:
                seen.add(tuple(S))
                return [S]
            elif s > t:
                return []

            if i >= len(N):
                return []
            
            n = N[i]
            return (
                backtrack(N, t, S, s, i+1) + 
                backtrack(N, t, S + [n], s + n, i) + 
                backtrack(N, t, S + [n], s + n, i+1)
            )

        return backtrack(nums, target, [], 0, 0)