class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
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

        def backtrack(word, node, i):
            if i >= len(word):
                return node.is_inserted
            
            if word[i] == '.':
                for c, n in node.children.items():
                    if backtrack(word, n, i+1):
                        return True
            elif word[i] in node.children:
                return backtrack(word, node.children[word[i]], i+1)
            return False

        return backtrack(word, self.root, 0)

class TreeNode:
    def __init__(self, val=""):
        self.val = val
        self.children = {}
        self.is_inserted = False
        

        