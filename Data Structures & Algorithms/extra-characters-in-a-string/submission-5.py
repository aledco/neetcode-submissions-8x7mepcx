class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        def dfs(s, T, i=0):
            if i >= len(s):
                return 0
            
            res = 1 + dfs(s, T, i+1) # do not use character i
            for w in T.find_all(s, i): # try each macthing word
                res = min(
                    res,
                    dfs(s, T, i+len(w))
                )
            return res

        # return dfs(s, Trie(dictionary))

        def dynamicProgramming_topDown(s, T):
            cache = {}

            def dfs(s, T, i=0):
                nonlocal cache

                if i in cache:
                    return cache[i]
                
                if i >= len(s):
                    return 0
                
                cache[i] = 1 + dfs(s, T, i+1) # do not use character i
                for w in T.find_all(s, i): # try each macthing word
                     cache[i] = min(
                         cache[i],
                        dfs(s, T, i+len(w))
                    )
                return cache[i]
            
            return dfs(s, T)
            
        # return dynamicProgramming_topDown(s, Trie(dictionary))

        def dynamicProgramming_bottomUp(s, T):
            # dp[i] = min characters left at position i

            dp = [0] * (len(s) + 1)
            for i in range(len(s)-1, -1, -1):
                dp[i] = 1 + dp[i+1] # do not use character i
                for w in T.find_all(s, i):
                    dp[i] = min(dp[i], dp[i+len(w)])
            return dp[0]
        
        return dynamicProgramming_bottomUp(s, Trie(dictionary))



class Trie:
    def __init__(self, words):
        self.root = TrieNode("")
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
    def __init__(self, word, is_word=False):
        self.word = word
        self.is_word = is_word
        self.children = {}
