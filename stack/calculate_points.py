# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        score_stack = []

        for o in operations:

            # it is +, D, or C
            # if stack isn't of sufficient length, then operation is voided
            if o == "+" and len(score_stack) >= 2:
                summed = score_stack[-2] + score_stack[-1]
                score_stack.append(summed)

            elif o == "D" and len(score_stack) >= 1:
                doubled = score_stack[-1] * 2
                score_stack.append(doubled)

            elif o == "C" and len(score_stack) >= 1:
                score_stack.pop()

            else:
                score_stack.append(int(o))

        return sum(score_stack)
