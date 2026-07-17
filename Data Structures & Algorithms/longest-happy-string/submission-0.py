import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        def greedy(a, b, c):
            opts = list(
                filter(
                    lambda x: x[0] > 0, 
                    [
                        (a, 'a'),
                        (b, 'b'),
                        (c, 'c')
                    ]
                )
            )
            heapq.heapify_max(opts)

            res = []
            while len(opts) > 0:
                c, v = heapq.heappop_max(opts)

                temp = []
                while len(res) >= 2 and res[-1] == res[-2] == v:
                    if len(opts) == 0:
                        return "".join(res)
                    
                    temp.append((c, v))
                    c, v = heapq.heappop_max(opts)
                
                
                res.append(v)
                if c-1 > 0:
                    heapq.heappush_max(opts, (c-1, v))

                if len(temp) > 0:
                    for c, v in temp:
                        heapq.heappush_max(opts, (c, v))
            return "".join(res)
        
        return greedy(a, b, c)