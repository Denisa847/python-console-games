from board import ObstructionBoard
from exceptions import BoardExceptions,NoValidMovesException
from game import ComputerGame
from colorama import Fore,Style

class UI:
    def __init__(self):
        self.__board=ObstructionBoard()
        self.__computerPlayer=ComputerGame(self.__board)

    def __place_human_marker(self):
      while True:
        print("Your turn to place a mark")
        try:
            row = int(input("Row = "))
            column = int(input("Column = "))
            self.__board.place_marker(row, column, "X")
            break

        except ValueError:
            print("Please enter a valid number.")

        except BoardExceptions as b:
            print(b)

    def printBoards(self):
        """print(Fore.YELLOW)
        print("The computer's board")
        print(self.__computerBoard)
        print(Style.RESET_ALL)"""

        print(Fore.GREEN)
        print(self.__board)
        print(Style.RESET_ALL)

    def startGame(self):
        self.printBoards()
        humanTurn = True

        while True:
            if humanTurn:
                print("Human's turn")
                self.__place_human_marker()
                self.printBoards()

                if not self.__computerPlayer.has_valid_moves():
                    print("Computer has no valid moves left")
                    print("You won! :)")
                    break

                humanTurn = False

            else:
                print("Computer's turn")
                try:
                    row, col = self.__computerPlayer.make_moves("O")
                    print(f"Computer placed 'O' at ({row},{col})")
                    self.printBoards()

                    if not self.__board.has_valid_moves():
                        print("You have no valid moves left")
                        print("You lost! :(")
                        break

                    humanTurn = True

                except NoValidMovesException:
                    print("Computer has no valid moves left")
                    print("You won! :)")
                    break


