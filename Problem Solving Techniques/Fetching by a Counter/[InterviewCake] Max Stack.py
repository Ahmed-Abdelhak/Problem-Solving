"""
Use your Stack class to implement a new class MaxStack with a method get_max() that returns the largest element in the stack. get_max() should not remove the item.

Your stacks will contain only integers.

Gotchas
What if we push several items in increasing numeric order (like 1, 2, 3, 4...), so that there is a new max after each push()? What if we then pop() each of these items off, so that there is a new max after each pop()? Your algorithm shouldn't pay a steep cost in these edge cases.

You should be able to get a runtime of O(1)O(1) for push(), pop(), and get_max().

Breakdown
A just-in-time ↴ approach is to have get_max() simply walk through the stack (popping all the elements off and then pushing them back on) to find the max element. This takes O(n)O(n) time for each call to get_max(). But we can do better.

To get O(1)O(1) time for get_max(), we could store the max integer as a member variable (call it max). But how would we keep it up to date?

For every push(), we can check to see if the item being pushed is larger than the current max, assigning it as our new max if so. But what happens when we pop() the current max? We could re-compute the current max by walking through our stack in O(n)O(n) time. So our worst-case runtime for pop() would be O(n)O(n). We can do better.

What if when we find a new current max (new_max), instead of overwriting the old one (old_max) we held onto it, so that once new_max was popped off our stack we would know that our max was back to old_max?

What data structure should we store our set of maxes in? We want something where the last item we put in is the first item we get out ("last in, first out").

We can store our maxes in another stack!
"""


import unittest

class MaxStack(object):

    # Implement the push, pop, and get_max methods

    def __init__(self):
        self.items = []
        self.max = 0
        self.counter = 0
        self.cached_max = {}

    def push(self, item):
        if item >= self.max:
            self.max = item
            self.counter += 1
            self.cached_max[self.counter] = item

        self.items.append(item)

    def pop(self):
        if not self.items:
            return None

        elif len(self.items) == 1:
            self.max = 0

        elif self.items[-1] == self.max:
            self.max = self.cached_max.get(self.counter - 1)  #O(1)
            self.counter -= 1
           
           
            """
            # O(n)
            new_max = 0
            for i in range(0,len(self.items)-1):
                if self.items[i] > new_max:
                    new_max = self.items[i]
            self.max = new_max
            """

        return self.items.pop()

    def get_max(self):
        return self.max



# Tests

class Test(unittest.TestCase):

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
