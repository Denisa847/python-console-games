from board import Board
from unittest import TestCase
from game import Controller

class TestBoard(TestCase):
    def setUp(self):
        self.board=Board()

    def testrow(self):
        for c in range(1,6):
            self.board._board[1][c]="X"

        self.assertTrue(self.board.check_win("X"))
        self.assertFalse(self.board.check_win("O"))

    def testcol(self):
        for i in range(1,6):
            self.board._board[i][0]="O"

        self.assertTrue(self.board.check_win("O"))
        self.assertFalse(self.board.check_win("X"))

    def test_diag(self):
        for i in range(1,6):
            self.board._board[i][i] = "X"

        self.assertTrue(self.board.check_win("X"))

    def test_other_diag(self):
        for i in range(1,6):
            self.board._board[i][6-i] = "O"
        self.assertTrue(self.board.check_win("O"))
