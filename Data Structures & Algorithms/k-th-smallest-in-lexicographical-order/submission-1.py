class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def bruteForce(n, k):
            return int(
                sorted([
                    str(i) for i in range(1, n+1)
                ])[k-1]
            )
        
        # return bruteForce(n, k)

        def optimized(n, k):
            
            def count_prefixes(c):
                res = 0
                d = c+1
                while c <= n:
                    res += min(d, n+1) - c
                    c *= 10
                    d *= 10
                return res

            i, c = 1, 1
            while i < k:
                p = count_prefixes(c)
                if i+p <= k:
                    c += 1
                    i += p
                else:
                    c *= 10
                    i += 1
            return c

            # print(n, k)
            # if k == 0:
            #     if n < 10:
            #         return ""
            #     else:
            #         return "0"
            # if n < 10:
            #     assert k < 10
            #     return str(k)
            
            # digits = len(str(n))
            # for d in range(1, 10):
            #     for i in range(digits):
            #         # print(f"n={n}, d={d}, i={i}, 10**i={10**i}, d * 10**i={d * 10**i}, k={k}, d * (10**i)={d * (10**i)}")
            #         if d * (10**i) <= n:
            #             nums = min(n - (d * (10**i)) + 1, 10**i)

            #             # print(f"k={k}, nums={nums}, k-nums={k-nums}")

            #             if k - nums <= 0: # (10**i) <= 0:
            #             #     return str(d)
            #             # elif k - nums < 0:
            #                 # look for digit of kth smallest from to (10**i)
            #                 return str(d) + optimized(nums, k-1)
            #             else:
            #                 k -= nums
            # return -1
        
        return int(optimized(n, k))