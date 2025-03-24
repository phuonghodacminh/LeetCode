class Solution(object):
    def backtrack(self, nums, n, k, subset, result):
        result.append(subset[:])
        if k == n:
            return
        for i in range(k, n):
            subset.append(nums[i])
            self.backtrack(nums, n, i + 1, subset, result)
            subset.pop(-1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        subset = []
        result = []
        self.backtrack(nums, n, 0, subset, result)
        return result
        