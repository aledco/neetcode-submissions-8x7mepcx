class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        # idea: we can continue incrementing a subarray until it reaches the miniumn value of the 
        # subarray in target, then recurse on each half of the array around the min value

        # each recursive call consists of finding the pivots (all occurences of the min value),
        # add the min value to the result (we can increment initial that many times),
        # then recurse on all subarrays between the pivots

        def divide(target, i, j, v=0):
            if i >= j:
                return 0
            
            min_value = min(target[i:j]) # can speed this up with interval min structure (Segment Tree)
            res = min_value - v
            
            l = i
            for r in range(i, j+1):
                if r == j or target[r] == min_value:
                    res += divide(target, l, r, min_value)
                    l = r+1
            return res
        
        # return divide(target, 0, len(target))

        def greedy(target):
            if len(target) == 0:
                return 0

            res = target[0]
            for i in range(1, len(target)):
                if target[i] > target[i-1]:
                    res += target[i] - target[i-1]
            return res
        
        return greedy(target)
