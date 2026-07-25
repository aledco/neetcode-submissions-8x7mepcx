class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        res = []
        c = 0
        for i in range(max(m, n)):
            if m-i-1 >= 0:
                c += int(a[m-i-1])
            if n-i-1 >= 0:
                c += int(b[n-i-1])
            
            if c <= 1:
                res.append(str(c))
                c = 0
            else:
                res.append(str(c - 2))
                c = 1 
        if c == 1:
            res.append(str(c))
        return "".join(reversed(res))


