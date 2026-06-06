class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        merged = set()
        for i, interval in enumerate(intervals):
            if interval[0] <= newInterval[0] <= interval[1] and interval[0] <= newInterval[1] <= interval[1]: # newInterval is contained by an existing interval. Nothing to do
                return intervals 

            if newInterval[0] <= interval[0] <= newInterval[1] or newInterval[0] <= interval[1] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                merged.add(i)
        
        newIntervals = []
        inserted = False
        for i, interval in enumerate(intervals):
            if i in merged:
                continue

            if not inserted and newInterval[0] < interval[0]:
                inserted = True
                newIntervals.append(newInterval)    
            newIntervals.append(interval) 
        
        if not inserted:
            newIntervals.append(newInterval)
        
        return newIntervals
            
        # def findInsertIndex(intervals, new):
        #     i = 0
        #     while i < len(intervals) and intervals[i][0] < new[0]:
        #         i += 1
        #     return i
        
        # i = findInsertIndex(intervals, newInterval)
        # if i >= len(intervals):
        #     intervals.append(newInterval)
        #     return intervals
        
        # to_remove = []
        # j = i
        # while j < len(intervals) and newInterval[1] >= intervals[j][0]:
        #     to_remove.append(j)
        #     newInterval[1] = max(newInterval[1], intervals[j][1])
        #     j += 1
        
        # for j in to_remove:
        #     intervals.pop(j)
        
        # intervals.insert(i, newInterval)
        # return intervals
