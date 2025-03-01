class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        idx = 0
        for i in nums:
            if i != 0:
                nums[idx] = i
                idx += 1
        
        while idx < n:
            nums[idx] = 0
            idx += 1
        
        return nums

        