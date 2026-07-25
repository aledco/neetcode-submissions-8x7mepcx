class Solution:
    def minEnd(self, n: int, x: int) -> int:
        import math

        b = int(math.log2(x))+1
        Z = []
        for i in range(b):
            if (x >> i) & 1 == 0:
                Z.append(i)

        O = [x]
        for i in Z:
            new = []
            for y in O:
                y = y | (1 << i)
                new.append(y)
            O += new

        p = (n-1) // len(O)
        return (p << b) + O[(n-1) % len(O)]

        # if len(O) >= n:
        #     return O[n-1]
        
        # o, c = 1, len(O)
        # while True:
        #     for y in O:
        #         y = (o << b) + y
        #         c += 1
        #         if c == n:
        #             return y
        #     o += 1
