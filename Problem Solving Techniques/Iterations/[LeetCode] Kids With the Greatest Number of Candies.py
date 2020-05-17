from typing import List

"""
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
"""

# runtime ( 32 ms )
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [candy + extraCandies >= max_candy for candy in candies]




# -------------------------------------------------------------------------


# Slow solution  (runtime : 60 ms)
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max = candies[0]

        for el in candies:
            if el > max:
                max = el

        min_pass = max - extraCandies

        output = []

        for i in candies:
            if i < min_pass:
                output.append(False)
            else:
                output.append(True)

        return output
"""
