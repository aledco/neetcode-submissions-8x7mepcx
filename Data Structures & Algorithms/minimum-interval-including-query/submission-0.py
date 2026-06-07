import sys

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        def bruteForce(I, Q):
            O = []
            for q in Q:
                m = sys.maxsize
                for a, b in I:
                    if a <= q <= b:
                        m = min(m, b-a+1)
                if m == sys.maxsize:
                    O.append(-1)
                else:
                    O.append(m)
            return O
        
        return bruteForce(intervals, queries)