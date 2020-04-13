# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_dic = {}
        for i in s:
            if i in string_dic:
                string_dic[i] = string_dic[i] + 1
            else:
                string_dic[i] = 1

        for i in s:
            if i in string_dic and string_dic[i] == 1:
                return s.index(i)
        return -1

print(Solution().firstUniqChar("loveleetcode"))
