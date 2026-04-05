class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binSearch(N, t, i, j):
            if i >= j:
                return -1
            
            m = (i + j) // 2
            if N[m] == t:
                return m
            elif N[m] < t:
                return binSearch(N, t, m+1, j)
            else:
                return binSearch(N, t, i, m)
        
        return binSearch(nums, target, 0, len(nums))