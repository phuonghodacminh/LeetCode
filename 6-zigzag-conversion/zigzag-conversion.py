class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        m = [[] for _ in range(numRows)]
        u = numRows - 1
        d = 0
        t = 0
        check = True
        for i in range(len(s)):
            m[t].append(s[i])
            if check:
                t += 1
            else:
                t -= 1

            if t == d or t == u:
                check = not check
        
        result = ''.join(str(char) for row in m for char in row)
        return result


        