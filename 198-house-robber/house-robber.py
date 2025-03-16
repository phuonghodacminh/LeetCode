class Solution(object):
    def dp(self, nums, idx, memo):
        n = len(nums)
        if idx in memo:
            return memo[idx]
        elif n == 1:
            memo[idx] = nums[0]
            return nums[0]
        elif n == 0:
            memo[idx] = 0
            return 0
        else:
            memo[idx] = max(nums[0] + self.dp(nums[2:], idx + 2, memo), self.dp(nums[1:], idx + 1, memo))
            return memo[idx]
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        idx = 0
        self.dp(nums, idx, memo)
        return memo[0]
        
        