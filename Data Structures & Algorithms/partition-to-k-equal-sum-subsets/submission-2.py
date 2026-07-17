class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if len(nums) < k:
            return False
        
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        if max(nums) > target:
            return False

        def backtrack(nums, k, target, sums=None, i=0):
            if sums is None:
                sums = [0] * k
            
            if i >= len(nums):
                for j in range(k):
                    if sums[j] != target:
                        return False
                return True
            
            valid = []
            seen = set()
            for j in range(k):
                if sums[j] not in seen:
                    valid.append(j)
                    seen.add(sums[j])
            
            for j in valid:
                if sums[j] + nums[i] <= target:
                    sums[j] += nums[i]
                    if backtrack(nums, k, target, sums, i+1):
                        return True
                    sums[j] -= nums[i]
            return False
        
        return backtrack(list(sorted(nums)), k, target)

        def optimized(nums, k, target, current_sum=0, indices_used=None):
            if indices_used is None:
                indices_used = set()
            
            if current_sum == target:
                k -= 1
            
            if k == 0: 
                return len(indices_used) == len(nums)
            
            for i in range(len(nums)):
                if i not in indices_used and current_sum + nums[i] <= target:
                    indices_used.add(i)
                    if optimized(nums, k, target, current_sum + nums[i], indices_used):
                        return True
                    indices_used.remove(i)
            return False
        
        # return optimized(list(sorted(nums)), k, target)
                
            
            


            

            

            