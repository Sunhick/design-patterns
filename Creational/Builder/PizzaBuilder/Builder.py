from Pizza import Pizza
from abc import ABCMeta, abstractmethod


class PizzaBuilder(object):
    """ Abstract Pizza builder """
    __metaclass__ = ABCMeta

    @abstractmethod
    def build_toppings(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_dough(self):
        pass

    def create_pizza(self):
        self._pizza = Pizza()

    @property
    def Pizza(self):
        return self._pizza


class HawaiianPizzaBuilder(PizzaBuilder):
    """ Hawaiian Pizza Builder  """
    def build_dough(self):
        self._pizza.Dough = 'cross'

    def build_toppings(self):
        self._pizza.Toppings = 'ham, pineapple'

    def build_sauce(self):
        self._pizza.Sauce = 'mild'


class SpicyPizzaBuilder(PizzaBuilder):
    """ Spicy Pizza Builder  """
    def build_dough(self):
        self._pizza.Dough = 'pan baked'

    def build_toppings(self):
        self._pizza.Toppings = 'pepperoni, salami'

    def build_sauce(self):
        self._pizza.Sauce = 'hot'
