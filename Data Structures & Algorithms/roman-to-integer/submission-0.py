class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = len(s)-1

        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        edges = {
            "I": "",
            "V": "I",
            "X": "I",
            "L": "X",
            "C": "X",
            "D": "C",
            "M": "C"
        }

        res = 0
        while i >= 0:
            res += values[s[i]]
            if i-1 >= 0 and edges[s[i]] == s[i-1]:
                res -= values[s[i-1]]
                i -= 2
            else:
                i -= 1
        return res
