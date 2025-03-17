class Solution(object):
    def dp(self, obstacleGrid, memo, x, y):
        if obstacleGrid[x][y] == 1:
            memo[(x, y)] = 0
            return 0
        elif x == 0 and y == 0:
            memo[(x, y)] = 1
            return 1
        elif x < 0 or y < 0:
            memo[(x, y)] = 0
            return 0
        else:
            if (x, y) in memo:
                return memo[(x, y)]
            else:
                memo[(x, y)] = self.dp(obstacleGrid, memo, x - 1, y) + self.dp(obstacleGrid, memo, x, y - 1)
                return memo[(x, y)]
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        memo = {}
        m = len(obstacleGrid) - 1
        n = len(obstacleGrid[0]) - 1
        self.dp(obstacleGrid, memo, m, n)
        return memo[(m, n)]
        