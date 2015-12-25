#!/usr/bin//python

import sys
from AfricaFactory import AfricaFactory
from AmericaFactory import AmericaFactory
from AnimalWorld import AnimalWorld


def main(argv):
    africa = AfricaFactory()
    animalWorld = AnimalWorld(africa)
    animalWorld.run_food_chain()

    america = AmericaFactory()
    animalWorld = AnimalWorld(america)
    animalWorld.run_food_chain()

if __name__ == '__main__':
    main(sys.argv)
