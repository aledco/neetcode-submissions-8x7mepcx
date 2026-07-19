class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        if n <= 2:
            return list(range(n))

        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        leaves = deque([i for i in range(n) if indegree[i] == 1])

        while len(leaves) > 0:
            if n <= 2:
                return list(leaves)

            n_leaves = len(leaves)
            for _ in range(n_leaves):
                i = leaves.popleft()
                n -= 1
                for j in graph[i]:
                    indegree[j] -= 1
                    if indegree[j] == 1:
                        leaves.append(j)

        # graph = defaultdict(list)
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # def height(graph, root, parent=None):
        #     h = 1
        #     for child in graph[root]:
        #         if child == parent:
        #             continue
        #         h = max(h, 1 + height(graph, child, root))
        #     return h
        
        # min_height = sys.maxsize
        # heights = defaultdict(list)
        # for i in range(n):
        #     h = height(graph, i)
        #     min_height = min(min_height, h)
        #     heights[h].append(i)
        # return heights[min_height]



