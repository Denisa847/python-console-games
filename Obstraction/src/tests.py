import unittest
from random import randint
from board import ObstructionBoard
from game import ComputerGame
from exceptions import BoardExceptions,NoValidMovesException,OutOfBoundsExceptions,CellBlockedException

class Test(unittest.TestCase):
    def setUp(self):
        self.board=ObstructionBoard(size=4)
        self.computer_game=ComputerGame(self.board)

    def test_valid_moves_available(self):
        self.assertTrue(self.computer_game.has_valid_moves())

    def test_finding_winning_moves(self):
        self.board.place_marker(0, 0, "X")
        self.board.place_marker(0, 3,"O")
        self.board.place_marker(3, 3, "X")

        move = self.computer_game.finding_winning_move("O")
        self.assertIsNotNone(move)

        row, col = move
        self.assertEqual(self.board._board[row][col], "O")


    def test_finding_random_moves(self):
        self.board.place_marker(0, 0, "X")
        self.board.place_marker(3, 3, "X")
        self.assertTrue(self.board.has_valid_moves())

        move=self.computer_game.finding_random_move("O")
        row, col=move
        self.assertEqual(self.board._board[row][col],"O")

    def test_make_moves_winning(self):
        self.board.place_marker(0, 0, "X")
        self.board.place_marker(1, 2, "X")
        self.board.place_marker(3, 1, "O")
        move = self.computer_game.make_moves('O')
        row, col = move
        self.assertEqual(self.board._board[row][col],'O')

    def test_blocking_move(self):
        self.board.place_marker(0, 0, "X")
        self.board.place_marker(2, 1, "O")
        self.board.place_marker(1, 3, "X")

        move = self.computer_game.find_blocking_move("O","X")
        row,col=move
        self.assertEqual((row,col),(3,3))




if __name__=="__main__":
    unittest.main()