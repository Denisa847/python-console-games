import unittest
from controller import Controller
from repo import Repo


class TestRepo(unittest.TestCase):
    def setUp(self):
        self.repo=Repo("s.txt")

    def test_load(self):
        expected = ["scramble", "dream without fear", "Brevity is beautiful", "Work hard dream big", "Be strong"]
        self.assertEqual(self.repo.sentence, expected)

    def test_get_sentance(self):
        s=self.repo.get_random_prop()
        self.assertTrue(s in self.repo.sentence)




if __name__=="__main__":
    unittest.main()


class Test(unittest.TestCase):
    def setUp(self):
        self.repo=Repo("s.txt")
        self.controller=Controller(self.repo)

    def test_scramble(self):
        sentence=self.controller.choose_prop()
        new_sentence=self.controller.scramble(sentence)
        self.assertNotEqual(sentence,new_sentence)

        sent="abcd"
        new=self.controller.scramble(sent)
        self.assertEqual(new[0],"a")
        self.assertEqual(new[-1], "d")

    def test_swaps(self):
        sent="abcde"
        result=self.controller.swap(sent,0,1,0,2)
        self.assertEqual(result, "acbde")

        with self.assertRaises(ValueError):
            self.controller.swap(sent,0,0,0,3)

        with self.assertRaises(ValueError):
            self.controller.swap(sent,5,0,0,1)

        with self.assertRaises(ValueError):
            self.controller.swap(sent,0,1,0,9)

        with self.assertRaises(ValueError):
            self.controller.swap(sent,0,1,0,4)
