class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)


        def topSort(G, n):
            I = defaultdict(int)
            for c, P in G.items():
                for p in P:
                    I[p] += 1

            Q = deque([c for c in range(n) if I[c] == 0])
            
            O = []
            while len(Q) > 0:
                c = Q.popleft()
                O.append(c)
                for p in G[c]:
                    I[p] -= 1
                    if I[p] == 0:
                        Q.append(p)
            if len(O) == n:
                return list(reversed(O))
            return []

        return topSort(graph, numCourses)