"""
Director.py

"""

from Approver import Approver

class Director(Approver):
    """ Director """

    def process_request(self, purchase):
        if purchase.Amount < 10000.0:
            print('{} approved request# {}'
                  .format(type(self).__name__, purchase.Number))
        elif self._successor:
            self._successor.process_request(purchase)
        else:
            print('Director says: Request# %d requires an executive meeting!' % purchase.Number)
