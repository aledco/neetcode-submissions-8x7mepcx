class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        def sol1(s):
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

        # return sol1(s)

        def sol2(s):

            indices = {}
            for i, c in enumerate(s):
                indices[c] = i
                
            res = []
            i = 0
            while i < len(s):
                e = indices[s[i]]
                j = i+1
                while j < e:
                    e = max(e, indices[s[j]])
                    j += 1
                res.append(e+1-i)
                i = e + 1
            return res
        
        return sol2(s)


