class Solution(object):
    def dp(self, grid, x, y, memo):
        if x < 0 or y < 0:
            return 100000000
        elif x == 0 and y == 0:
            memo[(0, 0)] = grid[0][0]
            return memo[(0, 0)]
        else:
            if (x, y) in memo:
                return memo[(x, y)]
            else:
                memo[(x, y)] = grid[x][y] + min(self.dp(grid, x - 1, y, memo), self.dp(grid, x, y - 1, memo))
                return memo[(x, y)]
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        memo = {}
        m = len(grid) - 1
        n = len(grid[0]) - 1
        self.dp(grid, m, n, memo)
        return memo[(m, n)]

        