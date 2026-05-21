from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # idea: each letter is a node in a graph. 
        # When letter a is lexographically less than letter b, 
        # an edge is created from a to b.
        # We then topologically sort the graph to determine the order.

        def order(s1, s2):
            i = 0
            while i < len(s1) and i < len(s2):
                if s1[i] != s2[i]:
                    return (s1[i], s2[i])
                i += 1

            if len(s1) > len(s2):
                raise Exception("invalid order")
            return None

        def buildGraph(W):
            G = defaultdict(list)
            I = defaultdict(int)
            A = set()
            for i in range(len(W)):
                A |= set(words[i])
                
                j = i+1
                if j >= len(W):
                    break
                
                o = order(W[i], W[j])
                if o is None:
                    continue
                a, b = o
                G[a].append(b)
                I[b] += 1
                
            return G, I, A
        
        def topSort(G, I, A):
            Q = deque([])
            for c in A:
                if I[c] == 0:
                    Q.append(c)
            
            R = []
            while len(Q) > 0:
                c = Q.popleft()
                R.append(c)
                for n in G[c]:
                    I[n] -= 1
                    if I[n] == 0:
                        Q.append(n)
                print(c)
                print(Q)
                print(R)
                print()
            if len(R) != len(A):
                raise Exception("cycle detected")
            return "".join(R)


        try:
            G, I, A = buildGraph(words)
            print(G)
            print(I)
            print(A)
            return topSort(G, I, A)
        except:
            return ""
        
        

