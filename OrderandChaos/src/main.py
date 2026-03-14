from board import Board
from game import Controller

from ui import Ui

def main():
    board=Board()
    controller=Controller(board)
    ui=Ui(controller)
    ui.start()
main()