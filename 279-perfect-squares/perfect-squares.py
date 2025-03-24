class Solution(object):
    def __init__(self):
        self.memo = {}

    def backtrack(self, n, squares):
        if n == 0:
            return 0
        if n in self.memo:
            return self.memo[n]
        
        min_count = float('inf')
        for square in squares:
            if square > n:
                break
            min_count = min(min_count, 1 + self.backtrack(n - square, squares))
        
        self.memo[n] = min_count
        return min_count

    def numSquares(self, n):
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        return self.backtrack(n, squares)
