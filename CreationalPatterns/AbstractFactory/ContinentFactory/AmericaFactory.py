from ContinentFactory import ContinentFactory
from Animals import Bison, Wolf


class AmericaFactory(ContinentFactory):
    """America factory class"""
    def create_herbivore(self):
        return Bison()

    def create_carnivore(self):
        return Wolf()

