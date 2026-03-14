
import unittest
from board import Board

class TestStars(unittest.TestCase):
    def setUp(self):
        self.board=Board()

    def is_adj(self,x1,y1,x2,y2):
        return max(abs(x1-x2), abs(y1-y2))<=1

    def test_place_stars(self):
        #self.board.place_stars()
        cnt=0
        stars=[]
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board._board[i][j]=="*":
                    cnt+=1
                    stars.append((i,j))

        self.assertEqual(cnt,10)

        for i in range(len(stars)):
            x1,y1=stars[i]
            for j in range(i+1,len(stars)):
                x2,y2=stars[j]
                self.assertFalse(self.is_adj(x1,y1,x2,y2))




if __name__=="__main__":
    unittest.main()
