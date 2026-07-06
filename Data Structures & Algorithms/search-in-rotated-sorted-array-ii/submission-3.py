class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def binSearch(N, t, i, j):
            print(i, j)
            if i >= j:
                return False
            
            m = (i + j) // 2
            if N[m] == t:
                return True
            elif N[i] < N[m]:
                if N[i] <= t <= N[m]:
                    return binSearch(N, t, i, m)
                else:
                    return binSearch(N, t, m+1, j)
            elif N[i] > N[m]:
                if N[m] <= t <= N[j-1]:
                    return binSearch(N, t, m+1, j)
                else:
                    return binSearch(N, t, i, m)
            else:
                while i < j and N[i] == N[m]:
                    i += 1
                return binSearch(N, t, i, j)
            
        return binSearch(nums, target, 0, len(nums))