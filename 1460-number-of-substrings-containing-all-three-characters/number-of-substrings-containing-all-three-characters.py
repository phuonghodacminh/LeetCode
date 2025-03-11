class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        l = 0
        count = defaultdict(int)
        result = 0
        for r in range(n):
            count[s[r]] += 1
            while len(count) == 3:
                result += (n - r)
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
        
        return result

