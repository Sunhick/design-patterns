class Pizza(object):
    """ Represents a pizza class"""
    def __init__(self):
        self._sauce = ''
        self._dough = ''
        self._toppings = ''

    @property
    def Sauce(self):
        return self._sauce

    @Sauce.setter
    def Sauce(self, sauce):
        self._sauce = sauce

    @property
    def Dough(self):
        return self._dough

    @Dough.setter
    def Dough(self, dough):
        self._dough = dough

    @property
    def Toppings(self):
        return self._toppings

    @Toppings.setter
    def Toppings(self, toppings):
        self._toppings = toppings

    def open(self):
        print('Pizza with {dough} dough, {sauce} sauce, and {toppings} toppings. Mmm...'.format(
            dough=self._dough, sauce=self._sauce, toppings=self._toppings))
