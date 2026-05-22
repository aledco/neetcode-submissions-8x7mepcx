import sys
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
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

