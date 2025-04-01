class Solution(object):
    def df(self, questions, index, memo):
        if index in memo:
            return memo[index]
        elif index >= len(questions):
            memo[index] = 0
            return 0
        else:
            memo[index] = max(self.df(questions, index + 1, memo), questions[index][0] + self.df(questions, index + questions[index][1] + 1, memo))
            return memo[index]
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        index = 0
        memo = {}
        self.df(questions, index, memo)
        return memo[0]
        