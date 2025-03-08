class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(blocks)
        for i in range(0, k):
            if blocks[i] == 'B':
                count += 1
        
        minimum = k - count
        for i in range (1, n - k + 1):
            if blocks[i - 1] == 'B':  
                count -= 1
            
            if blocks[i + k - 1] == 'B':
                count += 1
            
            minimum = min(minimum, k - count)
        
        return minimum
        