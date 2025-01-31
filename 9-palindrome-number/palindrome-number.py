class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        l, r = 0, len(y) - 1
        while l < r:
            if y[l] != y[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True
        