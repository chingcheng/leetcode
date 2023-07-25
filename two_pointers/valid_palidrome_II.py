# Given a string s, return true if the s can be palindrome
# after deleting at most one character from it.


class Solution(object):
    def validPalindrome(self, s):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                skipLeft = s[l+1:r+1]
                skipRight = s[l:r]
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
            l += 1
            r -= 1
        return True
