class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def validLength(ribbons, k, l):
            c = 0
            for r in ribbons:
                c += r // l
                if c >= k:
                    return True
            return False
        
        total = sum(ribbons)
        left, right = 1, total // k
        max_length = 0
        while left <= right:
            mid = (left + right) // 2
            if validLength(ribbons, k, mid):
                max_length = mid
                left = mid + 1
            else:
                right = mid - 1
        return max_length