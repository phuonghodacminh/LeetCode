class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n + 1):
            square = i * i
            s = str(square)
            if self.backtrack(s, 0, 0, i):
                count += square

        return count
    
    def backtrack(self, s, idx, check, i):
        if idx == len(s):
            if check == i:
                return True
            else:
                return False
        
        for l in range(1, len(s) - idx + 1):
            t = s[idx: idx + l]
            num = int(t)
            if self.backtrack(s, idx + l, check + num, i):
                return True

        return False

            
            

        