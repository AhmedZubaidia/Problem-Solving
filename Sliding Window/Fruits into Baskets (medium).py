import math


class Solution:
    def findLength(self, fruits):
        count = collections.defaultdict(int)

        left, total, result = 0, 0, 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[left]
                count[f] -= 1
                total -= 1
                left += 1

                if not count[f]:
                    count.pop(f)

            result = max(result, total)

        return result
