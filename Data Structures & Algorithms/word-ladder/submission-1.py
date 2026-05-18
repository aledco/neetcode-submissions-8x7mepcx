import string
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def climb(W, w):
            for i, c in enumerate(w):
                for d in string.ascii_lowercase:
                    if d == c:
                        continue
                    s = w[:i] + d + w[i+1:]
                    if s in W:
                        yield s
                    
        def bfs(W, e):
            c = 0
            Q = deque([e])
            V = {e}
            M = {}
            while len(Q) > 0:
                
                nQ = deque([])
                while len(Q) > 0:
                    e = Q.popleft()
                    M[e] = c
                    for w in climb(W, e):
                        if w in V:
                            continue
                        nQ.append(w)
                        V.add(w)

                c += 1
                Q = nQ
            return M

        W = set(wordList)
        if endWord not in W:
            return 0
        
        M = bfs(W, endWord)

        R = [M[w] for w in climb(M, beginWord)]

        if len(R) == 0:
            return 0
        return min(R) + 2