class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def overlapping(i1, i2):
            if i2 < i1:
                i1, i2 = i2, i1
            
            if i2[0] >= i1[1]:
                return False
            return True

        def dfs(I, i=0, p=-1):
            if i >= len(I):
                return 0
            
            res = dfs(I, i+1, p) # skip the current interval
            if p == -1 or I[p][1] <= I[i][0]:
                res = max(
                    res,
                    1 + dfs(I, i+1, i)  # take the current interval if it does not overlap with the previous
                )
            return res
        
        # intervals = list(sorted(intervals)) # sort by start time
        # return len(intervals) - dfs(intervals)

        def dynamicProgramming(I):
            # dp[i] = the maximum number of non-overlapping intervals we can keep ending at interval i
            n = len(I)
            dp = [0] * n
            for i in range(n):
                dp[i] = 1
                for j in range(i):
                    if I[j][1] <= I[i][0]: # interval j ends before interval i starts
                        dp[i] = max(dp[i], 1 + dp[j])
            return max(dp)

        intervals = list(sorted(intervals, key=lambda x: x[1])) # sort by end time
        return len(intervals) - dynamicProgramming(intervals)


        # intervals = list(sorted(intervals))
        # i, res = 0, 0
        # while i < len(intervals):
        #     if i+1 < len(intervals) and overlapping(intervals[i], intervals[i+1]):
        #         res += 1
        #         if i+2 < len(intervals) and overlapping(intervals[i+1], intervals[i+2]):# and not overlapping(intervals[i], intervals[i+2]):
        #             if overlapping(intervals[i], intervals[i+2]):
        #                 res += 1  
        #                 i += 3
        #             else:
        #                 i += 2
        #         else:
        #             i += 1
        #     else:
        #         i += 1
        # return res
