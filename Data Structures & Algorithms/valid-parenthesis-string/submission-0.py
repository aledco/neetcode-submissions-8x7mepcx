class Solution:
    def checkValidString(self, s: str) -> bool:
        L, S = [], []
        for i, c in enumerate(s):
            if c == '(':
                L.append(i)
            elif c == '*':
                S.append(i)
            elif c == ')':
                if len(L) > 0:
                    L.pop()
                elif len(S) > 0:
                    S.pop()
                else:
                    return False
        
        if len(L) == 0:
            return True
        elif len(S) < len(L):
            return False
        else:
            while len(L) > 0:                
                i = L.pop()
                j = S.pop()
                if j < i:
                    return False
            return True
                
