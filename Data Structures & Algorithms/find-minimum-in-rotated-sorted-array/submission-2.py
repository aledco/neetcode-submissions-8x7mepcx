class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def binSearch(N, i, j):
            if i >= j:
                return N[0]
            
            m = (i + j) // 2
            print(m, m-1, N[m], N[m-1])
            if N[m] < N[m-1]:
                return N[m]
            elif N[m] > N[0] and N[m] > N[-1]:
                return binSearch(N, m+1, j)
            else:
                return binSearch(N, i, m)
        
        return binSearch(nums, 0, len(nums))