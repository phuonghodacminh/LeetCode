class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        idx1 = 0
        idx2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        while idx1 < len1 and idx2 < len2:
            if nums1[idx1][0] < nums2[idx2][0]:
                result.append(nums1[idx1])
                idx1 += 1
            elif nums1[idx1][0] > nums2[idx2][0]:
                result.append(nums2[idx2])
                idx2 += 1
            else:
                nums1[idx1][1] += nums2[idx2][1]
                result.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
        
        while idx1 < len1:
            result.append(nums1[idx1])
            idx1 += 1
        
        while idx2 < len2:
            result.append(nums2[idx2])
            idx2 += 1
        
        return result


        