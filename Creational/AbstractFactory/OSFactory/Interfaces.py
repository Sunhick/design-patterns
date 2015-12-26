#!/usr/bin/python

from abc import ABCMeta, abstractmethod


class Button(object):
    """ Interface for button object """
    __metaclass__ = ABCMeta

    @abstractmethod
    def paint(self):
        pass


class Label(object):
    """ Interface for Label object """
    __metaclass__ = ABCMeta

    _name = ''

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    @abstractmethod
    def paint(self):
        pass


class WindowFrame(object):
    """ Interface for window frame """
    __metaclass__ = ABCMeta

    def __init__(self):
        self._elements = []

    def add(self, element):
        self._elements.append(element)

    def show(self):
        # paint window frame and then all it's
        # elements/children inside it.
        self.paint()
        for e in self._elements:
            e.paint()

    @abstractmethod
    def paint(self):
        pass


class GuiFactory(object):
    """ Interface for Gui factory """
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_label(self, name):
        pass
