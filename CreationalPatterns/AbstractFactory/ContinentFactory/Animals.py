from Herbivore import Herbivore
from Carnivore import Carnivore


class Wildebeest(Herbivore):
    """Wilde beest"""
    pass


class Bison(Herbivore):
    """Bison"""
    pass


class Lion(Carnivore):
    """Lion"""
    def eat(self, herbivore):
        print('{0} eats {1}'.format(
            type(self).__name__, type(herbivore).__name__))


class Wolf(Carnivore):
    """Wolf"""
    def eat(self, herbivore):
        print('{0} eats {1}'.format(
            type(self).__name__, type(herbivore).__name__))
