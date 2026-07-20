class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        import math
        from collections import defaultdict

        #G = defaultdict(list)
        # I = defaultdict(int)
        uf = UnionFind([(n, i) for i, n in enumerate(nums)])
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1:
                    uf.union((nums[i], i), (nums[j], j))
        print(uf.parent, uf.rank)
        return uf.isConnected()

class UnionFind:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 1 for n in nodes}
    
    def find(self, n):
        if self.parent[n] == n:
            return n
        
        return self.find(self.parent[n])
    
    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        
        if ap == bp:
            return False
        
        if self.rank[ap] > self.rank[bp]:
            self.parent[bp] = ap
            self.rank[ap] += self.rank[bp]
        else:
            self.parent[ap] = bp
            self.rank[bp] += self.rank[ap]

    def isConnected(self):
        return max(self.rank.values()) == len(self.rank) # there is a node that is the representative of all nodes
                