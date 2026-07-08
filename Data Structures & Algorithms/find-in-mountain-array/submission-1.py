class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        cache = {}
        def get(A, i):
            nonlocal cache
            if i not in cache:
                cache[i] = A.get(i)
            return cache[i]
                
        def findPeak(A, i, j):
            assert i < j

            m = (i+j) // 2
            mv = get(A, m)
            bv = get(A, m-1) if m-1 >= 0 else None
            av = get(A, m+1) if m+1 < A.length() else None
            if bv is not None and av is not None and bv < mv > av:
                return m
            elif m == 0 or bv < mv:
                return findPeak(A, m+1, j)
            else:
                return findPeak(A, i, m)

        def binSearch(A, t, i, j, h):
            if i >= j:
                return -1
            
            m = (i+j) // 2
            mv = get(A, m)
            if mv == t:
                return m
            elif (h == 'L' and mv < t) or (h == 'R' and mv > t):
                return binSearch(A, t, m+1, j, h)
            else:
                return binSearch(A, t, i, m, h)

        p = findPeak(mountainArr, 0, mountainArr.length())
        i = binSearch(mountainArr, target, 0, p, 'L')
        if i > -1:
            return i
        
        return binSearch(mountainArr, target, p, mountainArr.length(), 'R')

        