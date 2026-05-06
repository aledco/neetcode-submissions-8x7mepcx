class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(s):
            if len(s) == 0:
                return False
            if len(s) == 1:
                return True
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(s, i, j, P, p):
            if j >= len(s):
                return [P]

            if i >= len(s):
                return []
            
            R = backtrack(s, i+1, j, P, p + s[i])
            if is_palindrome(p + s[i]):
                R += backtrack(s, i+1, i+1, P + [s[j:i+1]], "")
                
            return R
        
        return backtrack(s, 0, 0, [], "")