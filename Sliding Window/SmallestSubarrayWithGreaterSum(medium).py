class Solution(object):
    def minSubArrayLen(self, target, nums):

        start_window = 0
        min_len = 10000000  # 10000000 mean math.inf
        sum_window = 0

        for end_window in range(len(nums)):

            sum_window += nums[end_window]

            while sum_window >= target:
                min_len = min(min_len, end_window - start_window + 1)
                sum_window -= nums[start_window]
                start_window += 1

        if min_len == 10000000:
            return 0

        return min_len






