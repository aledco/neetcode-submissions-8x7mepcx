class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])

        self.prefixes = [None] * self.m
        for i in range(self.m):
            row = [0] * (self.n + 1)
            for j, n in enumerate(matrix[i]):
                row[j+1] = row[j] + n
            self.prefixes[i] = row

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for i in range(row1, row2+1):
            s += self.sumRowRegion(i, col1, col2)
        return s

    def sumRowRegion(self, r, c1, c2):
        return self.prefixes[r][c2+1] - self.prefixes[r][c1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)