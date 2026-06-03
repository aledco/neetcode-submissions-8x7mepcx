class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def matches(s, p, i, j):
            return s[i] == p[j] or p[j] == '.'

        def dfs(s, p, i=0, j=0):
            if i >= len(s) and j >= len(p):
                return True
            elif i >= len(s) and j+2 == len(p) and p[j+1] == '*':
                return True
            elif i >= len(s) or j >= len(p):
                return False
            
            if j+1 < len(p) and p[j+1] == '*':
                return (
                    dfs(s, p, i, j+2) or # try zero matches
                    (
                        matches(s, p, i, j) and dfs(s, p, i+1, j)
                    ) # try 1 or more matches
                )
            elif matches(s, p, i, j):
                return dfs(s, p, i+1, j+1)
            else:
                return False
        
        return dfs(s, p)
            

            