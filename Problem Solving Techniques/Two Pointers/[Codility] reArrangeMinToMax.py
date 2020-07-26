"""
Given an integer, re-arrange the integer such that first and last digit will be at first and second, second and second last digit will be at third and fourth position from left of the re-arranges integer and so on.
Example:
Input -> 12345678, Output -> 18273645
Input -> 1234567, Output -> 1726354  

"""


def reArrangeMinToMax(arr):
      i = 0
      j = len(arr) - 1
      re_arranged_arr = []
      while i<=j:
            if i<j :
                re_arranged_arr.append(arr[i])
                re_arranged_arr.append(arr[j])
                i+=1
                j-=1
            elif i==j:
                re_arranged_arr.append(arr[i])
                break
      return re_arranged_arr

# print(reArrangeMinToMax([1,2,3,4,5,6,7,8]))
print(reArrangeMinToMax([1,2,3,4,5,6,7]))


