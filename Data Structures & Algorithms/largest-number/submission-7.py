class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def addSort(x, y):
            if x + y > y + x:
                return -1
            return 1

        res = list(sorted([str(n) for n in nums], key = cmp_to_key(addSort)))
        if int(res[0]) == 0:
            return '0'
        return "".join(res)




