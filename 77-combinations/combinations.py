class Solution(object):
    def backtrack(self, n, k, start, result, combination):
        if len(combination) == k:
            result.append(combination[:])
            return

        for i in range(start, n + 1):
            combination.append(i)
            self.backtrack(n, k, i + 1, result, combination)
            combination.pop()  

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(n, k, 1, result, [])
        return result


        