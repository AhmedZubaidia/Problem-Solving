class Solution:
    def findLength(self, str1, k):
        window_start = 0
        max_length = 0
        freq_chars = {}


        for window_end in range(len(str1)):
            right = str1[window_end]

            if right not in freq_chars:
                freq_chars[right] = 0

            freq_chars[right]+=1


            while len(freq_chars) > k:

                left = str1[window_start]
                freq_chars[left]-=1

                if freq_chars[left] == 0:
                    del freq_chars[left]
                window_start+=1

            max_length = max(max_length,window_end - window_start + 1)

        return max_length



def main():
    sol = Solution()
    print("Length of the longest substring: "
          + str(sol.findLength("araaci", 2)))
    print("Length of the longest substring: "
          + str(sol.findLength("araaci", 1)))
    print("Length of the longest substring: "
          + str(sol.findLength("cbbebi", 3)))


main()
