class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
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
            
        def solve(N):
            from collections import Counter
            N = list(sorted(N))
            C = Counter(N)
            S = set()
            i = 0
            while i < len(N) and N[i] <= 0:
                j = len(N)-1
                while j > i+1:
                    l, r = N[i], N[j]
                    m = -(l+r)
                    if m in C:
                        c = C[m]
                        if l == m:
                            c -= 1
                        if r == m:
                            c -= 1
                        if c > 0:
                            A = [l, m, r]
                            T = tuple(sorted(A))
                            if T not in S:
                                S.add(T)
                                yield A
                    j -= 1
                i += 1
                    

        return [x for x in solve(nums)]
            # i, j = 0, len(N)-1
            # while i < j and N[i] < 0:
            #     l, r = N[i], N[j]
            #     k = binSearch(N, l+r, i, j+1)
            #     if k > -1:
            #         m = N[k]
            #         if l != m and m != r:
            #             yield [l, m, r]
            #         i += 1
            #         j -= 1
            #     else:
            #         if l + r >= r:

                