class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order = {o: i for i, o in enumerate(order)}

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
            
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if not isLessThan(w1, w2, order):
                return False
        return True
