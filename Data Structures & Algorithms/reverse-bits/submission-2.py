class Solution:
    def reverseBits(self, n: int) -> int:

        def itob(n):
            s = bin(n).replace('0b', '')
            while len(s) != 32:
                s = '0' + s
            return s

        def revs(s):
            return "".join(reversed(s))
        
        def btoi(s):
            return int(s, 2)
        
        return btoi(revs(itob(n)))