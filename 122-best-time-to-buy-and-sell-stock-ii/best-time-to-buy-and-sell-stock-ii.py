class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = -1
        sell = -1
        profit = 0
        n = len(prices)
        check = True
        for i in range(n):
            if i == n - 1:
                if buy == i or buy < sell:
                    continue
                else:
                    profit += prices[i] - prices[buy]
            else:
                if prices[i] > prices[i + 1]:
                    sell = i
                    if buy != -1 and not check:
                        profit += (prices[sell] - prices[buy])
                        check = True
                else:
                    if check:
                        buy = i
                        check = False
        
        return profit


        