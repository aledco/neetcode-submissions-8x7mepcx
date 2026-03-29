class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce

        zeroes = len(list(filter(lambda x: x == 0, nums)))

        if zeroes == 0:
            P = reduce(lambda x, y: x * y, nums)
            O = [P // n for n in nums]
            return O
        elif zeroes == 1:
            P = reduce(lambda x, y: x * y, filter(lambda x: x != 0, nums))
            O = [0 if n != 0 else P for n in nums]
            return O 
        else:
            O = [0 for _ in nums]
            return O