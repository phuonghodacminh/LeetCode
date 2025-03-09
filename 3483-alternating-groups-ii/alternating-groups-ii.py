class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k - 1):
            colors.append(colors[i])

        n = len(colors)
        curr = 1
        count = 0
        for i in range(1, n):
            if colors[i] != colors[i - 1]:
                curr += 1
            else:
                curr = 1
            if curr >= k:
                count += 1
        
        return count