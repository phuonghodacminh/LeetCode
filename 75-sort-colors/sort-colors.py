class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
            else:
                blue += 1
        
        for i in range(red):
            nums[i] = 0
        
        for i in range(red, red + white):
            nums[i] = 1
        
        for i in range(red + white, red + white + blue):
            nums[i] = 2
        
        return nums
        