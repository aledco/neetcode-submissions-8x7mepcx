class Solution:
    def reorganizeString(self, s: str) -> str:
        
        import heapq
        from collections import Counter

        heap = [(v, k) for k, v in Counter(s).items()]
        heapq.heapify_max(heap)

        res = []
        while len(heap) > 0:
            c1, v1 = heapq.heappop_max(heap)
            if len(res) > 0 and res[-1] == v1:
                return ""
            
            res.append(v1)

            if len(heap) > 0:
                c2, v2 = heapq.heappop_max(heap)
                res.append(v2)
                if c2-1 > 0:
                    heapq.heappush_max(heap, (c2-1, v2))

            if c1-1 > 0:
                heapq.heappush_max(heap, (c1-1, v1))
        
        return "".join(res)

                


