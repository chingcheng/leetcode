# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = k-1
        minimized = float('inf')

        while r < len(nums):
            diff = nums[r] - nums[l]
            if diff < minimized:
                minimized = diff
            l += 1
            r += 1
        return minimized
