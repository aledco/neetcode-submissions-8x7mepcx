class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        criteria = [False, False, False]
        for ai, bi, ci in triplets:
            if ai == target[0] and bi <= target[1] and ci <= target[2]:
                criteria[0] = True
            if ai <= target[0] and bi == target[1] and ci <= target[2]:
                criteria[1] = True
            if ai <= target[0] and bi <= target[1] and ci == target[2]:
                criteria[2] = True
        return criteria[0] and criteria[1] and criteria[2]
