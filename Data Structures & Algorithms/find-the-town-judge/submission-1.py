class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        AtoB = defaultdict(set)
        BtoA = defaultdict(set)
        for a, b in trust:
            AtoB[a].add(b)
            BtoA[b].add(a)
        for i in range(1, n+1):
            if len(BtoA[i]) == n-1 and i not in BtoA[i]: # everyone except i one trusts i
                if len(AtoB[i]) == 0: # i trusts no one
                    return i
        return -1
