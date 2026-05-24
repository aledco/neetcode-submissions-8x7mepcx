class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(s, i=0):
            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0
            
            r = dfs(s, i+1)
            if i+1 < len(s) and int(s[i] + s[i+1]) <= 26:
                r += dfs(s, i+2)
            return r
        
        # return dfs(s)

        def dynamic_programming(s):
            dp = [0] * (len(s) + 1)
            dp[len(s)] = 1
            for i in range(len(s)-1, -1, -1):
                if s[i] == '0':
                    dp[i] = 0
                    continue
                
                dp[i] = dp[i+1]
                if i+1 < len(s) and 10 <= int(s[i] + s[i+1]) <= 26:
                    dp[i] += dp[i+2]
            return dp[0]
            
        return dynamic_programming(s)