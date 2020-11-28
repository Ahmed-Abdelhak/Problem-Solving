"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # n , is the current version I am trying to verify, and find the first bad of it
        # the whole versions array, are already defined and you have a an API  "isBadVersion(n)"

        # a typical BinarySearch problem, implemented with While loop, instead of Recursion
        # and I am searching for the "start" bad version

        start, end = 1, n

        while(end > start):

            mid = (start + end) // 2

            if not isBadVersion(mid):    # isBadVersion is defined at leetcode
                start = mid + 1
            else:
                end = mid

        return start
