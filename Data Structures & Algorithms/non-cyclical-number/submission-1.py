class Solution:
    def isHappy(self, n: int) -> bool:
        
        def digits(n):
            for c in str(n):
                yield int(c)
        
        seen = {n}
        while True:
            v = 0
            for d in digits(n):
                v += d * d
            
            if v == 1:
                return True
            elif v in seen:
                return False
            
            seen.add(v)
            n = v
            