#!/usr/bin/python

from abc import ABCMeta, abstractmethod


class Color(object):
    """color interface"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def fill(self):
        pass


class Red(Color):
    """Represents Red color"""
    def fill(self):
        print('Color is {color}'.format(color=type(self).__name__))


class Green(Color):
    """Green color"""
    def fill(self):
        print('Color is {color}'.format(color=type(self).__name__))


class Blue(Color):
    """Blue color"""
    def fill(self):
        print('Color is {color}'.format(color=type(self).__name__))
