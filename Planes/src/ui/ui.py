from texttable import Texttable
from src.domain.exceptions import InvalidMoveError
from src.domain.plane import Plane
from src.services.game_service import GameService

class ConsoleUi:
    def __init__(self,size=0):
        self.service=GameService(size)
        self.cheat_mode = False

    def print_board(self,board, show_planes=False):
        grid=board.get_visible_grid(show_planes)

        table=Texttable()
        header=[" "] + [str(i) for i in range(board.size)]
        table.header(header)

        for row_idx in range(board.size):
            row=[str(row_idx)]+grid[row_idx]
            table.add_row(row)

        print(table.draw())


    def print_cheat_board(self,board):
        print("\n**** CHEAT BOARD ****")
        self.print_board(board,show_planes=True)

    def read_position(self):
        while True:
            try:
                text=input("Enter coordinates (row col): ").strip()
                r,c=text.split()
                r,c=int(r), int(c)
                if not (0<=r<self.service.size and 0<=c<self.service.size):
                    print(f"Coodinates must be between 0 and {self.service.size-1}")
                    continue
                return (r,c)
            except ValueError:
                print("Invalid input")

    def run(self):
        for _ in range(3):
            player_plane = self.service.place_random_plane(self.service.player_board)
            computer_plane = self.service.place_random_plane(self.service.computer_board)

        cheat = input("Do you want to enable cheat mode? (y/n): ").strip().lower()
        if cheat == "y":
            self.cheat_mode = True
        else:
            self.cheat_mode = False



        while True:
            print("\nYour turn: ")
            print("\nComputer board(your shots): ")
            if self.cheat_mode:
                print("\nCHEAT BOARD:")
                self.print_board(self.service.computer_board, show_planes=True)
            else:
                self.print_board(self.service.computer_board, show_planes=False)

            pos=self.read_position()

            try:
                result=self.service.player_shoot(pos)
                print(f"You shot {pos}-> {result}")
            except InvalidMoveError as e:
                print(f"{e}! Try again!")
                continue

            if self.service.player_won():
                print("\n\nYOU WON! \n")
                break

            print("Computer's turn ")
            pos,result=self.service.computer_shoot()
            print(f"Computer shot {pos}-> {result}")

            print("\nYour board(computer shots): ")
            self.print_board(self.service.player_board, show_planes=True)

            if self.service.computer_won():
                print("GAME OVER! YOU LOST!")
                break


