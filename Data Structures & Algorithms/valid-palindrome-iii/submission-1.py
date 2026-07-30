class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        from functools import cache

        @cache
        def dfs(s, k, i, j):
            if i > j:
                return True
            
            if s[i] == s[j]:
                return dfs(s, k, i+1, j-1)
            else:
                if k == 0:
                    return False
                return (
                    dfs(s, k-1, i+1, j) or
                    dfs(s, k-1, i, j-1)
                )
        
        return dfs(s, k, 0, len(s)-1)

        # def dynamicProgramming(s, k):
            # dp[i] = p, the number of characters to remove so that s[:i+1] + s[n-i-1:] is a palindrome
            # s is a k palindrome if dp[n//2] <= k