# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False
