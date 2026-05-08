class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for w in words:
            trie.insert(w)
        
        def coords(B, i, j):
            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                if 0 <= i+x < len(B) and 0 <= j+y < len(B[i]):
                    yield i+x, j+y
                 
        def search(B, i, j, n, V):
            if (i, j) in V:
                return set()
            V.add((i, j))

            F = set()
            if n.is_inserted:
                F.add(n.val)

            for x, y in coords(B, i, j):
                if B[x][y] in n.children:
                    F |= search(B, x, y, n.children[B[x][y]], V.copy())
            return F
        
        found = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie.root.children:
                    found |= search(board, i, j, trie.root.children[board[i][j]], set())
        return list(found)



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