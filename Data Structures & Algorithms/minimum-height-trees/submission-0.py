class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def height(graph, root, parent=None):
            h = 1
            for child in graph[root]:
                if child == parent:
                    continue
                h = max(h, 1 + height(graph, child, root))
            return h
        
        min_height = sys.maxsize
        heights = defaultdict(list)
        for i in range(n):
            h = height(graph, i)
            min_height = min(min_height, h)
            heights[h].append(i)
        return heights[min_height]



