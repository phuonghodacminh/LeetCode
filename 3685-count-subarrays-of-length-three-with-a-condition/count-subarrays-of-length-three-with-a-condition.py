class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n - 2):
            if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
                count += 1
        return count