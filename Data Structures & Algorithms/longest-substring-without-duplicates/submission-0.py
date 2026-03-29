class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S = set()
        m = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in S:
                S.add(s[j])
                m = max(m, j - i + 1)
            else:
                while s[i] != s[j]:
                    S.remove(s[i])
                    i += 1
                i += 1
            j += 1
        return m
                