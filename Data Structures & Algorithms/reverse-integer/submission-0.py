class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = reversed(str(-x))
            y = -int("".join(s))
        else:
            s = reversed(str(x))
            y = int("".join(s))
       
        if -2**31 <= y <= 2**31 - 1:
            return y
        else:
            return 0