class Solution:
    def getSum(self, a: int, b: int) -> int:
        # sign = 1
        # if a < 0 and b < 0:
        #     a *= -1
        #     b *= -1
        # elif a < 0:
        #     sign = -1
        #     a *= -1
        # elif b < 0:
        #     sign = -1
        #     b *= -1

        mask = 0xFFFFFFFF
        while b & mask != 0:
            c = (a & b) << 1
            a = a ^ b
            b = c
        return (a & mask) if b > 0 else a
    