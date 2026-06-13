class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def digit(c):
            return ord(c) - ord('0')
        
        def char(d):
            return chr(ord('0') + d)

        def stoi(s):
            n = 0
            for i in range(len(s)-1, -1, -1):
                n += digit(s[i]) * (10 ** (len(s) - 1 - i))
            return n

        def itos(n):
            if not n:
                return "0"
            
            s = []
            while n:
                s.append(char(n % 10))
                n //= 10
            return "".join(reversed(s))
        
        n = stoi(num1) * stoi(num2)
        return itos(n)