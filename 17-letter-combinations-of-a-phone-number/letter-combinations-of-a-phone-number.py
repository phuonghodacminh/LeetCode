class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        check = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        s = ""
        n = len(digits)
        if n == 0:
            return result
        else:
            self.backtrack(0, digits, check, result, s)
            return result

    def backtrack(self, index, digits, check, result, s):
        p = digits[index]
        for i in check[p]:
            s += i
            if index == len(digits) - 1:
                result.append(s)
                s = s[:-1]
            else:
                self.backtrack(index + 1, digits, check, result, s)
                s = s[:-1]


        




        