from board import Board
from controller import Controller
from ui import Ui

def main():
    board=Board()
    controller=Controller(board)
    ui=Ui(controller)
    ui.start()
main()