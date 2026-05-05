class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def coords(board, i, j):
            for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if i+x < 0 or i+x >= len(board) or j+y < 0 or j+y >= len(board[i]):
                    continue
                yield (i+x, j+y)
            
        def search(board, i, j, word, w, V):
            if (i, j) in V:
                return False
            if board[i][j] != word[w]:
                return False
            if w+1 >= len(word):
                return True
            
            V.add((i, j))
            for x, y in coords(board, i, j):
                if search(board, x, y, word, w+1, V.copy()):
                    return True
            return False
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(board, i, j, word, 0, set()):
                    return True
        return False
