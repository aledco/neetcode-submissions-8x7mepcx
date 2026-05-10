class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(B, i, j, V):
            if i < 0 or i >= len(B) or j < 0 or j >= len(B[i]):
                return False
            
            if B[i][j] == "X":
                return True
            if (i, j) in V:
                return True
            
            V.add((i, j))
            return (
                dfs(B, i+1, j, V) and
                dfs(B, i-1, j, V) and
                dfs(B, i, j+1, V) and
                dfs(B, i, j-1, V)
            )
        
        def fill(B, F):
            for i, j in F:
                B[i][j] = "X"
            
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i, j) not in visited:
                    o = set()
                    if dfs(board, i, j, o):
                        fill(board, o)
                    visited |= o


