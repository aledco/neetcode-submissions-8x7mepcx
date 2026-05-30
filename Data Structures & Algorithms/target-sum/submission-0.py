class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(N, t, i=0):
            if i >= len(N):
                return 1 if t == 0 else 0
            
            return dfs(N, t+N[i], i+1) + dfs(N, t-N[i], i+1)
        
        return dfs(nums, target)
