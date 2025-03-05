class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        check = [False for _ in range(n)]
        check[0] = True
        for i in range(n):
            if check[i]:
                for j in range(nums[i] + 1):
                    if i + j < n:
                        check[i + j] = True
                    if check[-1]:
                        return True
        
        return check[-1]
        