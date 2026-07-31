from collections import defaultdict

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.player_rows = {1: defaultdict(int), 2: defaultdict(int)}
        self.player_cols = {1: defaultdict(int), 2: defaultdict(int)}
        self.player_diags = {1: defaultdict(int), 2: defaultdict(int)}

    def move(self, row: int, col: int, player: int) -> int:
        self.player_rows[player][row] += 1
        if self.player_rows[player][row] == self.n:
            return player
        
        self.player_cols[player][col] += 1
        if self.player_cols[player][col] == self.n:
            return player
        
        if row == col:
            self.player_diags[player][1] += 1
            if self.player_diags[player][1] == self.n:
                return player
        
        if row == self.n-col-1:
            self.player_diags[player][-1] += 1
            if self.player_diags[player][-1] == self.n:
                return player
            
        return 0

[1, 1, 2]
[0, 2, 0]
[2, 0, 1]

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
