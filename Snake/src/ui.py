from texttable import Texttable
from src.snake import Play

class Ui:
    def __init__(self,services):
        self.__services=services

    def print_board(self):
        print(self.__services.get_board())

    def menu(self):
        print("Commands:")
        print("  move [n]           - move the snake n steps (default = 1)")
        print("  left/right/up/down - change direction")

    def start(self):
        while True:
            self.print_board()
            self.menu()
            command=input("Your command: ").strip().split()
            if not command:
                continue

            if command[0]=="move":
                if len(command)==1:
                    alive=self.__services.move_steps()
                else:
                    try:
                        n=int(command[1])
                        alive=self.__services.move_steps(n)
                    except ValueError:
                        print("n must be int")
                        continue

                if not alive:
                    print("You lost!")
                    return


            elif command[0] in ["left", "right", "down", "up"]:
                 change=self.__services.change_direction(command[0])
                 if change==False:
                     print("You can not move 180 degrees")
                 else:
                     print("Direction changed!")
            else:
                print("Invalid command")
