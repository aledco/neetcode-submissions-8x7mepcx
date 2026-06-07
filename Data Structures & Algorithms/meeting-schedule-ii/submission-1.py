"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        def overlappingIntervals(I):
            p = -1
            res = []
            for i in range(len(I)):
                if p == -1 or I[p].end <= I[i].start: # if the current interval does not overlap with the last interval, keep it
                    p = i
                else: # there is overlap
                    res.append(I[i])
                    if I[p].end > I[i].end: # if the last interval ends after the current interval, replace the last interval with the current
                        p = i
            return res
        
        intervals = list(sorted(intervals, key = lambda x: x.start)) # sort by start time
        res = 0
        while len(intervals) > 0:
            intervals = overlappingIntervals(intervals)
            res += 1
        return res
