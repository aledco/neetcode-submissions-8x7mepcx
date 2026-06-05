import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        def divideAndConquer(N, i, j):
            
            def findMaxSumFromMiddle(N, i, j, m):
                max_left, max_right = -sys.maxsize, -sys.maxsize
                s = 0
                for k in range(m-1, i-1, -1):
                    s += N[k]
                    max_left = max(max_left, s)
                s = 0
                for k in range(m, j):
                    s += N[k]
                    max_right = max(max_right, s)
                # print("maxFromMiddle:", i, j, m, max_left, max_right)
                return max_left + max_right

            if j-i == 1:
                return N[i]
            
            m = (i + j) // 2
            left = divideAndConquer(N, i, m)
            right = divideAndConquer(N, m, j)
            middle = findMaxSumFromMiddle(N, i, j, m)
            # print(i, j, m, left, right, middle)
            return max(
                left,
                right,
                middle
            )
        
        return divideAndConquer(nums, 0, len(nums))
            
            