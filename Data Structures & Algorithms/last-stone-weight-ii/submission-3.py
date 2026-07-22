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
        
        return dfs(stones)

        def dynamicProgramming(S):
            pass
        
        # return dynamicProgramming(stones)
                