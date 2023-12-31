class Solution:
    def searchTriplets(self, arr, target):
        arr.sort()
        sum_less_triplets = 0

        for i in range(0, len(arr) - 2):

            left = i + 1
            right = len(arr) - 1

            while left < right:

                sum_of_triplet = arr[i] + arr[left] + arr[right]
                sum_of_right_left = arr[right] + arr[left]
                what_we_have = [arr[i], arr[left], arr[right]]
                target_value = target

                if sum_of_triplet < target:
                    what_we_have = [arr[i], arr[left], arr[right]]
                    sum_less_triplets += 1
                    left += 1

                if sum_of_right_left > target:
                    right -= 1

        return sum_less_triplets


def main():
    sol = Solution()
    print(sol.searchTriplets([-1, 0, 2, 3], 3))
    print(sol.searchTriplets([-1, 4, 2, 1, 3], 5))


main()
