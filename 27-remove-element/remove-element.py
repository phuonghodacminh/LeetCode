class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        count = 0
        for i in nums:
            if i != val:
                nums[idx] = i
                idx += 1
                count += 1
        
        return count
        
        
        