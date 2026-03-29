class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        def eq(C1, C2):
            if len(C1) != len(C2):
                return False
            for e, c in C1.items():
                if e not in C2 or c != C2[e]:
                    return False
            return True
        
        counters = [(s, Counter(s)) for s in strs]
        groups = []
        for s, C in counters:
            group_to_add = None
            for group in groups:
                if eq(C, group[-1][1]):
                    group_to_add = group
                    break
            if group_to_add is None:
                group_to_add = []
                groups.append(group_to_add)
            group_to_add.append((s, C))
            
        groups = [[s for s, _ in g] for g in groups]
        return groups