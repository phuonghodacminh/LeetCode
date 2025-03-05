class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        for i in range(n):
            count += (i * 4)
        
        return count
        