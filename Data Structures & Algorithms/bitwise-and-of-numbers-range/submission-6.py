class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        def helper(a, b):
            if len(a) == 0 or len(b) == 0:
                return '0' * max(len(a), len(b))

            if len(a) != len(b) or a[0] != b[0] or a == '0' or b == '0':
                return '0' * max(len(a), len(b))

            return a[0] + helper(a[1:], b[1:])

        a, b = bin(left).replace("0b", ""), bin(right).replace("0b", "")
        c = helper(a, b)
        return int(c, 2)
