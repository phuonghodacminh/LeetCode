class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        hashmap = {}
        ans = []
        count = 0
        for i in answers:
            if i not in hashmap:
                hashmap[i] = 1
                ans.append(i)
            else:
                hashmap[i] += 1
        
        for i in ans:
            group = i + 1
            remain = hashmap[i] % group
            if remain:
                count += (group - remain)
        
        return count + len(answers)