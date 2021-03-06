"""
URLify: Write a method to replace all spaces in a string with '%2e: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith JJ, 13
Output: "Mr%2eJohn%2eSmith"

"""

def urlify(s,size):
      return s[:size].replace(' ', '%20')    # o(n) space and runtime


print(urlify('Mr John Smith    ', 13))
