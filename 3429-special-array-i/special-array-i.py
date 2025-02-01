class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            if (nums[i] - nums[i + 1]) % 2 == 0:
                return False
        
        return True
        