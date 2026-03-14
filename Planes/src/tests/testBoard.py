import unittest
from src.domain.board import Board
from src.domain.plane import Plane
from src.domain.exceptions import InvalidMoveError


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board=Board(size=10)

    def test_add_plane(self):
        plane=Plane({(1,1),(1,2),(1,3)})
        self.board.add_plane(plane)
        self.assertEqual(len(self.board._planes),1)

        plane = Plane({(9, 9), (9, 10), (9, 11)})
        with self.assertRaises(InvalidMoveError):
            self.board.add_plane(plane)

        p1= Plane({(1, 2), (1, 3), (1, 4)})
        with self.assertRaises(InvalidMoveError):
            self.board.add_plane(p1)


    def fire(self):
        plane=Plane({(2,2),(2,3)})
        self.board.add_plane(plane)
        result=self._borad.fire((0,0))
        self.assertEqual(result,"miss")

        result1=self._borad.fire((2,2))
        self.assertEqual(result1, "hit")

        result2= self._borad.fire((2, 3))
        self.assertEqual(result1, "destroyed")
        self.assertTrue(self._board.all_planes_destroyed())


if __name__=="__main__":
    unittest.main()