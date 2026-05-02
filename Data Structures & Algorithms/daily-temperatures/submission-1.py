class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        def bruteForce(T):
            R = []
            for i in range(len(T)):
                j = i+1
                while j < len(T) and T[j] <= T[i]:
                    j += 1
                if j < len(T):
                    R.append(j - i)
                else:
                    R.append(0)
            return R
        
        def optimized(T):
            R = [0 for _ in range(len(T))]
            S = []
            for i in range(len(T)):
                while len(S) > 0 and T[i] > S[-1][0]:
                    _, j = S.pop()
                    R[j] = i - j
                S.append((T[i], i))
            return R
        
        return optimized(temperatures)