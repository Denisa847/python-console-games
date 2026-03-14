
class Ui:
    def __init__(self,controller):
        self.__controller=controller

    def print_board(self):
        print(self.__controller.board)

    def user_input(self):
        piece = input("Piece(X/O): ").upper()
        if piece not in ["X", "O"]:
            print("Invalid piece")
            return
        row = input("Row: ")
        try:
            row = int(row)
        except ValueError:
            print("Invalid row")
            return

        col = input("Col: ")
        try:
            col = int(col)
        except ValueError:
            print("Invalid col")
            return

        return piece,row,col


    def start(self):
        while True:
            self.print_board()
            result=self.user_input()
            if result is None:
                continue

            piece, row, col=result
            try:
                win=self.__controller.place_human_piece(row,col,piece)
            except ValueError as e:
                print(e)
                continue

            if win:
                self.print_board()
                print("Order wins! Game over")
                return

            win=self.__controller.computer_place()
            if win:
                self.print_board()
                print("Order wins! Game over")
                return

            if self.__controller.chaos_winning():
                self.print_board()
                print("Chaos won!")
                return

