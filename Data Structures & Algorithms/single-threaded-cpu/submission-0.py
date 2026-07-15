class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        import heapq

        heap1 = []
        for i, [e, p] in enumerate(tasks):
            heapq.heappush(heap1, (
                e, p, i
            ))

        t = 1
        heap2 = []
        res = []
        while len(heap1) > 0 or len(heap2) > 0:
            while len(heap1) > 0:
                if heap1[0][0] > t:
                    break
                e, p, i = heapq.heappop(heap1)
                heapq.heappush(heap2, (p, i))

            if len(heap2) == 0:
                t += 1
            else:
                p, i = heapq.heappop(heap2)
                t += p
                res.append(i)
        return res
                
