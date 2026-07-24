class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        def dynamicProgramming(s, mij, maj):
            # dp[i] = True if possible to jump to i
            n = len(s)
            dp = [False] * n
            dp[0] = True
            for j in range(1, n):
                if s[j] == '1':
                    continue
                for i in range(max(0, j-maj), j-mij+1):
                    if dp[i]:
                        dp[j] = True
                        break
            return dp[n-1]
        
        return dynamicProgramming(s, minJump, maxJump)