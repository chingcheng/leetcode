class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        for n in nums:
            if n < 0:
                result *= -1
            if n == 0:
                return 0
            if n > 0:
                result *= 1

        return result
