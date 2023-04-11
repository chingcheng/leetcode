# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return -1

        # index = -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         index = i
        # return index
