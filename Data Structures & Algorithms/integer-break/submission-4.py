class Solution:
    def integerBreak(self, n: int) -> int:
        res = 1
        for k in range(2, n + 1):
            d = n // k
            r = n % k
            p = (d**(k - r)) * ((1 + d)**r)
            print(d, r, p)
            res = max(res, p)
        return res
