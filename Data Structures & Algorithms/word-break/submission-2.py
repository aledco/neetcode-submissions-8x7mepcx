class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def hashSet(s, W): # O(n^3)
            W = set(W)
            I = []
            for j in range(len(s)):
                if s[0:j+1] in W:
                    I.append(j)
                else:
                    for i in I:
                        if s[i+1:j+1] in W:
                            I.append(j)
                            break
            return len(I) > 0 and I[-1] == len(s)-1
        
        # return hashSet(s, wordDict)

        def dfs(s, W, i=0):
            if i >= len(s):
                return True
            
            for w in W:
                if i+len(w) > len(s):
                    continue
                if s[i:i+len(w)] == w:
                    if dfs(s, W, i+len(w)):
                        return True
            return False
            
        # return dfs(s, wordDict)

        def dynamicProgramming(s, W):
            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(len(s)):
                for w in W:
                    j = i - len(w) + 1
                    if j >= 0 and s[j:i+1] == w and dp[j]:
                        dp[i+1] = True
            return dp[-1]
        
        return dynamicProgramming(s, wordDict)

