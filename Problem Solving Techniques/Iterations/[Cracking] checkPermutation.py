"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other
"""

# brute force solution is to sort the two arrays, iterate over any of them using two pointers and check the equality of the values of the corresponding one  [ return s.sort() == t.sort() ] 

def isPermutation(s, t):
      
      if(len(s) != len(t)):
            return False

      # I want to check each character is the same in each of them (using a helper arr of ascii)
      ascii_arr = [0] * 128
      for i in s:
            ascii_arr[ord(i)] += 1   # converting the character to its ascii int
      
      for i in t:
            ascii_arr[ord(i)] -= 1
            if(ascii_arr[ord(i)] < 0):
                  return False
      
      return True
     
      
print(isPermutation('125', '532'))
