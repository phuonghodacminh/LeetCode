class Solution(object):
    def backtracking(self, candidates, result, curr, currSum, target):
        if currSum == target:
            result.add(tuple(sorted(curr)))
            return 
        elif currSum > target:
            return
        else:
            for i in candidates:
                curr.append(i)
                currSum += i
                self.backtracking(candidates, result, curr, currSum, target)
                curr.pop()
                currSum -= i
            
            return
            
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = set()
        curr = []
        self.backtracking(candidates, result, curr, 0, target)
        rs = [list(t) for t in result]
        return rs
        

        