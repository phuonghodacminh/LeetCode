class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in nums:
            sum += i
        n = len(nums)
        final = -1
        result = 0
        for i in range(n):
            result += i * nums[i]
        curr = result
        for i in range(1, n):
            curr += (sum - n * nums[final])
            if curr > result:
                result = curr
            final -= 1
            
        return result
        