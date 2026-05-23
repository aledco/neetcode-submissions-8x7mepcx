class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def find(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        i, m, mp = 0, 0, None
        while i < len(s):
            p = find(s, i, i)
            if i-1 >= 0 and s[i-1] == s[i]:
                p2 = find(s, i-1, i)
                if len(p2) > len(p):
                    p = p2
        
            if len(p) > m:
                m, mp = len(p), p
            
            i += 1
            
        return mp
