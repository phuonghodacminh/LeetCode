class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in check:
                return [check[complement], i]
            else:
                check[num] = i
        
        return []