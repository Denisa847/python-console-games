import random
from texttable import Texttable

def load_file(filename):
    with open(filename,"r") as f:
        lines=f.read().strip().split()
        size = int(lines[0])
        nr_apples=int(lines[1])

    return size, nr_apples

class Board:
    def __init__(self,size,apples):
        self.__size=size
        self.__apples=apples
        self._board=[[" " for _ in range(self.__size)] for _ in range(self.__size)]
        self.snake=[]
        self.place_snake()
        self.place_apples()



    @property
    def size(self):
        return self.__size


    def place_snake(self):
        self.snake=[ (self.__size//2 - 1, self.__size//2),
                    (self.__size//2, self.__size//2),
                    (self.__size//2+1, self.__size//2)]

        self._board[self.__size//2-1][self.__size//2]="*"
        self._board[self.__size//2][self.__size//2]="+"
        self._board[self.__size//2+1][self.__size//2]="+"



    def place_apples(self):
        count=0
        while count<self.__apples:
            x=random.randint(0,self.__size-1)
            y=random.randint(0,self.__size-1)
            if self._board[x][y]==" ":
                if x>0 and self._board[x-1][y]=="a":
                    continue
                if x<self.__size-1 and self._board[x+1][y]=="a":
                    continue
                if y<self.__size-1 and self._board[x][y+1]=="a":
                    continue
                if y>0 and self._board[x][y-1]=="a":
                    continue

                self._board[x][y]="a"
                count+=1

    def place_apple(self):
        while True:
            x=random.randint(0,self.__size-1)
            y=random.randint(0,self.__size-1)
            if self._board[x][y]==" ":
                if x>0 and self._board[x-1][y]=="a":
                    continue
                if x<self.__size-1 and self._board[x+1][y]=="a":
                    continue
                if y>0 and self._board[x][y-1]=="a":
                    continue
                if y<self.__size-1 and self._board[x][y+1]=="a":
                    continue
                self._board[x][y]="a"
                return



    def __str__(self):
        table=Texttable()
        for i in range(self.size):
            table.add_row(self._board[i])


        return table.draw()

