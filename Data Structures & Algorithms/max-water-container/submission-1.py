class Solution:
    def maxArea(self, heights: List[int]) -> int:

        def solve(H):
            i, j = 0, len(H)-1
            m = 0
            while i < j:
                l, r = H[i], H[j]
                a = min(l, r) * (j - i)
                m = max(m, a)
                if l == r:
                    i += 1
                    j -= 1
                elif l < r:
                    i += 1
                else:
                    j -= 1
            return m
    
        return solve(heights)