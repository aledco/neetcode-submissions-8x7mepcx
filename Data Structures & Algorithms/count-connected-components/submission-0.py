class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def bfs(G, i, V):
            Q = deque([i])
            V.add(i)
            while len(Q) > 0:
                i = Q.popleft()
                for j in G[i]:
                    if j in visited:
                        continue
                    Q.append(j)
                    V.add(j)

        visited = set()
        count = 0
        for i in range(n):
            if i in visited:
                continue
            
            bfs(graph, i, visited)
            count += 1
        return count