# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stack = []
        closed_to_open = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for c in s:
            if c in closed_to_open:
                if stack and stack[-1] == closed_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
