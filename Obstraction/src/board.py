
from texttable import Texttable
from exceptions import BoardExceptions,NoValidMovesException,OutOfBoundsExceptions,CellBlockedException

class ObstructionBoard:
    def __init__(self,size=6):
        #the dimension of the board will be 6x6
        self.__size=size
        self._board=[[' ' for _ in range(self.__size)] for _ in range(self.__size)]

    @property
    def size(self):
        return self.__size

    def place_marker(self,row,col,marker):
        #this function it will handle placing a player's marker and blocks nearby cells
        if not (0<= row <self.__size and 0<= col <self.__size):
            raise OutOfBoundsExceptions()

        if self._board[row][col]!=" ":
            raise CellBlockedException()

        self._board[row][col]=marker
        for i in range(max(0,row-1),min(self.__size,row+2)):
            for j in range(max(0,col-1),min(self.__size,col+2)):
                if self._board[i][j]==" ":
                    self._board[i][j]="-"

    def simulate_place_marker(self,row,col,marker):
        #simulates placing a mark on the board without changing anything
        blocked_cells=[]
        if not (0<= row <self.__size and 0<= col <self.__size):
            raise OutOfBoundsExceptions()

        if self._board[row][col]!=" ":
            raise CellBlockedException()

        self._board[row][col]=marker
        for i in range(max(0,row-1),min(self.__size,row+2)):
            for j in range(max(0,col-1),min(self.__size,col+2)):
                if self._board[i][j]==" ":
                    self._board[i][j]="-"
                    blocked_cells.append((i,j))

        return blocked_cells

    def undo_simulation(self,row,col,blocked_cells):
        #undo the simulation
        self._board[row][col]=" "
        for i,j in blocked_cells:
            if self._board[i][j]=="-":
               self._board[i][j]=" "


    def has_valid_moves(self):
        for row in range(self.__size):
            for col in range(self.__size):
                if self._board[row][col] == " ":
                    return True
        return False

    def __str__(self):
        #converts the board into a readable string format for display
        table=Texttable()
        header=[' '] + [str(i) for i in range(self.size)]#creates header row of the table
        table.header(header)

        for i in range(self.size):
            row = [str(i)] + self._board[i]
            table.add_row(row)

        return table.draw()

