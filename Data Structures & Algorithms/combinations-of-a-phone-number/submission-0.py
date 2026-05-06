class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(D, M, i, s):
            if i >= len(D):
                if s == "":
                    return []
                return [s]
            
            R = []
            for c in M[D[i]]:
                R += backtrack(D, M, i+1, s + c)
            return R
        
        return backtrack(digits, digit_map, 0, "")