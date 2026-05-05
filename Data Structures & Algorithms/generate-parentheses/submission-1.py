class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(n, o, c, s):
            if o == c == n:
                return [s]
            
            R = []
            if o < n:
                R += backtrack(n, o+1, c, s + "(")
            if c < o:
                R += backtrack(n, o, c+1, s + ")")
            return R

        
        return backtrack(n, 0, 0, "")