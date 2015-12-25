#!/usr/bin/python

import sys
import unittest
from GeometryFactory import FactoryProducer, Shapes,\
    Colors, InvalidColorException, InvalidShapeException


class GeometryFactoryTest(unittest.TestCase):
    """
    Geometry abstract Factory tester
    """
    def setUp(self):
        self.shape_factory = FactoryProducer.get_factory('SHAPE')
        self.color_factory = FactoryProducer.get_factory('COLOR')

    def tearDown(self):
        pass

    def test_shape_factory(self):
        circle = self.shape_factory.get_shape('CIRCLE')
        self.assertEqual(isinstance(circle, Shapes.Circle), True,
                         'Not a circle object')

    def test_color_factory(self):
        red = self.color_factory.get_color('RED')
        self.assertEqual(isinstance(red, Colors.Red), True,
                         'Not a red color. Expected:Red Got:{0}'.
                         format(type(red).__name__))

    def test_color_factory_error(self):
        self.assertRaises(InvalidColorException,
                          self.color_factory.get_color, 'COLOR_XXX')

    def test_shape_factory_error(self):
        self.assertRaises(InvalidShapeException,
                          self.shape_factory.get_shape, 'SHAPE_XXX')


def main(*argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
