"""
President.py

"""

from Approver import Approver

class President(Approver):
    """ Vice President """

    def process_request(self, purchase):
        if purchase.Amount < 100000.0:
            print('{} approved request# {}'
                  .format(type(self).__name__, purchase.Number))
        elif self._successor:
            self._successor.process_request(purchase)
        else:
            print('Presient says: Request# %d requires an executive meeting!' % purchase.Number)
