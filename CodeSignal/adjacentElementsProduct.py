"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.
"""

def adjacentElementsProduct(inputArray):
  product = min(inputArray)

  if len(inputArray) > 2:
      for i in range(len(inputArray)-1):
          if inputArray[i] * inputArray[i+1] > product:
              product = inputArray[i] * inputArray[i+1]
  else:
      return inputArray[0] * inputArray[1]

  return product
