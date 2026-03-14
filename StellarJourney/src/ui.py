
class Ui:
    def __init__(self,controller):
        self.__controller=controller

    def display_board(self):
        print(self.__controller.board)

    def cheat_board(self):
        print(self.__controller.board.cheat_board())

    def menu(self):
        print("warp <coordinate>")
        print("fire <coordinate>")
        print("cheat")

    def get_coord(self, coord):
        coord = coord.strip().upper()
        try:
            row=ord(coord[0])-65
            col=int(coord[1:])-1

        except ValueError:
            print("Invalid coordinates")
            return

        return row,col

    def ui_warp(self, coord):
        pos = self.get_coord(coord)
        if not pos:
            return
        row, col = pos

        try:
            continuePlay = self.__controller.warp(row, col)
        except ValueError as e:
            print(e)
            return

        if continuePlay == False:
            print("You landed on emey!Game over!")
            return False

        return True

    def ui_fire(self,coord):
        pos = self.get_coord(coord)
        if not pos:
            return
        row, col = pos

        try:
            destr=self.__controller.fire(row,col)
        except ValueError as e:
            print(e)
            return

        if destr==True:
            print("The Blingon ship was destroyed!")
        else:
            print("Missed!")

    def start(self):
        while True:
            if self.__controller.check_win():
                print("You won!")
                return
            self.display_board()
            self.menu()
            cmd = input("Command: ").strip().split()
            if not cmd:
                continue

            if cmd[0] == "cheat":
                self.cheat_board()
                print("\n\n")

            elif cmd[0] == "warp":
                if len(cmd) != 2:
                    print("Command must have len 2")
                    continue
                result = self.ui_warp(cmd[1])
                if result == False:
                    return

            elif cmd[0]=="fire":
                if len(cmd)!=2:
                    print("Command must have len 2")
                    continue
                self.ui_fire(cmd[1])
            else:
                print("Invalid command")
