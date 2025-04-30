class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            curr = i
            digits = 0
            while curr:
                curr //= 10
                digits += 1
            if not digits % 2:
                count += 1

        return count