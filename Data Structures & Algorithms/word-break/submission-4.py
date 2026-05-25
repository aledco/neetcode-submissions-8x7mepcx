class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def hashSet(s, W): # O(n^3)
            W = set(W)
            I = []
            for j in range(len(s)):
                if s[0:j+1] in W:
                    I.append(j)
                else:
                    for i in I:
                        if s[i+1:j+1] in W:
                            I.append(j)
                            break
            return len(I) > 0 and I[-1] == len(s)-1
        
        # return hashSet(s, wordDict)

        def dfs(s, W, i=0):
            if i >= len(s):
                return True
            
            for w in W:
                if i+len(w) > len(s):
                    continue
                if s[i:i+len(w)] == w:
                    if dfs(s, W, i+len(w)):
                        return True
            return False
            
        # return dfs(s, wordDict)

        def dynamicProgramming(s, W):
            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(len(s)):
                for w in W:
                    j = i - len(w) + 1
                    if j >= 0 and s[j:i+1] == w and dp[j]:
                        dp[i+1] = True
                        break
            return dp[-1]
        
        # return dynamicProgramming(s, wordDict)

        def dynamicProgramming_trie(s, W):
            T = Trie(W)

            t = max(map(len, W))

            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(len(s)):
                for j in range(max(i-t+1, 0), i+1):
                    if T.search(s, j, i+1):
                        if dp[j]:
                            dp[i+1] = True
                            break
            return dp[-1]
        
        return dynamicProgramming_trie(s, wordDict)


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            self.insert(w)
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, s, i, j):
        node = self.root
        for k in range(i, j):  
            if s[k] not in node.children:
                return False
            node = node.children[s[k]]
        return node.is_word
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


