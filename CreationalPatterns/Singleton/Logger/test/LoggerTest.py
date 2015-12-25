#!/usr/bin/python

import sys
import unittest
from Logger import LogManager


class LoggerTest(unittest.TestCase):
    """
    Singleton tester
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_singleton(self):
        log1 = LogManager.get_logger()
        for i in range(0, 50):
            log1.log('ERROR', 'This is error message -- 1')
            log1.log('WARN', ' This is warning message -- 1')
            log1.log('DEBUG', 'This is debug message -- 1')

        log2 = LogManager.get_logger()
        for i in range(0, 50):
            log2.log('ERROR', 'This is error message -- 1')
            log2.log('WARN', ' This is warning message -- 1')
            log2.log('DEBUG', 'This is debug message -- 1')

        self.assertEqual(id(log1), id(log2),
                         'Not the same instances. Singleton violation')


def main(*argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
