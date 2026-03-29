class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                l = s[i].lower()
                r = s[j].lower()
                if l != r:
                    return False
                i += 1
                j -= 1
        return True