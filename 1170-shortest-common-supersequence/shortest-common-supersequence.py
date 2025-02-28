class Solution(object):
    def LCS (self, str1, str2, idx1, idx2, memoization):
        if idx1 == len(str1) or idx2 == len(str2):
            return 0
        if memoization[idx1][idx2] != -1:
            return memoization[idx1][idx2]
        else:
            if str1[idx1] == str2[idx2]:
                memoization[idx1][idx2] = 1 + self.LCS(str1, str2, idx1 + 1, idx2 + 1, memoization)
            else:
                memoization[idx1][idx2] = max(self.LCS(str1, str2, idx1 + 1, idx2, memoization), self.LCS(str1, str2, idx1, idx2 + 1, memoization))
        
        return memoization[idx1][idx2]
    
    def reconstruct_LCS(self, str1, str2, memoization):
        i, j = 0, 0
        lcs = []
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]: 
                lcs.append(str1[i])
                i += 1
                j += 1
            elif i + 1 < len(str1) and (j + 1 >= len(str2) or memoization[i + 1][j] >= memoization[i][j + 1]):                  
                i += 1
            else:
                j += 1

        return ''.join(lcs)

    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        memoization = [[-1] * len(str2) for _ in range(len(str1))] 
        self.LCS(str1, str2, 0, 0, memoization)
        s = self.reconstruct_LCS(str1, str2, memoization)
        result = []
        i, j = 0, 0
        for char in s:
            while str1[i] != char:
                result.append(str1[i])
                i += 1
            while str2[j] != char:
                result.append(str2[j])
                j += 1

            result.append(char)
            i += 1
            j += 1
        result.extend(str1[i:])
        result.extend(str2[j:])
        return ''.join(result)



        