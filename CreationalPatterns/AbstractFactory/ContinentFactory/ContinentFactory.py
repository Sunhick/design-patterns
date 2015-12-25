from abc import ABCMeta, abstractmethod


class ContinentFactory(object):
    """Continent factory interface"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_herbivore(self):
        pass

    @abstractmethod
    def create_carnivore(self):
        pass
