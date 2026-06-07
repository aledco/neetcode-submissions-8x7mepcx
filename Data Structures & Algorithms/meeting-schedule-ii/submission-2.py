"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        def greedySimulation(I):
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
            
            I = list(sorted(I, key = lambda x: x.start)) # sort by start time
            res = 0
            while len(I) > 0:
                I = overlappingIntervals(I)
                res += 1
            return res
        
        # return greedySimulation(intervals)

        def greedy(I):
            time = [] # create an array of events. when an interval starts a meeting room is needed (+1), and when an interval ends a meeting room is freed (-1)
            for i in I:
                time.append((i.start, 1))
                time.append((i.end, -1))
            
            time = list(sorted(time)) # sort the events by time and event

            res, count = 0, 0 # keep track of how many meeting rooms are needed at any time. the result is the maximum meeting rooms needed
            for _, e in time:
                count += e
                res = max(res, count)
            return res
        
        return greedy(intervals)
