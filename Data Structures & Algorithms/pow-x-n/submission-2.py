class Solution:
    def myPow(self, x: float, n: int) -> float:
        inverse = False
        if n < 0:
            inverse = True
            n *= -1
        
        def powPos(x, n):
            if n == 0:
                return 1 
            v, i = x, 1
            while i * 2 <= n:
                v *= v
                i *= 2
            return v * powPos(x, n-i)
            
            # v = 1
            # for i in range(n):
            #     v *= x
            # return v

        p = powPos(x, n)
        if inverse:
            return 1 / p
        else:
            return p