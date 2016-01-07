"""
Purchase.py
"""

class Purchase(object):
    """
    class holding request details
    """
    def __init__(self, number, amount, purpose):
        self._number = number
        self._amount = amount
        self._purpose = purpose

    @property
    def Number(self):
        return self._number

    @Number.setter
    def Number(self, number):
        self._number = Number

    @property
    def Amount(self):
        return self._amount

    @Amount.setter
    def Amount(self, amount):
        self._amount = amount

    @property
    def Purpose(self):
        return self._purpose

    @Purpose.setter
    def Purpose(self, purpose):
        return self._purpose
