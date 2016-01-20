"""
visitor.py

"""

from abc import ABCMeta, abstractmethod

class Visitor(object):
    """
    Visitor interface class
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def visit(self, element):
        pass
