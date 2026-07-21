class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        t0, t1, t2 = 0, 1, 1
        for _ in range(2, n):
            t3 = t2 + t1 + t0
            t0, t1, t2 = t1, t2, t3
        return t2
        