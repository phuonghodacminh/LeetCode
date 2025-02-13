class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [0] * 26
        count = 0 
        for i in s:
            o = ord(i)
            arr[o - 97] += 1
        
        for i in arr:
            if i == 0:
                count += 0
            else:
                if i % 2 == 0:
                    count += 2
                else:
                    count += 1
        
        return count
        