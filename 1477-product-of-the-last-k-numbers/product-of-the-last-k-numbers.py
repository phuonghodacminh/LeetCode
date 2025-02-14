class ProductOfNumbers(object):

    def __init__(self):
        self.products = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.products) - 1 < k:
            return 0
        else:
            return self.products[-1] / self.products[-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)