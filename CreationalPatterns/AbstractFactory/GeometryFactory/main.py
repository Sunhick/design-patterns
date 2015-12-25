#!/usr/bin/python

import sys
from GeometryFactory import FactoryProducer


def main(*argv):
    shape_factory = FactoryProducer.get_factory('SHAPE')
    circle = shape_factory.get_shape('CIRCLE')
    circle.draw()
    rect = shape_factory.get_shape('RECTANGLE')
    rect.draw()

    color_factory = FactoryProducer.get_factory('COLOR')
    red = color_factory.get_color('RED')
    red.fill()
    blue = color_factory.get_color('GREEN')
    blue.fill()

if __name__ == '__main__':
    main(sys.argv)
