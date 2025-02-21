# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.node = set()
        self.initialize(root, 0)
    
    def initialize(self, root, value):
        root.val = value
        self.node.add(value)
        if root.left:
            self.initialize(root.left, 2 * value + 1)
        if root.right:
            self.initialize(root.right, 2 * value + 2)    

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.node


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)