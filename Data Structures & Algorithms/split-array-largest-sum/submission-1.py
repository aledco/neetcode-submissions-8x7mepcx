class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def dfs(N, k, i=0, c=1, s=0, m=0):
            if i >= len(N):
                return m
            
            if c >= k:
                return dfs(N, k, i+1, c, s+N[i], max(s+N[i], m))
            else:
                return min(
                    dfs(N, k, i+1, c, s+N[i], max(s+N[i], m)),
                    dfs(N, k, i+1, c+1, N[i], max(N[i], m))
                )

        # return dfs(nums, k)

        # def dynamicProgramming(N, k):
        #     # dp[i][c][0] = the minimum of the max subarray at index i with c subarrays
        #     # dp[i][c][1] = the sum of the current subarray
        #     # dp[n][k][0] = the solution

        #     n = len(N)
        #     dp = [[[0, 0] for _ in range(k+1)] for _ in range(n+1)]
        #     for i in range(1, n+1):
        #         for c in range(1, k+1):
        #             s1 = dp[i-1][c][1] + N[i-1]
        #             m1 = max(dp[i-1][c][0], s1)
        #             if c >= k:
        #                 dp[i][c] = [m1, s1]
        #             else:
        #                 s2 = N[i-1]
        #                 m2 = max(dp[i-1][c-1][0], s2)
        #                 if m1 < m2:
        #                     dp[i][c] = [m1, s1]
        #                 else:
        #                     dp[i][c] = [m2, s2]
        #     return dp[n][k][0]
        
        # return dynamicProgramming(nums, k)

        def binarySearch(N, k):
            
            def sim(N, k, m):
                c, s = 1, 0
                for n in N:
                    if s + n <= m:
                        s += n
                    else:
                        # print(s)
                        c += 1
                        if c > k:
                            return False
                        s = n
                # print(m, c)
                # print()
                return c <= k

            l, r = max(N), sum(N)
            res = r
            while l <= r:
                m = (l + r) // 2
                if sim(N, k, m):
                    res = m
                    r = m-1
                else:
                    l = m+1
            return res
        
        return binarySearch(nums, k)



