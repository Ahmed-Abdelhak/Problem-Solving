"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""


#Brute Force solution:
"""
is doubly nested two for-loops,
to keep iterating over the elements, the second for loop will start from the index of the current outer loop +1 , to find if the next warmer element, and subtract the difference in indices
"""

#Better solution using stack:
"""
first, iterate over the array, and I will keep pushing elements into stack, if the next element is smaller than the top of stack, once I reach an element > top of stack, then pop elements and subtract their indices ( the current element in my loop - stack.pop())


# in case of no warmer in the right, then our output will be 0s ( that's why our output array is initialized with 0s) 
"""
def dailyTemperatures(self, T):
      stack = []
      ans = [0] * len(T)
      for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                 top_index = stack.pop() 
                 ans[top_index] = i - top_index
            stack.append(i)
      return ans
      
          

