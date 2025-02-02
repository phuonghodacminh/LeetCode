class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        check = True
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                check = False
                break
        
        if check:
            return True
            
        i += 1

        for j in range(len(nums) - 1):
            if nums[(i + j + 1) % len(nums)] < nums[(i + j) % len(nums)]:
                return False
        
        return True
        