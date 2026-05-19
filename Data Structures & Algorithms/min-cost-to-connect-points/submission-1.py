import sys

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        u = 0
        cost = 0
        visited = [False] * n
        dist = [sys.maxsize] * n

        for _ in range(n-1):
            visited[u] = True
            m = -1
            for v in range(n):
                if visited[v]:
                    continue
                dist[v] = min(
                    dist[v],
                    abs(points[v][0] - points[u][0]) + abs(points[v][1] - points[u][1])
                )
                if m == -1 or dist[v] < dist[m]:
                    m = v
            cost += dist[m]
            u = m
        return cost


# class UnionFind:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
    
#     def find(self, u):
#         if self.parent[u] == u:
#             return u
#         return self.find(self.parent[u])
    
#     def union(self, u, v):
#         u_root = self.find(u)
#         v_root = self.find(v)
#         if u_root == v_root:
#             return False
#         else:
#             self.parent[v_root] = u_root
#             return True
    


# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)

#         graph = []
#         for i in range(n):
#             xi, yi = points[i]
#             for j in range(i+1, n):
#                 xj, yj = points[j]
#                 d = abs(xi - xj) + abs(yi - yj)
#                 graph.append((d, i, j))
#         graph.sort()

#         uf = UnionFind(n)

#         cost = 0
#         for d, i, j in graph:
#             if uf.union(i, j):
#                 cost += d
#         return cost


        