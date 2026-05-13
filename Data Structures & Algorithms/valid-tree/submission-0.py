from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def isConnected(G, n):
            Q = deque([0])
            V = {0}
            while len(Q) > 0:
                a = Q.popleft()
                for b in G[a]:
                    if b not in V:
                        Q.append(b)
                        V.add(b)
            return len(V) == n
                    

        def hasCycle(G, n):

            def dfs(G, s, P, b):
                if s in P:
                    return True
                
                for n in G[s]:
                    if n == b:
                        continue
                    if dfs(G, n, P | {s}, s):
                        return True
                return False

            for i in range(n):
                if dfs(G, i, set(), None):
                    return True
            return False

        graph = [[] for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return isConnected(graph, n) and not hasCycle(graph, n)

            
