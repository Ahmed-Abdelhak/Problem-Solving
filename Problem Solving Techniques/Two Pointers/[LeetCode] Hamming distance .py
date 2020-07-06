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

      maxLen = max(len(b1), len(b2))
      smallLen = len(b1) if maxLen == len(b2) else len(b2)

      counter =0
      for i in range(0, maxLen):
          if i >= smallLen:
                  counter = counter +1
          else:
                  if b1[i] != b2[i]:
                      counter = counter + 1
      return counter

      

print(Solution().hammingDistance(888888888888,25921952982))
