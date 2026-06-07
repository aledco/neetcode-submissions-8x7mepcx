class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for interval in sorted(intervals):
            if len(res) == 0 or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1] = [
                    min(res[-1][0], interval[0]),
                    max(res[-1][1], interval[1])
                ]
        return res