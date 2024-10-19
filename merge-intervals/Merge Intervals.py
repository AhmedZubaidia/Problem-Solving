
#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
  def merge(self, intervals):

    if len(intervals) < 2 :
      return intervals

    intervals.sort(key = lambda x : x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):

      interval= intervals[i]
      if interval.start <= end:
        end = max(interval.end,end)

      else:
        mergedIntervals.append(Interval(start, end))
        start = interval.start
        end = interval.end

    mergedIntervals.append(Interval(start, end))
    return mergedIntervals


    return mergedIntervals
