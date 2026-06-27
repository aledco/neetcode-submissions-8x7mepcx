class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        K = set()
        for i, n in enumerate(nums):
            if n in K:
                return True
            K.add(n)
            if len(K) > k:
                K.remove(nums[i-k])
        return False
