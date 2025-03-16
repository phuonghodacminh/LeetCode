class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = max(nums)
        check = {}
        if result > 0:
            result = 0
            for i in nums:
                if i > 0 and i not in check:
                    result += i
                    check[i] = True
        
        return result
                