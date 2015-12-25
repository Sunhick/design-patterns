#!/usr/bin/python

import Colors
import Shapes
from abc import ABCMeta, abstractmethod


class AbstractFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_color(self, color):
        pass

    @abstractmethod
    def get_shape(self, shape):
        pass


class ShapeFactory(AbstractFactory):
    def get_color(self, color):
        raise 'Use color factory'

    def get_shape(self, shape):
        shape = shape.lower()
        if shape == 'circle':
            return Shapes.Circle()
        elif shape == 'rectangle':
            return Shapes.Rectangle()
        elif shape == 'square':
            return Shapes.Square()
        else:
            raise InvalidShapeException('unknown shape: {0}'.format(shape))


class ColorFactory(AbstractFactory):
    def get_color(self, color):
        color = color.lower()
        if color == 'red':
            return Colors.Red()
        elif color == 'green':
            return Colors.Green()
        elif color == 'blue':
            return Colors.Blue()
        else:
            raise InvalidColorException('unknown color: {0}'.format(color))

    def get_shape(self, shape):
        raise 'use shape factory'


class FactoryProducer(object):
    @staticmethod
    def get_factory(factory_name):
        factory_name = factory_name.lower()
        if factory_name == 'shape':
            return ShapeFactory()
        elif factory_name == 'color':
            return ColorFactory()
        else:
            raise InvalidFactoryException('unknown factory specified')


class InvalidFactoryException(Exception):
    pass


class InvalidColorException(Exception):
    pass


class InvalidShapeException(Exception):
    pass
