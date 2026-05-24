class Solution:
    def countSubstrings(self, s: str) -> int:
        def find(s, i, j):
            c = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                c += 1
            return c

        i, t = 0, 0
        while i < len(s):
            t += find(s, i, i)
            if i-1 >= 0 and s[i-1] == s[i]:
                t += find(s, i-1, i)
        
            i += 1
            
        return t
