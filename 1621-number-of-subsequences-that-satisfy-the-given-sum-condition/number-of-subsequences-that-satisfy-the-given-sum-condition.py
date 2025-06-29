class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mod = 1000000007
        nums.sort()
        n = len(nums)
        power = [1]
        for i in range(1, n):
            power.append(power[-1] * 2 % mod)
        left, right = 0, n - 1
        result = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % mod
                left += 1
            else:
                right -= 1

        return result
        