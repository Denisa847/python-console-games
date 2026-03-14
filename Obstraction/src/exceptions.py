#here are exceptions that are used in the game to handle errors

class BoardExceptions(Exception):#allows you to create specific exceptions
    def __init__(self, message):
        self.__message =message

    def __str__(self):
        return self.__message#returns a message string that was passed when the exception was called


class OutOfBoundsExceptions(BoardExceptions):#an error when a move is made outside the board
    def __init__(self):
        super().__init__("Position is out of bounds")#this message will be displayed to the user if it's needed


class CellBlockedException(BoardExceptions):#an error when the positon was already hit
    def __init__(self):
        super().__init__("Position was already hit. Try again")

class NoValidMovesException(Exception):#represents a situation when are no valid moves
    pass