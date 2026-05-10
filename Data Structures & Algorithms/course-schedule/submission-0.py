from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def isCyclic(G, c, P):
            if c in P:
                return True
            
            for p in G[c]:
                if isCyclic(G, p, P | {c}):
                    return True
            return False

        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)
        
        for c in range(numCourses):
            if isCyclic(graph, c, set()):
                return False
        return True
        

            
