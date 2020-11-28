"""
Solve the game "Guess a number", find a secret integer between 1 and 1000000
in less than 50 guesses. Write a function that solves the game without user input and returns the
solution by using the function verify() which is defined with the following
specification:
function verify(guess: integer) -> integer
Argument:
     guess (integer) the number to verify
Returns:
     0 if the guess is the solution, your program won
     -1 if the solution is smaller than the guess parameter
     1  if the solution is bigger than the guess parameter

Warning: You are not allowed to call verify() more that 50 times or you lose.
"""

import random

random_num = random.randint(1,1000000)

def guess_the_num(start, end, no_of_guess = 0 ):
      
      mid = (end+start) // 2
      
      if no_of_guess > 50:
            return -1
      
      if end < start:
             return -1
      
      verify_result = verify(mid)
      no_of_guess += 1  
      if verify_result == 0:
            return mid
      elif verify_result == 1:
            return guess_the_num(mid+1, end, no_of_guess)
      else:
            return guess_the_num(start, mid - 1, no_of_guess)


def verify(guess):
      solution = random_num
      if guess == solution:
            return 0
      elif solution < guess:
            return -1
      else:
            return 1
      
      
print(guess_the_num(1, 1000000, no_of_guess = 0 ))
