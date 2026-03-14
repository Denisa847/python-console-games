from texttable import Texttable

class Board:
    def __init__(self,size=6):
        self.__size=size
        self._board=[[" " for _ in range(self.__size)] for _ in range(self.__size)]


    @property
    def size(self):
        return self.__size

    def is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self._board[i][j]==" ":
                    return False
        return True

    def check_row(self,piece):
        for i in range(self.size):
            cnt=0
            for j in range(self.size):
                if self._board[i][j]==piece:
                    cnt+=1
                else:
                    cnt=0
                if cnt==5:
                    return True
        return False

    def check_col(self,piece):
        for j in range(self.size):
            cnt=0
            for i in range(self.size):
                if self._board[i][j]==piece:
                    cnt+=1
                else:
                    cnt=0
                if cnt==5:
                    return True
        return False

    def check_diag_1(self,piece):
        for i in range(self.size):
            for j in range(self.size):
                cnt=0
                x,y=i,j
                while x<self.size and y<self.size:
                    if self._board[x][y]==piece:
                        cnt+=1
                        if cnt==5:
                            return True
                    else:
                        cnt=0
                    x+=1
                    y+=1
        return False

    def check_diag_2(self,piece):
        for i in range(self.size):
            for j in range(self.size):
                x,y=i,j
                cnt=0
                while x<self.size and y>=0:
                    if self._board[x][y]==piece:
                        cnt+=1
                        if cnt==5:
                            return True
                    else:
                        cnt=0
                    x+=1
                    y-=1
        return False




    def check_win(self,piece):
        return self.check_col(piece) or self.check_row(piece) or self.check_diag_1(piece) or self.check_diag_2(piece)


    def count_near(self,row,col,piece):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        cnt=0
        for x,y in directions:
            dx,dy=x+row,y+col
            if 0<=dx<self.size and 0<=dy<self.size:
                if self._board[dx][dy]==piece:
                    cnt+=1
        return cnt

    def __str__(self):
        table=Texttable()
        header=[" "]+ [str(i) for i in range(self.size)]
        table.add_row(header)

        for i in range(self.size):
            row=[str(i)]+self._board[i]
            table.add_row(row)

        return table.draw()