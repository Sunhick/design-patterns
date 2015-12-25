from ContinentFactory import ContinentFactory
from Animals import Wildebeest, Lion


class AfricaFactory(ContinentFactory):
    def create_herbivore(self):
        return Wildebeest()

    def create_carnivore(self):
        return Lion()
