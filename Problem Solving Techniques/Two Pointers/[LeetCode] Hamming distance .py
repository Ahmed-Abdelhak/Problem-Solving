"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
      b1 = bin(x)[2:]
      b2 = bin(y)[2:]
      
      b1Len = len(b1)
      b2Len = len(b2)
      zerosNeeded = 0
      if b1Len > b2Len:
          zerosNeeded = b1Len - b2Len
          b2 = ('0' * zerosNeeded) + b2
      elif b2Len > b1Len:
          zerosNeeded = b2Len - b1Len
          b1 = ('0' * zerosNeeded) + b1

      counter =0
      for i in range(0, len(b1)):
           if b1[i] != b2[i]:
               counter = counter + 1

      return counter

      

print(Solution().hammingDistance(1,4))
