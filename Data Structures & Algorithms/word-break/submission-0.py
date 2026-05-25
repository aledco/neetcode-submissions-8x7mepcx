class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def hashSet(s, W):
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
        
        return hashSet(s, wordDict)
