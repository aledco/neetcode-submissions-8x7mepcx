class Solution:
    def totalNQueens(self, n: int) -> int:
        return len(
            self.solveNQueens(n)
        )

    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(B, j):
            # look for queen straght up
            for i in range(len(B) - 1, -1, -1):
                if B[i][j] == 'Q':
                    return False
            
            # look for queen left up
            k = j-1
            for i in range(len(B) - 1, -1, -1):
                if k < 0:
                    break
                if B[i][k] == 'Q':
                    return False
                k -= 1
            
            # look for queen right up
            k = j+1
            for i in range(len(B) - 1, -1, -1):
                if k >= len(B[i]):
                    break
                if B[i][k] == 'Q':
                    return False
                k += 1

            return True

        def backtrack(n, i, B):
            if i >= n:
                return [B]
            
            R = []
            row = ['.'] * n
            for j in range(n):
                if is_valid(B, j):
                    row[j] = 'Q'
                    R += backtrack(n, i+1, B.copy() + ["".join(row)])
                    row[j] = '.'
            return R
        
        return backtrack(n, 0, [])