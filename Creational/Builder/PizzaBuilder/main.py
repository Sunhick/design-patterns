#!/usr/bin/python

import sys
from Cook import Cook
from Builder import HawaiianPizzaBuilder, SpicyPizzaBuilder


def main(*argv):
    cook = Cook()
    cook.make_pizza(HawaiianPizzaBuilder())
    cook.open_pizza()

    cook.make_pizza(SpicyPizzaBuilder())
    cook.open_pizza()

if __name__ == '__main__':
    main(sys.argv)
