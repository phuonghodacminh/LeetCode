class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        min = 1
        max = -1
        count = 0
        result = 0
        for i in piles:
            if i > max:
                max = i
        
        while min + 1 < max:
            count = 0
            mid = (min + max) / 2
            for i in piles:
                if i % mid:
                    count += (i / mid + 1)
                else:
                    count += (i / mid)
            
            if count == h:
                result = mid
                break
            else:
                if count > h:
                    min = mid
                else:
                    max = mid

        if min == max - 1:
            count = 0
            for i in piles:
                if i % min:
                    count += (i / min + 1)
                else:
                    count += (i / min)
            
            if count <= h:
                return min
            else:
                return max

        count = h
        i = result
        while True:
            count = 0
            i -= 1
            for j in piles:
                if j % i:
                    count += (j / i + 1)
                else:
                    count += (j / i)
            
            if count == h:
                result = i
            else:
                break
        
        return result


