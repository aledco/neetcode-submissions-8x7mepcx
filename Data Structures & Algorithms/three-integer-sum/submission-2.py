class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
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

                