class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict

        denominators = defaultdict(set)
        values_map = {}

        def add(a, b, v):
            nonlocal denominators, values_map
            denominators[a].add(b)
            values_map[(a, b)] = v
            denominators[b].add(a)
            values_map[(b, a)] = 1.0/v

        for (a, b), v in zip(equations, values):
            add(a, b, v)
        
        def dfs(a, b, V=None):
            nonlocal denominators, values_map

            if V is None:
                V = set()

            if (a, b) in values_map:
                return values_map[(a, b)]
            
            if (a, b) in V:
                return -1.0
            
            V.add((a, b))

            for x in denominators[a]:
                v = dfs(x, b, V)
                if v > 0:
                    add(a, b, values_map[(a, x)] * v)
                    return values_map[(a, b)]
            return -1.0

        return [dfs(a, b) for a, b in queries]

