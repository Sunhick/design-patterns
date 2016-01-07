"""
VicePresident.py

"""

from Approver import Approver

class VicePresident(Approver):
    """ Vice President """

    def process_request(self, purchase):
        if purchase.Amount < 25000.0:
            print('{} approved request# {}'
                  .format(type(self).__name__, purchase.Number))
        elif self._successor:
            self._successor.process_request(purchase)
        else:
            print('Vice President says: Request# %d requires an executive meeting!' % purchase.Number)
