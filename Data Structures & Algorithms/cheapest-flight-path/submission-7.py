import sys
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # idea: perform Dijkstra's algoritm starting from src. After k steps, return dist[dst]
        # Dijkstra's algorithm does not work because a shorter path may be found that breaches k stops.
        # Need to use a different shortest path algorithm

        # graph = defaultdict(list)
        # for u, v, p in flights:
        #     graph[u].append((v, p))
        
        # def dijkstra(G, n, s, d, k):
        #     D = [sys.maxsize] * n
        #     pQ = []
        #     heapq.heappush(pQ, (0, s, 0))
        #     while len(pQ) > 0:
        #         t, u, i = heapq.heappop(pQ)
                
        #         if i > k or t > D[u]:
        #             continue
        #         for v, c in G[u]:
        #             if t + c < D[v]:
        #                 D[v] = t + c
        #                 heapq.heappush(pQ, (D[v], v, i + 1))
        #     if D[d] == sys.maxsize:
        #         return -1
        #     return D[d]

        # return dijkstra(graph, n, src, dst, k)
        
        # Bellman - Ford Algorithm, augmented to support k stops constraint.
        dist = [sys.maxsize] * n
        dist[src] = 0

        for i in range(k+1):
            dist_copy = dist.copy()
            for u, v, p in flights:
                if dist[u] != sys.maxsize and dist_copy[v] > dist[u] + p:
                    dist_copy[v] = dist[u] + p
            dist = dist_copy
        if dist[dst] == sys.maxsize:
            return -1
        return dist[dst]

