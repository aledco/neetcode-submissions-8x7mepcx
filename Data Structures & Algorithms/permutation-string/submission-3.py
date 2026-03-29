class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        C = Counter(s1)
        i = 0
        while i < len(s2):
            if s2[i] in C:
                D = C.copy()
                j = i
                while j < len(s2) and s2[j] in D:
                    D[s2[j]] -= 1
                    if D[s2[j]] == 0:
                        del D[s2[j]]
                    j += 1
                if len(D) == 0:
                    return True
            i += 1
        return False