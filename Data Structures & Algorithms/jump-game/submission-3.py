class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def dfs(N, i=0):
            if i >= len(N)-1:
                return True
            
            for j in range(1, N[i]+1):
                if dfs(N, i+j):
                    return True
            return False

        # return dfs(nums)

        def greedy(N):
            
            # idea: anytime we jump, only jump to the index that can get us the farthest

            i = 0
            while i < len(N)-1:
                if N[i] == 0:
                    return False
                
                start, maxj = i+1, i + N[i]
                farthest = 0
                for j in range(start, min(maxj+1, len(N))):
                    if j + N[j] > farthest:
                        i = j
                        farthest = j + N[j]
            return True
        
        return greedy(nums)