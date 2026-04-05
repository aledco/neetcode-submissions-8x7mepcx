class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def findRow(M, t, i, j):
            if i >= j:
                return -1
            
            m = (i + j) // 2
            if M[m][0] <= t and M[m][-1] >= t:
                return m
            elif M[m][0] > t:
                return findRow(M, t, i, m)
            else:
                return findRow(M, t, m+1, j)
        
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
            
        r = findRow(matrix, target, 0, len(matrix))
        if r == -1:
            return False
        
        c = binSearch(matrix[r], target, 0, len(matrix[r]))
        return c > -1
            

            

                
        