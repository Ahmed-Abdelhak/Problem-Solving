class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = [('#', 0)]

        for char in s:

            if char == stack[-1][0]:
                a, b = stack.pop()
                stack.append((a, b+1))

            else:
                stack.append((char, 1))

            if stack[-1][1] == k:
                stack.pop()

        return ''.join(x[0] * x[1] for x in stack)


print(Solution().removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
