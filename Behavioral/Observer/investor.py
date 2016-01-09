"""
investor.py
"""

from abc import ABCMeta, abstractmethod

class Investor(object):
    """ Investor """
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(stock):
        pass

class ConcreteInvestor(Investor):
    """ concrete investor """
    def __init__(self, name):
        self._name = name
        self._stock = None

    def update(self, stock):
        print('Notified {} of {}s change to {}'.
              format(self._name, stock.Symbol, stock.Price))

    @property
    def Stock(self):
        return self._stock

    @Stock.setter
    def Stock(self, stock):
        self._stock = stock
