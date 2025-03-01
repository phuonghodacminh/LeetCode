class Solution(object):
    def dp(self, n, memoization):
        if memoization[n] != -1:
            return memoization[n]
        else:
            memoization[n - 1] = self.dp(n - 1, memoization) 
            memoization[n - 2] = self.dp(n - 2, memoization)
            memoization[n] = memoization[n - 1] + memoization[n - 2]
            return memoization[n]
        
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        memoization = [-1 for _ in range(n + 1)]
        memoization[0] = 0
        memoization[1] = 1
        self.dp(n, memoization)
        return memoization[n]

        