
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution:
    def moveZeroes(self, nums) -> None:

        i = 0   # a pointer for non zero Elements

        # j is considered as a pointer that iterates the array
        # I am shifting the "non Zero" elemnts to the left
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i = i+1

        # now, I will trigger the free places at the array, to put zeros in them till the end
        for k in range(i, len(nums)):
            nums[k] = 0

        print(nums)


print(Solution().moveZeroes([0,1,0,3,12]))           




# C# solution

# public class Solution {
#     public void MoveZeroes(int[] nums) {
#          int i = 0;
#        // Shifting all nonZero elements to the left
#         for (int j = 0; j < nums.Length; j++) {    
#             if (nums[j] != 0) {
#                 nums[i++] = nums[j];   
#             }
#         }
        
#         // put zeros starting from the index after shifting till the end
#         for (int j = i; j < nums.Length; j++) {   
#             nums[j] = 0;
#         }
        
        
#     }
# }
