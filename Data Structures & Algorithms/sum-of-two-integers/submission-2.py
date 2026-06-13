class Solution:
    def getSum(self, a: int, b: int) -> int:

        def sign(n):
            return 1 if n >= 0 else -1
            
        if b < a:
            a, b = b, a
        
        for i in range(abs(a)):
            b += sign(a) * 1
        return b

        # while b:
        #     c = (a & b) << 1
        #     a = a ^ b
        #     b = c
        # return a