import unittest
from team_states import *

class TestWinner(unittest.TestCase):

    def test_team1_wins(self):
        self.assertEqual(Teams(11, 9).winner(), 1)
        self.assertEqual(Teams(15, 13).winner(), 1)
        x = Teams(11,9)
        print(type(x))
    def test_team2_wins(self):
        self.assertEqual(Team2Server1(9, 11).winner(), 2)
        self.assertEqual(Team2Server2(14, 16).winner(), 1)
    x = Teams(11, 8)
    print(type(x),x.__class__.__mro__)
    def test_no_winner(self): 
        self.assertEqual(Team1Server1(10, 10).winner(), 0)
        self.assertEqual(Team2Server2(11, 10).winner(), 1)
        self.assertEqual(Team1Server2(12, 11).winner(), 0)

if __name__ == "__main__":
    unittest.main()