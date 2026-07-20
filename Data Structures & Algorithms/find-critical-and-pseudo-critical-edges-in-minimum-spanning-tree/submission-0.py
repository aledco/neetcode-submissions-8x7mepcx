class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(u, v, w, i) for (i, [u, v, w]) in enumerate(edges)]
        edges = list(sorted(edges, key=lambda x: x[2]))

        uf = UnionFind(n)
        mst_weight = 0
        for u, v, w, _ in edges:
            if uf.union(u, v):
                mst_weight += w

        critical, pseudo = [], []
        for u1, v1, w1, i in edges:

            weight = 0
            uf = UnionFind(n)
            for u2, v2, w2, j in edges:
                if i == j: # skip the current edge
                    continue
                
                if uf.union(u2, v2):
                    weight += w2
            
            # if graph becomes disconnected, or mst weight increases, this edge is critical
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue
            
            # try to create the mst with the current edge
            uf = UnionFind(n)
            uf.union(u1, v1)
            weight = w1
            for u2, v2, w2, j in edges:
                if uf.union(u2, v2):
                    weight += w2
            
            # if the weight with this edge is the minium, it is a pseudo edge
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]
            
    
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, i):
        if self.parent[i] == i:  # i is the representative
            return i
        
        return self.find(self.parent[i]) # else find the parents representative
    
    def union(self, i, j):
        ir = self.find(i)
        jr = self.find(j)
        
        if ir == jr:
            return False
        
        if self.rank[ir] > self.rank[jr]:
            self.parent[jr] = ir
            self.rank[ir] += self.rank[jr]
        else:
            self.parent[ir] = jr
            self.rank[jr] += self.rank[ir]
        return True
    
