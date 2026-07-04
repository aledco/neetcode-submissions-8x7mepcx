class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x+1
        while i < j:
            m = (i + j) // 2
            y = m * m
            if y == x or (y < x and (m+1)*(m+1) > x):
                return m
            elif y < x:
                i = m+1
            else:
                j = m
        return -1
