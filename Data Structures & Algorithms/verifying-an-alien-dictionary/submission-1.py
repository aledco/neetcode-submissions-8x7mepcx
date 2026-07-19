class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def iteratePairs(L):
            for i in range(len(L)-1):
                yield L[i], L[i+1]
            
        def isLessThan(w1, w2, order):
            j = 0
            while j < min(len(w1), len(w2)):
                if order[w1[j]] < order[w2[j]]:
                    return True
                elif order[w1[j]] > order[w2[j]]:
                    return False
                else:
                    j += 1
            
            return j == len(w1)
        
        order = {o: i for i, o in enumerate(order)}
        for w1, w2 in iteratePairs(words):
            if not isLessThan(w1, w2, order):
                return False
        return True
