class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        from collections import Counter

        counts = Counter(s)
        res = []
        i = 0
        while i < len(s):
            unconsumed = {s[i]}
            j = i
            while j < len(s) and len(unconsumed) > 0:
                counts[s[j]] -= 1
                if counts[s[j]] > 0:
                    unconsumed.add(s[j])
                elif s[j] in unconsumed:
                    unconsumed.remove(s[j])

                j += 1
            
            res.append(j-i)
            i = j
        return res

