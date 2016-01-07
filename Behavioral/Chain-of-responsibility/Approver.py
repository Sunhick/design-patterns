"""
Approver.py
"""

from abc import ABCMeta, abstractmethod


class Approver(object):
    """ Approver class """
    __metaclass__ = ABCMeta

    def __init__(self):
        self._successor = None

    def setsuccessor(self, successor):
        self._successor = successor

    @abstractmethod
    def process_request(self, purchase):
        pass
