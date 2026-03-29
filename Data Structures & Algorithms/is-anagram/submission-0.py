class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        C = Counter(s)
        for c in t:
            if c not in C:
                return False
            else:
                C[c] -= 1
                if C[c] == 0:
                    del C[c]
        return len(C) == 0
            