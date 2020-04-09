# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation:
# 1.power(2) + 9.power(2) = 82
# 8.power(2) + 2.power(2) = 68
# 6.power(2) + 8.power(2) = 100
# 1.power(2) + 0.power(2) + 0.power(2) = 1


# Hint : (Floyd's Cycle Detection Algorithm) : https://cs.stackexchange.com/a/45540
# the cycle will be broken, when the travelled distance are equal (slow == fast)

# ![Floyd's Cycle Detection Algorithm](images\floyd_cycle_detect.png)


class Solution:
    def isHappy(self, n: int) -> bool:

        def next_num(num):
            return sum(map(lambda x: int(x)**2, str(num)))

        slow, fast = n, next_num(n)    # a tuple  ## slow and fast pointers

        while slow != fast and fast != 1:    
            slow = next_num(slow)           # here the slow
            fast = next_num(next_num(fast)) # the fast ,  we ace it

        return fast == 1 or not slow == fast   ## solution is when it's == 1   only !


print(Solution().isHappy(7))


