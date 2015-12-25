#!/usr/bin/python

import sys
import unittest
from Cook import Cook
from Builder import HawaiianPizzaBuilder, SpicyPizzaBuilder


class PizzaBuilderTest(unittest.TestCase):
    """
    Pizza Builder tester
    """
    def setUp(self):
        self._cook = Cook()

    def tearDown(self):
        pass

    def test_hawaiian_builder(self):
        self._cook.make_pizza(HawaiianPizzaBuilder())
        self.assertEqual(self._cook.Pizza.Toppings, 'ham, pineapple',
                         'Not a Hawaiian Pizza')
        self.assertEqual(self._cook.Pizza.Sauce, 'mild',
                         'Not a Hawaiian Pizza')
        self.assertEqual(self._cook.Pizza.Dough, 'cross',
                         'Not a Hawaiian Pizza')

    def test_spicy_builder(self):
        self._cook.make_pizza(SpicyPizzaBuilder())
        self.assertEqual(self._cook.Pizza.Toppings, 'pepperoni, salami',
                         'Not a Spicy Pizza')
        self.assertEqual(self._cook.Pizza.Sauce, 'hot', 'Not a Spicy Pizza')
        self.assertEqual(self._cook.Pizza.Dough, 'pan baked',
                         'Not a Spicy Pizza')


def main(*argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
