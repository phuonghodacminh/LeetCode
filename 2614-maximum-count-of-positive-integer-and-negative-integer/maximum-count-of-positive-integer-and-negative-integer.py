class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
        
        negative = l
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] > 0:
                r = mid - 1
            else:
                l = mid + 1
        
        positive = len(nums) - r - 1
        return max(negative, positive)
        