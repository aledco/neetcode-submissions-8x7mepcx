class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict
        from functools import cache

        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[b].add(a)
        
        G = graph 

        @cache
        def isPrereq_dfs(u, v):
            if u == v:
                return False
            if u in G[v]:
                return True
            
            for c in G[v]:
                if isPrereq_dfs(u, c):
                    return True
            return False
        
        #def isPrereq_dfs(G, u, v):

        
        res = []
        for u, v in queries:
            res.append(isPrereq_dfs(u, v))
        return res
