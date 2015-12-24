#!/usr/bin/python

import sys
import unittest
from LoadBalancer import LoadBalancer


class LoadBalancerTest(unittest.TestCase):
    """
    Singleton tester
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_singleton(self):
        b1 = LoadBalancer()
        b2 = LoadBalancer()
        self.assertEqual(id(b1), id(b2),
                         'Not the same instances. Singleton violation')


def main(*argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
