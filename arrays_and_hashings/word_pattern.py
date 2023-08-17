class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        pattern_map = {}

        for i in range(len(pattern)):
            if pattern[i] not in pattern_map:
                pattern_map[pattern[i]] = s[i]
            if pattern[i] in pattern_map and pattern_map[pattern[i]] != s[i]:
                return False

        return True
