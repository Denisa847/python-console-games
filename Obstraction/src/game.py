from random import randint
from exceptions import BoardExceptions,NoValidMovesException,OutOfBoundsExceptions,CellBlockedException
from board import ObstructionBoard

class ComputerGame:
    def __init__(self, board):
        #given board
        self.__board=board

    def finding_winning_move(self, marker):
        for row in range(self.__board.size):
            for col in range(self.__board.size):
                if self.__board._board[row][col] == " ":
                    try:
                        blocked_cells = self.__board.simulate_place_marker(row, col, marker)
                        is_winning = not self.has_valid_moves()
                        self.__board.undo_simulation(row, col, blocked_cells)

                        if is_winning:
                            self.__board.place_marker(row, col, marker)
                            return row, col
                    except (OutOfBoundsExceptions, CellBlockedException):
                        continue
        return None

    def find_blocking_move(self,marker,opponent_marker):
        #finds a move that blocks the opponent from winning
        for row in range(self.__board.size):
            for col in range(self.__board.size):
              if self.__board._board[row][col]==" ":
                try:
                    blocked_cells=self.__board.simulate_place_marker(row,col,opponent_marker)
                    if not self.has_valid_moves():
                        self.__board.undo_simulation(row,col,blocked_cells)
                        self.__board.place_marker(row, col,marker)
                        return row,col

                    self.__board.undo_simulation(row,col,blocked_cells)
                except (OutOfBoundsExceptions, CellBlockedException):
                   continue
        return None

    def finding_random_move(self, marker):
        valid_moves = []
        for row in range(self.__board.size):
            for col in range(self.__board.size):
                if self.__board._board[row][col] == " ":
                    valid_moves.append((row, col))

        if not valid_moves:
            raise NoValidMovesException()

        row, col = valid_moves[randint(0, len(valid_moves) - 1)]
        self.__board.place_marker(row, col, marker)
        return row, col

    def make_moves(self,marker):
        #decides the best move for the computer
        opponent_marker="X" if marker=="O" else "O"
        move=self.finding_winning_move(marker)
        if move:
            return move
        move=self.find_blocking_move(marker,opponent_marker)
        if move:
            return move

        return self.finding_random_move(marker)

    def has_valid_moves(self):
        for row in range(self.__board.size):
            for col in range(self.__board.size):
                if self.__board._board[row][col] == " ":
                    return True
        return False