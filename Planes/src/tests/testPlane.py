import unittest
from src.domain.board import Board
from src.domain.plane import Plane
from src.domain.exceptions import InvalidMoveError


class TestPlane(unittest.TestCase):
    def test_hit(self):
        plane=Plane({(1,1),(1,2)})
        self.assertFalse(plane.hit((0, 0)))
        self.assertTrue(plane.hit((1,1)))
        self.assertTrue(plane.hit((1,2)))
        self.assertTrue(plane.is_destroyed())



if __name__=="__main__":
    unittest.main()