from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon = Counter('balloon')
        count = Counter(text)

        result = len(text)

        for c in balloon:
            result = min(result, count[c] // balloon[c])

        return result

