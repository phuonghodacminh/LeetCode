class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        check = [[-1 for _ in range(n)] for _ in range(n)]
        maxLength = 1
        start = 0
        for i in range(n):
            check[i][i] = 1
            if i < n - 1:
                if s[i] == s[i + 1]:
                    check[i][i + 1] = 1
                    start = i
                    maxLength = 2
                else:
                    check[i][i + 1] = 0
        
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and check[i + 1][j - 1] == 1:
                    check[i][j] = 1
                    start = i
                    maxLength = l
        
        return s[start:start + maxLength]

        

        


        