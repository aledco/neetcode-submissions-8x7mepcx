class Solution:
    def isHappy(self, n: int) -> bool:
        
        def digits(n):
            for c in str(n):
                yield int(c)

        def squareSum(n):
            v = 0
            for d in digits(n):
                v += d * d
            return v 
        
        seen = {n}
        while True:
            n = squareSum(n)
            if n == 1:
                return True
            elif n in seen:
                return False
            
            seen.add(n)
            