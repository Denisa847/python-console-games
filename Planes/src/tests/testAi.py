import unittest
import random

from src.domain.board import Board
from src.domain.plane import Plane
from src.domain.exceptions import InvalidMoveError
from src.services.ai import ComputerStrategy

class TestComputerStrategy(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        self.board=Board(size=6)
        self.ai=ComputerStrategy()

    def test_random_move_on_empty_board(self):
        pos=self.ai.choose_move(self.board)
        r,c=pos
        self.assertTrue(0<=r<self.board.size)
        self.assertTrue(0 <= c < self.board.size)
        self.assertNotIn(pos,self.board._shots)

    def test_ai_targets_after_hit(self):
        plane=Plane({(2,2),(2,3)})
        self.board.add_plane(plane)
        self.board.fire((2,2))
        self.ai.update_after_shot((2,2),"hit")

        pos=self.ai.choose_move(self.board)
        r,c=pos

        neighbors={(1,2),(3,2),(2,1),(2,3)}
        self.assertIn((r,c),neighbors)
        self.assertNotIn((r,c),self.board._shots)

    def test_ai_does_not_repeat_shot(self):
        self.board._shots.add((0,0))
        for _ in range(10):
            pos=self.ai.choose_move(self.board)
            self.assertNotEqual(pos,(0,0))




if __name__=="__main__":
    unittest.main()