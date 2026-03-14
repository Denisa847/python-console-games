from src.board import Board, load_file
from src.snake import Play
from src.ui import Ui

def start():
     size, nr_apples=load_file("settings.txt")
     board=Board(size, nr_apples)
     services=Play(board)
     ui=Ui(services)
     ui.start()

start()
