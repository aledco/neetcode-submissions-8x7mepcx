class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfs(N, i=0, s1=0, s2=0):
            
            if i >= len(N):
                return s1 == s2
            
            return (
                dfs(N, i+1, s1 + N[i], s2) or
                dfs(N, i+1, s1, s2 + N[i])
            )

        # return dfs(nums)

        def dfs_optmized(N, t, i=0, s=0):
            if t % 2 == 1:
                return False
            if s > t//2:
                return False
            if i >= len(N):
                return s == t//2
            
            return (
                dfs_optmized(N, t, i+1, s + N[i]) or
                dfs_optmized(N, t, i+1, s)
            )

        return dfs_optmized(nums, sum(nums))