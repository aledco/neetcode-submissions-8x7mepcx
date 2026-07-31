class NumArray:

    def __init__(self, nums: List[int]):
        p = 0
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)
        
        self.suffix = [0]
        for n in reversed(nums):
            self.suffix.append(self.suffix[-1] + n)
        self.suffix = list(reversed(self.suffix))

        self.total = sum(nums)
        self.n = len(nums)

    def sumRange(self, left: int, right: int) -> int:
        p = self.prefix[left]
        s = self.suffix[right+1]
        return self.total - p - s

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)