class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict

        H = nums[:k]
        C = defaultdict(int)
        for n in H:
            C[n] += 1
        heapq.heapify_max(H)
        M = [H[0]]
        i, j = 0, k
        while j < len(nums):
            a, b = nums[i], nums[j]
            C[a] -= 1
            C[b] += 1

            if H[0] == a and C[a] == 0:
                while len(H) > 0 and H[0] == a:
                    heapq.heappop_max(H)
            
            heapq.heappush_max(H, b)
            M.append(H[0])

            i += 1
            j += 1

        return M
