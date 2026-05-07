class TreeNode:
    def __init__(self, val=""):
        self.val = val
        self.children = {}
        self.is_inserted = False
        

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        while i < len(word):
            curr.children[word[i]] = TreeNode(word[:i+1])
            curr = curr.children[word[i]]
            i += 1

        curr.is_inserted = True

    def search(self, word: str) -> bool:
        curr = self.root
        i = 0
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        return i >= len(word) and curr.is_inserted

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        i = 0
        while i < len(prefix) and prefix[i] in curr.children:
            curr = curr.children[prefix[i]]
            i += 1
        
        return i >= len(prefix)

        