class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binSearch(N, t, i, j):
            print(i, j)
            if i >= j:
                return -1
            
            m = (i + j) // 2
            print(i, j, m)
            if N[m] == t:
                return m
            elif (
                t > N[m] and N[m] > N[j-1]
            ) or (
                t > N[m] and t <= N[j-1]  
            ) or (
                t < N[m] and N[m] > N[j-1] and t <= N[j-1]
            ):
                return binSearch(N, t, m+1, j)
            else:
                return binSearch(N, t, i, m)
        
        return binSearch(nums, target, 0, len(nums)) 