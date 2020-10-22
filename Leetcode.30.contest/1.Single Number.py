# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4


def uniqe_number(nums):
      result = 0
      for i in nums:
            result = result ^ i 
      return result      


"""
A solution with SPACE COMPLEXITY O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_ = set()
        for i in nums:
            if i in set_:
                set_.remove(i)
            else:
                set_.add(i)\

        for i in set_:
            return i
        return -1

"""

print(uniqe_number([1, 1, 2,2,3,3,5,4,4]))
