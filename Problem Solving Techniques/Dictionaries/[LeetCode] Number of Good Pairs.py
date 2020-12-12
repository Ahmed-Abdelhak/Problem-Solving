"""
1512. Number of Good Pairs
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

"""
Brute Force Solution :   O(n)^2

- double nested for loops with a counter that increases whenever the following conditions is True  ----->   nums[i] == nums[j] and i < j
"""


# O(n) Solution:
class Solution(object):
    def numIdenticalPairs(self, nums):
        values = {}
        counter = 0
        for i in range(len(nums)):
            if nums[i] in values:
                values[nums[i]] += 1
            else:
                values[nums[i]] = 1

        for i in values:
            if values[i] > 1:
                counter += (values[i] * (values[i]-1)) / 2

        return counter


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
