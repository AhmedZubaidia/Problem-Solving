class Solution:
    def max_sub_array_of_size_k(self, k, arr):
        max_sum = 0
        window_sum = 0
        start_window = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            if window_end >= k - 1:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[start_window]
                start_window += 1

        return max_sum


def main():
    sol = Solution()
    print("Maximum sum of a subarray of size K: " +
          str(sol.max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(sol.max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
