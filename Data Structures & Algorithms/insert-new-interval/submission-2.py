class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                return newIntervals + [newInterval] + intervals[i:]
            elif newInterval[0] > interval[1]:
                newIntervals.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1])
                ]
        return newIntervals + [newInterval]

        # merged = set()
        # for i, interval in enumerate(intervals):
        #     if interval[0] <= newInterval[0] <= interval[1] and interval[0] <= newInterval[1] <= interval[1]: # newInterval is contained by an existing interval. Nothing to do
        #         return intervals 

        #     if newInterval[0] <= interval[0] <= newInterval[1] or newInterval[0] <= interval[1] <= newInterval[1]:
        #         newInterval[0] = min(newInterval[0], interval[0])
        #         newInterval[1] = max(newInterval[1], interval[1])
        #         merged.add(i)
        
        # newIntervals = []
        # inserted = False
        # for i, interval in enumerate(intervals):
        #     if i in merged:
        #         continue

        #     if not inserted and newInterval[0] < interval[0]:
        #         inserted = True
        #         newIntervals.append(newInterval)    
        #     newIntervals.append(interval) 
        
        # if not inserted:
        #     newIntervals.append(newInterval)
        
        # return newIntervals
