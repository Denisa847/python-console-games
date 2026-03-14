from texttable import Texttable
import random

class Board:
    def __init__(self,size=8):
        self.__size=size
        self._board=[[" " for _ in range(self.__size)] for _ in range(self.__size)]
        self.ship = None
        self.place_stars()
        self.place_ship()
        self.place_Blingon()


    @property
    def size(self):
        return self.__size

    def place_ship(self):
        while True:
            row = random.randint(0, self.__size - 1)
            col = random.randint(0, self.__size - 1)
            if self._board[row][col] == " ":
                self._board[row][col] = "E"
                self.ship = (row, col)
                return

    def place_Blingon(self):
        cnt=0
        while cnt<3:
            row = random.randint(0, self.__size - 1)
            col = random.randint(0, self.__size - 1)
            if self._board[row][col] == " ":
                self._board[row][col] = "B"
                cnt+=1




    def check_adj(self,row,col):
        """
        helper function to check what we have on col,row,and diag if ther eis anothe rdstar will return True
        :param row: the numbe rof row
        :param col: the number of the col
        :return: True if there are stars around the given row and col
        """
        directions=[(-1,-1),(-1,0),(-1,1),
                   (0,-1),(0,1),
                   (1,-1),(1,0),(1,1)]


        for x,y in directions:
            dx,dy=x+row,y+col
            if 0<=dx<self.size and 0<=dy<self.size:
                if self._board[dx][dy]=="*":
                    return True
        return False

    def place_stars(self):
        """ This function takes a cnt to check when we have 10 stars and will use the random function
        to generate random positions(row and col). Then will check if the row and col are empty if they are we will call a
        helper function to check what we have on col,row,and diagonal if there is another star will return True and
        the star will not be placed and will try to find other positions"""
        cnt=0
        while cnt<10:
            row=random.randint(0,self.__size-1)
            col=random.randint(0,self.__size-1)
            if self._board[row][col]==" ":
                if self.check_adj(row,col):
                    continue
                self._board[row][col]="*"
                cnt+=1

    def reposition_blingons(self):
        """
        Repositions all remaining Blingon ships randomly on empty cells.
        """
        remaining = 0
        for i in range(self.__size):
            for j in range(self.__size):
                if self._board[i][j] == "B":
                    remaining += 1
                    self._board[i][j] = " "

        placed = 0
        while placed < remaining:
            row = random.randint(0, self.__size - 1)
            col = random.randint(0, self.__size - 1)

            if self._board[row][col] == " ":
                self._board[row][col] = "B"
                placed += 1

    def get_visible_board(self):
        visible = [[" " for _ in range(self.size)] for _ in range(self.size)]

        for i in range(self.size):
            for j in range(self.size):
                if self._board[i][j] == "*":
                    visible[i][j] = "*"
                elif self._board[i][j] == "E":
                    visible[i][j] = "E"
                    for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        dx, dy = x + i, y + j
                        if 0 <= dx < self.__size and 0 <= dy < self.__size:
                            if self._board[dx][dy] == "B":
                                visible[dx][dy] = "B"

        return visible

    def cheat_board(self):
        table = Texttable()
        header = ["0"] + [str(i + 1) for i in range(self.size)]
        table.header(header)

        for i in range(self.size):
            row = [chr(i + 65)] + self._board[i]
            table.add_row(row)

        return table.draw()


    def __str__(self):
        table=Texttable()
        head=["0"] + [str(i+1) for i in range(self.size)]
        table.header(head)
        board=self.get_visible_board()

        for i in range(self.size):
            row=[chr(i+65)] +board[i]
            table.add_row(row)

        return table.draw()
