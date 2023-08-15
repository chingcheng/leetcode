class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        result = 0
        max_count = 0

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
            if count[n] > max_count:
                result = n

        return result
        