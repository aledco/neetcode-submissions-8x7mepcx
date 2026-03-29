class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidCell(c):
            return c in [str(i) for i in range(10)]

        def check(row):
            S = set()
            for c in row:
                if c == '.':
                    continue
                if isValidCell(c):
                    if c in S:
                        return False
                    S.add(c)
                else:
                    return False
            return True
        
        def checkRows(B):
            for row in B:
                if not check(row):
                    return False
            return True
        
        def checkCols(B):
            T = []
            for i in range(9):
                C = []
                for j in range(9):
                    C.append(B[j][i]) 
                T.append(C)
            return checkRows(T)
        
        def checkSquares(B):
            T = []
            for p in range(0, 9, 3):
                for q in range(0, 9, 3):
                    S = []
                    for i in range(p, p+3):
                        for j in range(q, q+3):
                            S.append(B[i][j])
                    T.append(S)
            return checkRows(T)

        return checkRows(board) and checkCols(board) and checkSquares(board)