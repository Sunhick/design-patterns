#!/usr/bin/python

from abc import ABCMeta, abstractmethod


class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('Drawing {shape}'.format(shape=type(self).__name__))
 

class Rectangle(Shape):
    def draw(self):
        print('Drawing {shape}'.format(shape=type(self).__name__))


class Square(Shape):
    def draw(self):
        print('Drawing {shape}'.format(shape=type(self).__name__))
