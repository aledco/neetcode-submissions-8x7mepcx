from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        G = defaultdict(list)
        for a, b, in sorted(tickets, reverse=True):
            G[a].append(b)
        
        S = ["JFK"]
        P = []

        while len(S) > 0:
            u = S[-1]
            if len(G[u]) > 0:
                v = G[u].pop()
                S.append(v)
            else:
                P.append(S.pop())

        return list(reversed(P))
            