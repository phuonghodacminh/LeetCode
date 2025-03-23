class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        sum = 0
        if nums[0] < 0:
            curr = nums[0]
        else:
            curr = 0

        for i in nums:
            if sum < 0:
                sum = i
            else:
                sum += i
            if sum > curr:
                curr = sum
        return curr
