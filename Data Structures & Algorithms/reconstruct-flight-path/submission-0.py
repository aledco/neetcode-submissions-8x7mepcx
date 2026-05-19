from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        G = defaultdict(list)
        for a, b, in tickets:
            heapq.heappush(G[a], b)
        
        S = ["JFK"]
        P = []

        while len(S) > 0:
            u = S[-1]
            if len(G[u]) > 0:
                v = heapq.heappop(G[u])
                S.append(v)
            else:
                P.append(S.pop())

        return list(reversed(P))
            