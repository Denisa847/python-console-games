import unittest
from src.domain.board import Board
from src.domain.plane import Plane
from src.domain.exceptions import InvalidMoveError
from src.services.game_service import GameService


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.service=GameService(size=10)

    def test_add_player_and_computer_plane(self):
        p1=Plane({(1,1),(1,2),(1,3)})
        p2=Plane({(3,3),(3,4),(3,5)})
        self.service.add_player_plane(p1)
        self.service.add_computer_plane(p2)
        self.assertEqual(len(self.service.player_board._planes), 1)
        self.assertEqual(len(self.service.computer_board._planes),1)

    def test_player_shoot(self):
        plane1 = Plane({(1, 1), (1, 2)})
        self.service.add_computer_plane(plane1)

        self.service.player_shoot((1,1))
        self.service.player_shoot((1,2))

        self.assertTrue(self.service.player_won())
        self.assertTrue(self.service.is_game_over())

    def test_player_shoot(self):
        plane2 = Plane({(2, 3), (2, 4), (2, 5)})
        self.service.add_player_plane(plane2)

        pos,result=self.service.computer_shoot()
        r,c =pos
        self.assertTrue(0<=r<self.service.size)
        self.assertTrue(0<=c<self.service.size)

    def test_place_random_planes(self):
        board=self.service.player_board
        self.service.place_random_plane(board)
        self.assertGreaterEqual(len(board._planes),1)


if __name__ == "__main__":
    unittest.main()