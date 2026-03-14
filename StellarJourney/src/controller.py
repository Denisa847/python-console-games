
class Controller:
    def __init__(self,board):
        self.board=board

    def path_has_star(self, start_row, start_col, end_row, end_col):
        dr = 0
        dc = 0

        if end_row > start_row:
            dr = 1
        elif end_row < start_row:
            dr = -1

        if end_col > start_col:
            dc = 1
        elif end_col < start_col:
            dc = -1

        r = start_row + dr
        c = start_col + dc

        while r != end_row or c != end_col:
            if self.board._board[r][c] == "*":
                return True
            r += dr
            c += dc

        if self.board._board[end_row][end_col] == "*":
            return True

        return False

    def valid_coord(self,row,col):
        if row < 0 or row >= self.board.size:
            raise ValueError("Invalid row")

        if col<0 or col>=self.board.size:
            raise ValueError("Invalid col")

        pos_row,pos_col=self.board.ship
        if not(row==pos_row or col==pos_col or abs(pos_row-row)==abs(pos_col-col)):
            raise ValueError("You can move only on row/col/diag")

        if self.path_has_star(pos_row, pos_col, row, col):
            raise ValueError("There is a star on the way!")

    def check_enemy(self,row,col):
        if self.board._board[row][col]=="B":
            return True
        return False

    def warp(self,row, col):
        self.valid_coord(row, col)
        if self.check_enemy(row, col):
            return False

        old_row, old_col = self.board.ship
        self.board._board[row][col] = "E"
        self.board.ship = (row, col)
        self.board._board[old_row][old_col] = " "
        return True

    def is_adj(self,x1,y1,x2,y2):
        return max(abs(x1-x2), abs(y1-y2))<=1

    def check_win(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board._board[i][j]=="B":
                    return False
        return True

    def fire(self,row,col):
        if row < 0 or row >= self.board.size:
            raise ValueError("Invalid row")

        if col < 0 or col >= self.board.size:
            raise ValueError("Invalid col")

        ship_row,ship_col=self.board.ship
        if not self.is_adj(ship_row,ship_col,row,col):
            raise ValueError("Not adj with Blingon!You can not fire!")

        if self.board._board[row][col]=="B":
            self.board._board[row][col]=" "
            if not self.check_win():
                self.board.reposition_blingons()

            return True

        return False



