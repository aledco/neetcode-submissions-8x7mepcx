class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        # at each node, we need to start at the node, visit all apples in the nodes children, and come back to the node
        # then the solution to node u with children v and w is minTime(v) + minTime(w) + (1 for each v and w that has at least one apple)

        from collections import defaultdict

        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        def dfs(G, A, r=0, p=-1):
            if r is None:
                return 0
            
            res = 0
            for n in G[r]:
                if n == p:
                    continue
                x = dfs(G, A, n, r)
                res += x
            
            if res == 0 and not A[r]:
                return 0 # no apples in this subtree
            
            if p > -1:
                return res + 2 # time for children + time to visit this node and leave this node
            return res # root does not need time to visit the node

        return dfs(G, hasApple)