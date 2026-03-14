import random

class Controller:
    def __init__(self,board):
        self.board=board

    def count_X(self):
        cnt=0
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board._board[i][j]=="X":
                    cnt+=1


        return cnt

    def count_O(self):
        cnt = 0
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board._board[i][j] == "O":
                    cnt += 1

        return cnt


    def find_winning_move(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board._board[i][j] == " ":
                    for piece in ["X", "O"]:
                        self.board._board[i][j] = piece
                        won = self.board.check_win(piece)
                        self.board._board[i][j] = " "
                        if won:
                            return i, j, piece
        return None


    def best_move_neigh(self,piece):
        best=-1
        best_pos=None
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board._board[i][j]==" ":
                    cnt=self.board.count_near(i,j,piece)
                    if cnt>best:
                        best=cnt
                        best_pos=(i,j)

        return best_pos

    def computer_place(self):
        pos = self.find_winning_move()
        if pos is not None:
            x, y, piece = pos
            self.board._board[x][y] = piece
            return self.board.check_win(piece)

        if self.count_O()>self.count_X():
            piece="O"
        elif self.count_O()<self.count_X():
            piece="X"
        else:
            piece=random.choice(["X","O"])

        pos=self.best_move_neigh(piece)
        if pos is not None:
            x,y=pos
            self.board._board[x][y]=piece
            if self.board.check_win(piece):
                return True
            return False

        while True:
            row=random.randint(0,self.board.size-1)
            col=random.randint(0,self.board.size-1)
            if self.board._board[row][col]==" ":
                self.board._board[row][col]=piece
                if self.board.check_win(piece):
                    return True
                return False



    def place_human_piece(self,row,col,piece):
        if row<0 or col<0 or row>= self.board.size or col>=self.board.size:
            raise ValueError("Out of bound")

        if self.board._board[row][col]==" ":
            self.board._board[row][col] = piece
        else:
            raise ValueError("This position is taken!")

        if self.board.check_win(piece):
            return True
        return False

    def chaos_winning(self):
        return self.board.is_full()
