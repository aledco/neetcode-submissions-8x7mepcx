from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        @cache
        def dfs(s, T, i=0):
            if i >= len(s):
                return [[]]
            
            res = []
            for w in T.find_all(s, i):
                for sub in dfs(s, T, i+len(w)):
                    res.append([w] + sub)
            return res
            
        return [" ".join(x) for x in dfs(s, Trie(wordDict))]

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self._build(words)

    def find_all(self, s, i=0):
        curr = self.root
        while i < len(s) and s[i] in curr.children:
            curr = curr.children[s[i]]
            if curr.is_word:
                yield curr.word
            i += 1
        
    def _build(self, words):
        for w in words:
            curr_node = self.root
            curr_word = ""
            for c in w:
                curr_word += c
                if c not in curr_node.children:
                    curr_node.children[c] = TrieNode(curr_word)
                curr_node = curr_node.children[c]
            curr_node.is_word = True

class TrieNode:
    def __init__(self, word="", is_word=False):
        self.word = word
        self.is_word = is_word
        self.children = {}