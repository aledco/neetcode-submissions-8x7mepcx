class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            # one, two = 1, 1
            # # M = [1, 2]
            # for _ in range(n-1):
            # # for i in range(2, n):
            #     one, two = one + two, one
            #     # M.append(
            #     #     M[i-1] + M[i-2]
            #     # )
            # return one
            # # return M[-1]

            import math

            b = math.sqrt(5)
            phi = (1 + b) / 2
            psi = (1 - b) / 2
            return round(
                (phi ** (n+1) - psi ** (n-1)) / b
            )