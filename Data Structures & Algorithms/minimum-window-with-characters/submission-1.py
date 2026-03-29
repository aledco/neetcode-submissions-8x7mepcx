class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        C = Counter(t)
        S = len(t)

        i, j = 0, 0
        m, ms = len(s) + 1, ""
        while j < len(s):
            if s[j] in C:
                if C[s[j]] > 0:
                    S -= 1
                C[s[j]] -= 1
                if S == 0:
                    while s[i] not in C or C[s[i]] < 0:
                        if s[i] in C:
                            C[s[i]] += 1
                        i += 1
                    
                    assert C[s[i]] == 0

                    if j - i + 1 <= m:
                        m = j - i + 1
                        ms = s[i:j+1]
                    
                    C[s[i]] += 1
                    S += 1
                    i += 1
            j += 1
        return ms

            