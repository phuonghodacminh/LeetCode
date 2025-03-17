class Trie(object):

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self
        for i in word:
            if i not in curr.children:
                curr.children[i] = Trie()
            curr = curr.children[i]
        curr.end = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)