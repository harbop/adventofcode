from unittest import TestCase
from adventofcode import Adventofcode
from data import Data

class TestAdventofcode(TestCase):
    # December 1st
    def test_sum(self):
        advent = Adventofcode()

        self.assertEqual(1, advent.data_sum(Data.test1))
        self.assertEqual(-1, advent.data_sum(Data.test2))
        self.assertEqual(2, advent.data_sum(Data.test3))
        self.assertEqual(3, advent.data_sum(Data.test4))

    # December 2nd
    def test_first_repeat(self):
        advent = Adventofcode()

        self.assertEqual(0, advent.first_repeat(Data.test1))
        self.assertEqual(10, advent.first_repeat(Data.test2))
        self.assertEqual(5, advent.first_repeat(Data.test3))
        self.assertEqual(14, advent.first_repeat(Data.test4))
