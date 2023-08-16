class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_d = {}
        for i, n in enumerate(nums1):
            nums1_d[n] = i

        result = [-1]*len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1_d:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    index = nums1_d[nums2[i]]
                    result[index]=nums2[j]
                    break

        return result
