import sys
import heapq

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
        
        # return bruteForce(intervals, queries)

        def optimized(I, Q):
            I = list(sorted(I))
            O, H = {}, []
            i = 0
            for q in sorted(Q):
                while i < len(I) and I[i][0] <= q:
                    s = I[i][1] - I[i][0] + 1
                    heapq.heappush(H, (s, I[i][1]))
                    i += 1

                while len(H) > 0 and H[0][1] < q:
                    heapq.heappop(H)
                if len(H) == 0:
                    O[q] = -1
                else:
                    O[q] = H[0][0]

            return [O[q] for q in Q]

        return optimized(intervals, queries)