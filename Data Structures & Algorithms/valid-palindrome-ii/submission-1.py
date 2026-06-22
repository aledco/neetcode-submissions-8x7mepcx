class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(s, can_delete):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                elif can_delete:
                    return (
                        isPalindrome(s[:i] + s[i+1:], False) or
                        isPalindrome(s[:j] + s[j+1:], False)
                    )
                else:
                    return False
            return True

        return isPalindrome(s, True)