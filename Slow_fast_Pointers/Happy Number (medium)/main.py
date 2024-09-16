class Solution(object):
    def isHappy(self, n):
        slow, fast = n, n
        while True:
            slow = self.get_squar(slow)
            fast = self.get_squar(self.get_squar(fast))

            if slow == fast:
                break

        return slow == 1

    def get_squar(self, num):
        _sum = 0
        while num > 0:
            digit = num % 10
            _sum += digit * digit
            num //= 10

        return _sum
