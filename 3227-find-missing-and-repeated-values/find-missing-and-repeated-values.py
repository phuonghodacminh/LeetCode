class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        hashmap = [0 for _ in range(n * n)]
        sum = 0
        for i in range(n):
            for j in range(n):
                hashmap[grid[i][j] - 1] += 1
        
        repeat = -1
        miss = -1
        for i in range(len(hashmap)):
            if hashmap[i] == 2:
                repeat = i + 1
            if hashmap[i] == 0:
                miss = i + 1
        
        return [repeat, miss]
        

