class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math

        def divides(s, t):
            if len(s) % len(t) != 0:
                return False
            
            return (t * (len(s) // len(t))) == s
        
        def divisors(n):
            S, L = [], []
            for i in range(1, int(math.sqrt(n))+1):
                if n % i == 0:
                    S.append(i)
                    if i != n // i:
                        L.append(n // i)
            return S + list(reversed(L))

        def bruteForce(s1, s2):
            if len(s1) < len(s2):
                s1, s2 = s2, s1
            
            m, n = len(s1), len(s2)
            for d in divisors(n):
                k = n // d
                if m % k != 0:
                    continue
                
                t = s2[:k]
                if divides(s2, t) and divides(s1, t):
                    return t
            return ""

        return bruteForce(str1, str2)