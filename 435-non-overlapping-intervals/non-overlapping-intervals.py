class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        last_point = float("-inf")
        res = 0

        for interval in intervals:
            if interval[0] < last_point:
                res += 1
                last_point = min(last_point, interval[1])
            else:
                last_point = interval[1]
        
        return res

        