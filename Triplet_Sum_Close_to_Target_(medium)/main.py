import math


class Solution:
    def searchTriplet(self, arr, target_sum):

        arr.sort()
        smallest_diff = math.inf
        diff = 0
        smallest_list = []

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1
            while left < right:
                diff = target_sum - (arr[i] + arr[left] + arr[right])

                if diff == 0:
                    return [arr[i], arr[left], arr[right]]

                if abs(diff) < abs(smallest_diff) or abs(diff) == abs(smallest_diff) and diff > smallest_diff:
                    smallest_list = [arr[i], arr[left], arr[right]]
                    smallest_diff = diff

                if diff > 0:
                    left += 1
                else:
                    right -= 1


        return smallest_list
def main():
    sol = Solution()
    print(sol.searchTriplet([-1, 0, 2, 3], 2))
    print(sol.searchTriplet([-3, -1, 1, 2], 1))
    print(sol.searchTriplet([1, 0, 1, 1], 100))
    print(sol.searchTriplet([0, 0, 1, 1, 2, 6], 5))


main()
