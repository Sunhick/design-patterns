class AnimalWorld(object):
    def __init__(self, factory):
        self._herbivore = factory.create_herbivore()
        self._carnivore = factory.create_carnivore()

    def run_food_chain(self):
        self._carnivore.eat(self._herbivore)
