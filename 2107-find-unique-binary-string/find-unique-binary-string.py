class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        result = ""
        for idx, i in enumerate(nums):
            if nums[idx][idx] == '0':
                result += '1'
            else: 
                result += '0'
        
        return result
        