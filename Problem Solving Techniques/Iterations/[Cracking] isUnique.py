"""
find the duplicate numbers of an array (in-place) with O(n) runtime and O(1) space 
"""

import math

def isUnique(nums =[2,3,4,5,4,3,5,2,0,1]):
      output = set()
      for i in range(len(nums)):
            num = abs(nums[i])
            if(nums[num] < 0):
                  if( abs(nums[i]) not in output):
                        output.add(abs(nums[i]))
            else:
                  nums[num] = -1 * nums[num]
      return output



print(isUnique())
