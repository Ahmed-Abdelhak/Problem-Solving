"""
In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

example : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Fibonacci(9) means the first nine elements of the sequence
"""


"""
Dynamic programming concept means that, from a solved example, you can use it to solve the whole problem.

Dynamic Programming = Divide and Conqure + Memoization (caching)

# ![Dynamic Programming with Fibonacci](images\Dynamic_Programming_Fibonacci.png)
"""

class Fib:
      def fibonacci(self,n):
            self.__cache = {}                  # caching to avoid recalculation
            if n in self.__cache:
                return self.__cache[n]
            else:
                  if n < 2:                      # BaseCase
                        return n
                  else:                          # recusrsive case
                      self.__cache[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
                      return self.__cache[n]


print(Fib().fibonacci(9))                      

