# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 0, n+1
        while i < j:
            m = (i + j) // 2
            match guess(m):
                case 0:
                    return m
                case -1:
                    j = m
                case 1:
                    i = m+1
        return -1