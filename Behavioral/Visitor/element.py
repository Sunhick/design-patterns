"""
element.py

"""

from abc import ABCMeta, abstractmethod

class Element(object):
    """
    Element class
    """
    @abstractmethod
    def accept(self, visitor):
        pass
