# Given an array of integers where 1 ≤ a[i] ≤ n(n=size of array), some elements appear twice and others appear once.

# Find all the elements of[1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4, 3, 2, 7, 8, 2, 3, 1]

# Output:
# [5, 6]




#Brute Force Solution :   space: O(n) , Time:  O(n)
"""
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        
        nums_set = set()
        
        for i in nums:
            nums_set.add(i)
        
        for i in range(1,len(nums)+1):
            if not i in nums_set:
                output.append(i)
            
        return output
"""


# optimum solution:  space: O(1) , Time:  O(n)

class Solution:
      
      def findDisappearedNumbers(self, nums) :
            output = []

            # because of All the elements are in the range [1, N]
            # means I can use the corresponding indices to represent the elemnts                                                                    themselves

            for i in range(len(nums)):

                  # array starts from zero, so we will subtract 1
                  new_index = abs(nums[i]) - 1

                  if(nums[new_index]) > 0:
                        nums[new_index] *= -1

            for i in range(1, len(nums)+1):
                  if nums[i-1] > 0:
                        output.append(i)

            return output


print(Solution().findDisappearedNumbers([1,1]))
