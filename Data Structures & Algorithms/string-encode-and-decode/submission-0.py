class Solution:

    def encode(self, strs: List[str]) -> str:
        E = [str(len(s)) + "|" + s for s in strs]
        return "".join(E)

    def decode(self, s: str) -> List[str]:
        def get_len(s, i):
            n = ""
            while i < len(s) and s[i] != '|':
                n += s[i]
                i += 1
            if len(n) > 0:
                assert s[i] == '|'
                return int(n), i + 1
            return -1, i
        
        D = []
        i = 0
        while i < len(s):
            l, i = get_len(s, i)
            if l == -1:
                break

            D.append(s[i:i+l])
            i = i+l
        return D


