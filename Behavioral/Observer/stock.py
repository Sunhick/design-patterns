"""
stock.py
"""

from abc import ABCMeta, abstractmethod

class Stock(object):
    """ Stock """
    __metaclass__ = ABCMeta

    def __init__(self, symbol, price):
        self._symbol = symbol
        self._price = price
        self._investors = []

    def attach(self, investor):
        self._investors.append(investor)

    def detach(self, investor):
        self._investors.remove(investor)

    def notify(self):
        for investor in self._investors:
            investor.update(self)

        print('')

    @property
    def Price(self):
        return self._price

    @Price.setter
    def Price(self, price):
        if self._price != price:
            self._price = price
            self.notify()

    @property
    def Symbol(self):
        return self._symbol
