# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K = 5
# Here, we are asked to find the average of all contiguous subarrays of size ‘5’ in the given array. Let’s solve this:

# For the first 5 numbers(subarray from index 0-4), the average is: (1+3+2+6-1)/5 = > 2.2(1+3+2+6−1)/5 = >2.2
# The average of next 5 numbers(subarray from index 1-5) is: (3+2+6-1+4)/5 = > 2.8(3+2+6−1+4)/5 = >2.8
# For the next 5 numbers(subarray from index 2-6), the average is: (2+6-1+4+1)/5 = > 2.4(2+6−1+4+1)/5 = >2.4
# …
# Here is the final output containing the averages of all contiguous subarrays of size 5:

# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

# ![Sliding Window Pattern](images\sliding_window_pattern.png)

def find_average(nums,k):
      result = list(range(len(nums) - k + 1))
      sum = 0
      left_window = 0

      for i in range(len(nums)):
            sum = sum + nums[i]
            if i >= k-1:                          # at the last element of k
                result[left_window] = (sum / k)   # assign the first result to the average
                sum = sum - nums[left_window]     # subtract the first element of the window
                left_window = left_window +1

      return result          


print(find_average([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
