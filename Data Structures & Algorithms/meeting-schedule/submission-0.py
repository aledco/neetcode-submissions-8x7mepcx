"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def sorting(I):
            I = list(sorted(I, key = lambda x: x.start))
            for i in range(len(I)):
                if i+1 < len(I) and I[i+1].start < I[i].end:
                    return False
            return True
        
        return sorting(intervals)
