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
        
        return bruteForce(temperatures)