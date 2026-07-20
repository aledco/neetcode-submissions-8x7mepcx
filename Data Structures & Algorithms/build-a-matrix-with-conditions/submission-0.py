class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        rG = defaultdict(list)
        rI = {i: 0 for i in range(1, k+1)}
        for a, b in rowConditions:
            rG[a].append(b)
            rI[b] += 1
        
        cG = defaultdict(list)
        cI = {i: 0 for i in range(1, k+1)}
        for l, r in colConditions:
            cG[l].append(r)
            cI[r] += 1
        
        rS = self.topsort(rG, rI, k)
        if len(rS) == 0:
            return []
        
        cS = self.topsort(cG, cI, k)
        if len(cS) == 0:
            return []
        
        rS = {v: i for i, v in enumerate(rS)}
        cS = {v: i for i, v in enumerate(cS)}
        
        matrix = [[0] * k for _ in range(k)]
        for n in range(1, k+1):
            i, j = rS[n], cS[n]
            matrix[i][j] = n
        return matrix 
    
    def topsort(self, G, I, k):
        from collections import deque

        order = []
        queue = deque([i for i, d in I.items() if d == 0])

        while len(queue) > 0:
            u = queue.popleft()
            order.append(u)
            
            for v in G[u]:
                I[v] -= 1
                if I[v] == 0:
                    queue.append(v)
        
        if len(order) != k:
            return []
        return order
        
