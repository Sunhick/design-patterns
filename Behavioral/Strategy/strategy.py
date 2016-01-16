"""
sort strategy interface
"""

from abc import ABCMeta, abstractmethod

class SortStrategy(object):
    """ Sorting strategy """
    __metaclass__ = ABCMeta

    @abstractmethod
    def sort(self, elements):
        pass
