class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber > 0:
            print(columnNumber, (columnNumber-1) % 26, chr(ord('A') + ((columnNumber-1) % 26)), columnNumber // 26)
            letter = chr(ord('A') + ((columnNumber-1) % 26))
            title.append(letter)
            columnNumber = (columnNumber - 1) // 26
        return "".join(reversed(title))