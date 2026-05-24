import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(C, t, s=0, i=0):
            if s == t:
                return i
            elif s > t:
                return -1
            
            R = []
            for c in C:
                r = dfs(C, t, s+c, i+1)
                if r > -1:
                    R.append(r)
            if len(R) == 0:
                return -1
            return min(R)
        
        # return dfs(coins, amount)

        def dynamic_programming(C, t):
            C = list(sorted(C, reverse=True))
            dp = [sys.maxsize] * (t+1)
            dp[0] = 0
            for i in range(t+1):
                for c in C:
                    if i - c >= 0:
                        dp[i] = min(dp[i], dp[i-c]+1)
            if dp[-1] == sys.maxsize:
                return -1
            return dp[-1]

        return dynamic_programming(coins, amount)