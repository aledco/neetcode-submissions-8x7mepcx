class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            M = [1, 2]
            for i in range(2, n):
                M.append(
                    M[i-1] + M[i-2]
                )
            return M[-1]