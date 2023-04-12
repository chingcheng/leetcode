# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted
# in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
        return left
