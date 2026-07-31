class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if num == "0":
            return True
        
        for d in num:
            if d not in ('0', '1', '6', '8', '9'):
                return False
        
        if num[-1] == '0': # canot have leading zeroes
            return False
        
        def strobogramaticPair(a, b):
            if a in ('0', '1', '8') and b in ('0', '1', '8'):
                return True
            if a in ('6', '9') and b in ('6', '9') and a != b:
                return True
            return False
        
        i, j = 0, len(num)-1
        while i <= j:
            if not strobogramaticPair(num[i], num[j]):
                return False
            i += 1
            j -= 1
        return True

        
