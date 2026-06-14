class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def prefix(a, b):
            if len(b) < len(a):
                a, b = b, a
            i = 0
            while i < len(a) and a[i] == b[i]:
                i += 1
            return b[:i]

        p = strs[0]
        for s in strs[1:]:
            p = prefix(p, s)
        return p