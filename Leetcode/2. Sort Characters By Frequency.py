# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


class Solution:
    def frequencySort(self, s: str) -> str:
        chars = {}

        for i in s:
            if i in chars:
                chars[i] = chars[i] + 1
            else:
                chars[i] = 1

        # I need to sort the elements in the dictionary by values
        chars = {k: v for k, v in sorted(
            chars.items(), key=lambda item: item[1], reverse=True)}

        values = ''

        for k in chars:
            values = values + chars[k] * k

        return values


print(Solution().frequencySort("tree"))