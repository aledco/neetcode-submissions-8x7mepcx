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
        
        def optimized(H):
            S = []
            L = [-1] * len(H)
            for i in range(len(H)):
                while len(S) > 0 and H[S[-1]] >= H[i]:
                    S.pop()
                if len(S) > 0:
                    L[i] = S[-1]
                S.append(i)
            
            S = []
            R = [len(H)] * len(H)
            for i in range(len(H) - 1, -1, -1):
                while len(S) > 0 and H[S[-1]] >= H[i]:
                    S.pop()
                if len(S) > 0:
                    R[i] = S[-1]
                S.append(i)
            
            M = 0
            for i in range(len(H)):
                L[i] += 1
                R[i] -= 1
                M = max(
                    M,
                    H[i] * (R[i] - L[i] + 1) 
                )
            return M
        
        return optimized(heights)
                
                
        
                    