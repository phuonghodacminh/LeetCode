class Solution(object):
    def maxGrid(self, grid, xpos, ypos):
        if xpos < 0 or ypos < 0 or xpos >= len(grid) or ypos >= len(grid[0]) or grid[xpos][ypos] == 0:
            return 0
        else:
            fish_count = grid[xpos][ypos]
            grid[xpos][ypos] = 0
            fish = fish_count + self.maxGrid(grid, xpos + 1, ypos) + self.maxGrid(grid, xpos - 1, ypos) + self.maxGrid(grid, xpos, ypos + 1) + self.maxGrid(grid, xpos, ypos - 1)
            return fish


    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for ii, i in enumerate(grid):
            for ij, j in enumerate(i):
                if j != 0:
                    count = max(count, self.maxGrid(grid, ii, ij))
        
        return count


        