class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(N, t, i=0):
            if i >= len(N):
                return 1 if t == 0 else 0
            
            return dfs(N, t+N[i], i+1) + dfs(N, t-N[i], i+1)
        
        # return dfs(nums, target)

        def dynamicProgramming(N, t):
            n = len(N)
            dp = [defaultdict(int) for _ in range(n+1)]
            dp[0][0] = 1
            for i in range(n):
                for s, c in dp[i].items():
                    dp[i+1][s + N[i]] += c
                    dp[i+1][s - N[i]] += c
            return dp[n][t]
        
        # return dynamicProgramming(nums, target)

        def dynamicProgramming_spaceOptimized(N, t):
            n = len(N)
            dp = defaultdict(int)
            dp[0] = 1
            for i in range(n):
                dp_next = defaultdict(int)
                for s, c in dp.items():
                    dp_next[s + N[i]] += c
                    dp_next[s - N[i]] += c
                dp = dp_next
            return dp[t]
        
        return dynamicProgramming_spaceOptimized(nums, target)