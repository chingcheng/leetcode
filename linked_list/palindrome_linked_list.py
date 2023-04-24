# Given the head of a singly linked list,
# return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] != nums[r]:
                return False

            l += 1
            r -= 1
        return True
