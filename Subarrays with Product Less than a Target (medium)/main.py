class Solution:
  def findSubarrays(self, arr, target):
      # Resultant list to store all valid subarrays.
      result = []

      # Variable to store the product of elements in the current subarray.
      product = 1.0

      # Left boundary of the current subarray.
      left = 0

      # Iterate over the array using 'right' as the right boundary of the current subarray.
      for right in range(len(arr)):
          # Update the product with the current element.
          product *= arr[right]

          # If the product is greater than or equal to the target, slide the left boundary to
          # the right until product is less than target.
          while product >= target and left < len(arr):
              product /= arr[left]
              left += 1

          # Create a temporary list to store the current subarray.
          temp_list = []

          # Iterate from 'right' to 'left' and add all these subarrays to the result.
          for i in range(right, left - 1, -1):
              # Add the current element at the beginning of the list.
              temp_list.insert(0, arr[i])

              # Add the current subarray to the result.
              result.append(list(temp_list))

      # Return the result.
      return result


# Example usage
sol = Solution()
print(sol.findSubarrays([2, 5, 3, 10], 30))
print(sol.findSubarrays([8, 2, 6, 5], 50))
