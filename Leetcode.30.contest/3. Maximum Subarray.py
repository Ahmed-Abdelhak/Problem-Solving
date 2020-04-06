# Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

import math

class Solution:
    def maxSubArray(self,nums) -> int:
        if not nums:
            return 0
        local_max1, global_max1 = 0, -math.inf
        for i in range(len(nums)):
            local_max1 = max(local_max1+nums[i], nums[i])
            global_max1 = max(global_max1, local_max1)

        return global_max1


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
