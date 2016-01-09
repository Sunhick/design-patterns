"""
IBM.py
"""

from stock import Stock

class IBM(Stock):
    """ IBM stock """
    def __init__(self, symbol, price):
        Stock.__init__(self, symbol, price)
