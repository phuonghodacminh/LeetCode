class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        prime = [2, 3]
        limit = int(math.sqrt(right))
        for i in range(5, limit + 1, 2):
            check = True
            to = int(math.sqrt(i))
            for j in prime:
                if j > to:
                    break
                else:
                    if i % j == 0:
                        check = False
                        break
            
            if check:
                prime.append(i)
        
        prev = -1
        curr = -1
        result = [-1, -1]
        for i in range(left, right + 1):
            if i < 2:
                continue
                
            check = True
            to = int(math.sqrt(i))
            for j in prime:
                if j > to:
                    break
                else:
                    if i % j == 0:
                        check = False
                        break 

            if check:
                prev = curr
                curr = i

            if ((result[0] == -1 and result[1] == -1) or (result[1] - result[0] > curr - prev)) and prev != -1:
                result[0] = prev
                result[1] = curr
            
            if result[1] - result[0] == 2:
                return result
        
        return result
        