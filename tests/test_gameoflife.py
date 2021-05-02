import unittest

from gameoflife import __version__
from gameoflife.game import get_next_generation


def test_version():
    assert __version__ == '0.1.0'


class GameOfLifeTest(unittest.TestCase):

    def test_given_single_living_cell_when_generation_dies_of_under_population(self):
        current_generation = '*'
        next_generation = get_next_generation(current_generation)
        self.assertEqual(next_generation, '.')
