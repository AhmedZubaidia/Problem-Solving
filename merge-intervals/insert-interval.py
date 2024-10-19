class Solution(object):
    def insert(self, intervals, new_interval):
        merged = []
        i = 0

        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            merged.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(intervals[i][0], new_interval[0])
            new_interval[1] = max(intervals[i][1], new_interval[1])
            i += 1

        merged.append(new_interval)

        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged
