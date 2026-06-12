class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        inverse = False
        if n < 0:
            inverse = True
            n *= -1
        
        def powPos(x, n):
            v = 1
            for i in range(n):
                v *= x
            return v

        p = powPos(x, n)
        if inverse:
            return 1 / p
        else:
            return p