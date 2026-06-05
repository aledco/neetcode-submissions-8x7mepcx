class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def greedy(N):
            
            # idea: anytime we jump, only jump to the index that can get us the farthest


            i, jumps = 0, 0
            while i < len(N)-1:
                # if N[i] == 0:
                #     return False
                # print(i)
                start, maxj = i+1, i + N[i]
                farthest = 0
                for j in range(start, min(maxj+1, len(N))):
                    if j + N[j] > farthest or j + N[j] >= len(N)-1:
                        i = j
                        farthest = j + N[j]
                jumps += 1
            return jumps
        
        return greedy(nums)