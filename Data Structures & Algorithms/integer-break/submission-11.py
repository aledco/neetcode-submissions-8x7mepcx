class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        res = 1
        for k in range(2, n // 2 + 1):
            d = n // k
            r = n % k
            p = (d**(k - r)) * ((1 + d)**r)
            res = max(res, p)
        return res
