class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binSearch(N, t, i, j):
            if i >= j:
                return 0
            
            m = (i + j) // 2
            if N[m] == t:
                return m
            elif (
                N[m] > t and (m == 0 or N[m-1] < t)
            ):
            # ) or (
            #     N[m] < t and (m == len(N)-1 or N[m+1] > t)
            # ):
                #print(N[m] > t and (m == 0 or N[m-1] < t), "or", N[m] < t and (m == len(N)-1 or N[m+1] > t))
                return m
            elif (
                N[m] < t and (m == len(N)-1 or N[m+1] > t)
            ):
                return m+1
            elif N[m] < t:
                return binSearch(N, t, m+1, j)
            else:
                return binSearch(N, t, i, m)

        return binSearch(
            nums, target, 0, len(nums)
        )
