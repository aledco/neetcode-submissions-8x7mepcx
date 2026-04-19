class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def getKth(A, B, k):
            if len(B) < len(A):
                A, B = B, A
            if len(A) == 0:
                return B[k-1]
            elif k == 1:
                return min(A[0], B[0])
            else:
                i = min(len(A), k//2)
                j = min(len(B), k//2)
                if A[i-1] <= B[j-1]:
                    return getKth(A[i:], B, k - i)
                else:
                    return getKth(A, B[j:], k - j)
        
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return getKth(nums1, nums2, (total + 1) // 2)
        else:
            return (
                getKth(nums1, nums2, total // 2) + 
                getKth(nums1, nums2, total // 2 + 1)
            ) / 2
