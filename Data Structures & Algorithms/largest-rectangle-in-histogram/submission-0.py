class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def bruteForce(H):
            M = 0
            for i in range(len(H)):

                j = i-1
                while j >= 0 and H[j] >= H[i]:
                    j -= 1
                
                k = i+1
                while k < len(H) and H[k] >= H[i]:
                    k += 1
                
                L = (k - j - 1)
                A = L * H[i]
                M = max(M, A)
            
            return M
        
        return bruteForce(heights)
                    