import unittest

from gameoflife.game import Point


class TestPoint(unittest.TestCase):

    def test_point_has_x_y_coordinates(self):
        point = Point(4, 5)
        self.assertEqual(point.x, 4)
        self.assertEqual(point.y, 5)

    def test_same_points_are_equal(self):
        p1 = Point(3, 4)
        p2 = Point(3, 4)
        assert p1 == p2
        self.assertEqual(p1, p2)

    def test_different_points_are_not_equal(self):
        p1 = Point(3, 4)
        p2 = Point(4, 4)
        assert p1 != p2
        self.assertNotEqual(p1, p2)

    def test_list_of_points_equal(self):
        points1 = [Point(3, 4), Point(6, 2)]
        points2 = [Point(3, 4), Point(6, 2)]
        self.assertListEqual(points1, points2)
