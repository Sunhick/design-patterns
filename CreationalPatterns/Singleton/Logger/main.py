#!/usr/bin/python

import sys
from Logger import LogManager


def main(*argv):
    logger = LogManager.get_logger()
    for i in range(0, 50):
        logger.log('ERROR', 'This is error message -- 1')
        logger.log('WARN', ' This is warning message -- 1')
        logger.log('DEBUG', 'This is debug message -- 1')
        logger.log('FATAL', 'This is fatal message -- 1')
        logger.log('INFO', ' This is information message -- 1')

    logger2 = LogManager.get_logger()
    for i in range(0, 50):
        logger2.log('ERROR', 'This is error message -- 2')
        logger2.log('WARN', ' This is warning message -- 2')
        logger2.log('DEBUG', 'This is debug message -- 2')
        logger2.log('FATAL', 'This is fatal message -- 2')
        logger2.log('INFO', ' This is information message -- 2')

    if not id(logger) == id(logger2):
        print('Two loggers are different instances! Singleton violation')
    else:
        print('Two logger instances are same! Singleton')


if __name__ == '__main__':
    main(sys.argv)
