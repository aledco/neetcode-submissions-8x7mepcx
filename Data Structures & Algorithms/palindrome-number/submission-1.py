class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math

        if x < 0:
            return False
        elif x < 10:
            return True

        digits = int(math.log10(x)) + 1

        def getDigit(x, i):
            return (x // (10 ** i)) % 10

        for i in range(digits//2):
            if getDigit(x, i) != getDigit(x, digits-i-1):
                return False
        return True