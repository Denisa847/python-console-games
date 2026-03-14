from src.domain.board import Board
from src.domain.exceptions import InvalidMoveError
from src.services.ai import ComputerStrategy
from src.domain.plane import Plane
import random

class GameService:
    def __init__(self,size=10):
        """
        Initialize a new game service
        """
        self._size=size
        self._player_board=Board(size)
        self._computer_board=Board(size)

        self._ai=ComputerStrategy()

    @property
    def player_board(self):
        """
        :return: Returns the player's board
        """
        return self._player_board

    @property
    def computer_board(self):
        """
        :return: Returns the computer's board
        """
        return self._computer_board

    @property
    def size(self):
        """
        :return: Returns board size
        """
        return self._size

    def add_player_plane(self,plane):
        """
        Add a plane to the player's board if is valid
        """
        self._player_board.add_plane(plane)

    def add_computer_plane(self,plane):
        """
         Add a plane to the computer's board if is valid
        """
        self._computer_board.add_plane(plane)

    def player_shoot(self,pos):
        """
        Process a player shot on the computer's borad, returns "hit","missed" or "destroyed"
        and riases an error if the shot is invalid
        """
        return self._computer_board.fire(pos)

    def computer_shoot(self):
        """
        Will ask ai to choose a move and apply it to the player's board
        :return:
        """
        pos=self._ai.choose_move(self._player_board)
        result=self._player_board.fire(pos)

        self._ai.update_after_shot(pos,result)

        return pos,result

    def player_won(self):
        """
        Check if the player destoryed all computer planes
        :return: Returns True if all computer planes are destroyed, False otherwise
        """
        return self._computer_board.all_planes_destroyed()

    def computer_won(self):
        """
        Check if computer destroyed all player planes
        :return: True if the planes are destroyed, False otherwise
        """
        return self._player_board.all_planes_destroyed()

    def is_game_over(self):
        """
        Check if either player won the game
        :return: True if the game is over, False otherwise
        """
        return self.player_won() or self.computer_won()

    def place_random_plane(self,board):
        """Generate and add a random 3-cell plane to the given board. Tries until a valid placement is found.
           Planes can be horizontal or vertical.  """
        size=board.size
        while True:
            orientation=random.choice(["horizontal","vertical"])
            if orientation=="horizontal":
                row=random.randint(0,size-1)
                col=random.randint(0,size-3)
                cells={(row,col),(row,col+1),(row,col+2)}
            else:
                row=random.randint(0,size-3)
                col=random.randint(0,size-1)
                cells={(row,col),(row+1,col), (row+2,col)}

            plane=Plane(cells)
            try:
                board.add_plane(plane)
                return plane
            except InvalidMoveError:
                continue
