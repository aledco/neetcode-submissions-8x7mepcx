class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber > 0:
            columnNumber -= 1
            letter = chr(ord('A') + (columnNumber % 26))
            title.append(letter)
            columnNumber //= 26
        return "".join(reversed(title)) 