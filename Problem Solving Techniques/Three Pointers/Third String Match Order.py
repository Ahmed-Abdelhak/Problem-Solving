"""
Write a program that receives three strings and tells if the third string is a result of mixing the two first strings together while keeping their respective order.
Ex.:
- abc def adbecf --> true
- abc def abdecf --> true
- abc def adbcfe --> false
          adbefc --> false

# 1- third length is sum of the two, otherwise return False
# 2- three pointer i,j,k = 0
# 3- iterate over the third string
# 4- if i < len(arr1)) && arr3[k] == arr1[i] :  i += 1
# 5- elif  j < len(arr2) && j < i arr3[k] == arr2[i] :  j += 1
# 5- else: return False

"""


def third_string_is_combination_in_order(str1,str2,str3):
      if len(str3) != len(str1) + len(str2) or not str3:
            return False
      
      i = 0
      j = 0
      
      for k in range(len(str3)):
          if i < len(str1) and str3[k] == str1[i]  :
                i += 1
          elif j < len(str2) and str3[k] == str2[j] and j < i:
                j += 1
          else:
                return False
          
      return True          
            
            
print(third_string_is_combination_in_order('abc', 'def', 'adbefc'))
      
      
