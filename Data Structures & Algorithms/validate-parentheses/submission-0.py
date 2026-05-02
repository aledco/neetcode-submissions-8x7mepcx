class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        for c in s:
            if c in ('(', '{', '['):
                S.append(c)
            else:
                if len(S) == 0:
                    return False
                o = S.pop()
                if c == ')' and o != '(':
                    return False
                if c == '}' and o != '{':
                    return False
                if c == ']' and o != '[':
                    return False
        return len(S) == 0