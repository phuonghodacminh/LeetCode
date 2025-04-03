class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = []
        suffix = [-1 for _ in range(n)]
        result = 0
        curr = 0        
        for i in range(n):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(max(prefix[-1], nums[i]))
        
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = max(suffix[i + 1], nums[i])
        
        for i in range(n):
            if i == 0 or i == n - 1:
                continue
            else:
                curr = (prefix[i - 1] - nums[i]) * suffix[i + 1]
                if curr > result:
                    result = curr
        
        return result
        