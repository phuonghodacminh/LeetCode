class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxi = [nums[n - 1]]
 
        for i in range(1, n):
            maxi.append(max(nums[n - i], maxi[-1]))
        
        result = 0
        for i in range(n):
            curr = maxi[n - i - 1] - nums[i]
            if curr > result:
                result = curr

        if not result:
            return -1
        else:
            return result

        