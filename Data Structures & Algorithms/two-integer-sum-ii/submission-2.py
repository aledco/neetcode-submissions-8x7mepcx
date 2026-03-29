class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binSearch(N, t, i=None, j=None):
            if i is None:
                i = 0
            if j is None:
                j = len(N)
            
            if i >= j:
                return -1
            
            m = (i+j) // 2
            if N[m] == t:
                return m
            elif N[m] < t:
                return binSearch(N, t, m+1, j)
            else:
                return binSearch(N, t, i, m)
        
        def solve(N, t):
            for i, n in enumerate(N):
                m = t - n
                if m != n:
                    j = binSearch(N, m)
                    if j > -1:
                        return [i+1, j+1]
            return [-1, -1]
        
        return solve(numbers, target)