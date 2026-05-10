from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)


        def topSort(G, n):
            I = defaultdict(int)
            for c, P in G.items():
                for p in P:
                    I[p] += 1

            Q = deque([c for c in range(n) if I[c] == 0])

            d = 0
            while len(Q) > 0:
                c = Q.popleft()
                d += 1
                for p in G[c]:
                    I[p] -= 1
                    if I[p] == 0:
                        Q.append(p)
            return d == n

        return topSort(graph, numCourses)

        # def isCyclic(G, c, P):
        #     if c in P:
        #         return True
            
        #     for p in G[c]:
        #         if isCyclic(G, p, P | {c}):
        #             return True
        #     return False

        # for c in range(numCourses):
        #     if isCyclic(graph, c, set()):
        #         return False
        # return True
        

            
