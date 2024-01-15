import unittest

from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    This is a test discovery for Rectangle
    class Methods.
    """

    def testInitialization(self):
        """
        The test initialization checks if all
        arguments are there and if the positioning
        is correctly
        """

        rect = Rectangle(6, 8, 5, 4, 1)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 1)

    def testSetValue_width(self):
        """Testing width value requirement"""
        rect = Rectangle(5, 9, 2, 1, 5)

        """setting a positive value"""
        self.assertEqual(rect.width, 5)

        """setting a negative value"""
        with self.assertRaises(ValueError):
            rect.width = -6

        """Testing a non integer value"""
        with self.assertRaises(TypeError):
            rect.width("width")

    def testSetValue_height(self):
        """Testing width value requirement"""
        rect = Rectangle(5, 9, 2, 1, 5)

        """setting height to a positive value"""
        self.assertEqual(rect.height, 9)

        """setting height to a negative value"""
        with self.assertRaises(ValueError):
            rect.height = -7

        """Testing a non integer value"""
        with self.assertRaises(TypeError):
            rect.width("height")

    def testSetter_y(self):
        """Testing x value"""
        rect = Rectangle(5, 9, 2, 1, 5)

        """setting y to a negative value"""
        with self.assertRaises(ValueError):
            rect.y = -8

        """Testing y as a non integer"""
        with self.assertRaises(TypeError):
            rect.y("y_value")

    def testSetter_y(self):
        """Testing y value"""
        rect = Rectangle(5, 9, 2, 1, 5)

        """setting x to a negative value"""
        with self.assertRaises(ValueError):
            rect.x = -9

        """Testing x as a non integer"""
        with self.assertRaises(TypeError):
            rect.x("x_value")


if __name__ == '__main__':
    unittest.main()
