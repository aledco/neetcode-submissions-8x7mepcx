class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict, deque

        graph = defaultdict(set)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].add(b)
            indegree[b] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        prereq_map = defaultdict(set)
        while len(queue) > 0:
            u = queue.popleft()
            for v in graph[u]:
                prereq_map[v] = prereq_map[v] | prereq_map[u] | {u}
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return [u in prereq_map[v] for u, v in queries]
        


        # graph = defaultdict(set)
        # for a, b in prerequisites:
        #     graph[b].add(a)

        # cache = {}
        # def isPrereq_dfs(G, u, v):
        #     nonlocal cache
        #     if (u, v) in cache:
        #         return cache[(u, v)]
            
        #     if u == v:
        #         cache[(u, v)] = False
        #         return cache[(u, v)]
        #     if u in G[v]:
        #         cache[(u, v)] = True
        #         return cache[(u, v)]

        #     for c in G[v]:
        #         if isPrereq_dfs(G, u, c):
        #             cache[(u, v)] = True
        #             return cache[(u, v)]
        #     cache[(u, v)] = False
        #     return cache[(u, v)]
        
        # res = []
        # for u, v in queries:
        #     res.append(isPrereq_dfs(graph, u, v))
        # return res
