class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sets = []
        for n in nums:
            set_to_add = None
            for S in sets:
                if n not in S:
                    set_to_add = S
                    break
            if not set_to_add:
                set_to_add = set()
                sets.append(set_to_add)
            set_to_add.add(n)
        
        def find_ans(sets, k):
            A = set()
            for S in reversed(sets):
                for n in S:
                    if n not in A:
                        A.add(n)
                        k -= 1
                        if k <= 0:
                            return list(A)
            return list(A)
        
        return find_ans(sets, k)