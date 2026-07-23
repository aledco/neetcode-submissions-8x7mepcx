class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        def dfs(S):
            if len(S) == 0:
                return 0
            elif len(S) == 1:
                return S[0]
            
            res = sys.maxsize
            for i in range(len(S)-1):
                for j in range(i+1, len(S)):
                    x, y = S[i], S[j]
                    U = S.copy()
                    if x < y:
                        U[j] = y - x
                        U.pop(i)
                    elif x > y:
                        U[i] = x - y
                        U.pop(j)
                    else:
                        U.pop(j)
                        U.pop(i)
                    res = min(res, dfs(U))
            return res
        
        # return dfs(stones)

        def dfs_optimized(S):

            # dfs finds the largest subset sum that is <= t
            def dfs(S, t, s=0, i=0):
                if s > t:
                    return -1
                if i >= len(S):
                    return s
                
                return max(
                    dfs(S, t, s, i+1),
                    dfs(S, t, s+S[i], i+1)
                )
            
            total = sum(S)
            a = dfs(S, total // 2)
            b = total - a
            return abs(a - b)

        # return dfs_optimized(stones)

        def dynamicProgramming(S):
            
            # solve finds the largest subset sum that is <= t
            def solve(S, t):
                # dp[s] = True if sum s is possible
                dp = [False] * (t+1)
                dp[0] = True
                for w in S:
                    for s in range(t, w-1, -1):
                        dp[s] = dp[s] or dp[s-w]
                for s in range(t, -1, -1):
                    if dp[s]:
                        return s 
            
            total = sum(S)
            a = solve(S, total // 2)
            return abs(2*a - total)

        return dynamicProgramming(stones)
                