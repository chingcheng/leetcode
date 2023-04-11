# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase,
# typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        d_1 = {}
        for char in s:
            if char not in d_1:
                d_1[char] = 0
            d_1[char] += 1
        d_2 = {}
        for char in t:
            if char not in d_2:
                d_2[char] = 0
            d_2[char] += 1
        if d_1 == d_2:
            return True
        return False
