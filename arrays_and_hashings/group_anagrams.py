# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution(object):
    def groupAnagrams(self, strs):
        strs_table = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in strs_table:
                strs_table[sorted_string] = []
            strs_table[sorted_string].append(string)
        return list(strs_table.values())
