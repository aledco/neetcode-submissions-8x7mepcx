class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def getRuns(S):
            R = []
            i = 0
            while i < len(S):
                s = S[i]
                j = i+1
                r = 1
                while j < len(S) and S[j] == s:
                    r += 1
                    j += 1
                R.append((s, r))
                i = j
            return R

        def processRun(R, i, k):
            c, L = R[i]
            j = i+1
            while j < len(R):
                d, J = R[j]
                if d == c:
                    L += J  
                else:
                    if k >= J:
                        L += J
                        k -= J
                    else:
                        L += k
                        return L
                j += 1
            
            if k > 0:
                j = i - 1
                while j >= 0:
                    d, J = R[j]
                    if d == c:
                        L += J  
                    else:
                        if k >= J:
                            L += J
                            k -= J
                        else:
                            L += k
                            return L
                    j -= 1
            return L

        def solve(S, k):
            R = getRuns(S)
            if len(R) == 0:
                return 0
            elif len(R) == 1:
                return R[0][1]
                    
            m = 0 
            for i in range(len(R)):
                L = processRun(R, i, k)
                m = max(m, L)
            return m

        return solve(s, k)