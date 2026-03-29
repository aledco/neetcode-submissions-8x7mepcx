class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        C = Counter(nums)

        freq = [[] for _ in nums]
        for n, c in C.items():
            freq[c-1].append(n)
        
        A = []
        for F in reversed(freq):
            for n in F:
                A.append(n)
                if len(A) == k:
                    return A

        # sets = []
        # for n in nums:
        #     set_to_add = None
        #     for S in sets:
        #         if n not in S:
        #             set_to_add = S
        #             break
        #     if not set_to_add:
        #         set_to_add = set()
        #         sets.append(set_to_add)
        #     set_to_add.add(n)
        
        # def find_ans(sets, k):
        #     A = set()
        #     for S in reversed(sets):
        #         for n in S:
        #             if n not in A:
        #                 A.add(n)
        #                 k -= 1
        #                 if k <= 0:
        #                     return list(A)
        #     return list(A)
        
        # return find_ans(sets, k)