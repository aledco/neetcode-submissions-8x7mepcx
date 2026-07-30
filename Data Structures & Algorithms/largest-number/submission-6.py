class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def addSort(x, y):
            if x + y > y + x:
                return -1
            return 1

        res = list(sorted([str(n) for n in nums], key = cmp_to_key(addSort)))

        # stip leading zeroes
        i = 0
        while i < len(res)-1 and res[i] == '0':
            i += 1
        return "".join(res[i:])




