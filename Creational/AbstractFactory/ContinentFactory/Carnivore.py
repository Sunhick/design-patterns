from abc import ABCMeta, abstractmethod


class Carnivore(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def eat(self, herbivore):
        pass
