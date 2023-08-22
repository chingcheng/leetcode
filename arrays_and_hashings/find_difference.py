class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        result = [[],[]]

        for n1 in nums1:
            if n1 not in nums2:
                if n1 not in result[0]:
                    result[0].append(n1)

        for n2 in nums2:
            if n2 not in nums1:
                if n2 not in result[1]:
                    result[1].append(n2)

        return result
