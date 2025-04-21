class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = [0]
        n = len(differences)
        for i in range(n):
            prefix.append(prefix[-1] + differences[i])
        minimum = float('inf')
        maximum = float('-inf')
        for i in prefix:
            if i > maximum:
                maximum = i
            if i < minimum:
                minimum = i
        maximum = upper - maximum
        minimum = lower - minimum
        if maximum < minimum:
            return 0
        else:
            return maximum - minimum + 1
            
            
        