import sys
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = {i: [] for i in range(n)}
        for u, v, w in times:
            G[u-1].append((v-1, w))

        D = [sys.maxsize] * n
        D[k-1] = 0

        pQ = []
        heapq.heappush(pQ, (0, k-1))

        while len(pQ) > 0:
            d, u = heapq.heappop(pQ)
            if d > D[u]:
                continue
            for v, w in G[u]:
                if D[u] + w < D[v]:
                    D[v] = D[u] + w
                    heapq.heappush(pQ, (D[v], v))

        m = max(D)
        if m == sys.maxsize:
            return -1
        return m
        
