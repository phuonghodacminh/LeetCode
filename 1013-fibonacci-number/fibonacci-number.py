class Solution(object):
    def dp(self, n, memoization):
        if memoization[n] != -1:
            return memoization[n]
        memoization[n] = self.dp(n - 1, memoization) + self.dp(n - 2, memoization)
        return memoization[n]
        
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        memoization = [-1] * (n + 1)
        memoization[0], memoization[1] = 0, 1
        return self.dp(n, memoization)