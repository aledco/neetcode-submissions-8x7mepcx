class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict

        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[b].add(a)

        cache = {}
        def isPrereq_dfs(G, u, v):
            nonlocal cache
            if (u, v) in cache:
                return cache[(u, v)]
            
            if u == v:
                cache[(u, v)] = False
                return cache[(u, v)]
            if u in G[v]:
                cache[(u, v)] = True
                return cache[(u, v)]

            for c in G[v]:
                if isPrereq_dfs(G, u, c):
                    cache[(u, v)] = True
                    return cache[(u, v)]
            cache[(u, v)] = False
            return cache[(u, v)]
        
        res = []
        for u, v in queries:
            res.append(isPrereq_dfs(graph, u, v))
        return res
