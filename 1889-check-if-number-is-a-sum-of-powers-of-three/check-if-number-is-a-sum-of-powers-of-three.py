class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1:
            if n % 3 == 2:
                return False
            else:
                n /= 3
        
        return True
        