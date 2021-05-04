import unittest

from gameoflife import __version__
from gameoflife.game import GameOfLife, Point


def test_version():
    assert __version__ == '0.1.0'


class GameOfLifeTest(unittest.TestCase):

    def test_given_single_living_cell_when_generation_dies_of_under_population(self):
        game = GameOfLife.load("*")
        nextGeneration = game.getNextGeneration()
        self.assertEqual(str(nextGeneration), ".")

    def test_given_two_by_two_grid_Lives_next_generation_due_to_two_neighbours(self):
        game = GameOfLife.load("* *\n"
                               "* *")
        nextGeneration = game.getNextGeneration()
        self.assertEqual(str(nextGeneration), "* *\n"
                                              "* *")

    def test_load_game_from_string(self):
        game = GameOfLife.load("* . * .\n"
                               ". * . .\n"
                               ". . * *")
        self.assertEqual(3, game.rows)
        self.assertEqual(4, game.columns)
        self.assertListEqual([Point(0, 0), Point(2, 0), Point(1, 1), Point(2, 2), Point(3, 2)], game.livingCells)
