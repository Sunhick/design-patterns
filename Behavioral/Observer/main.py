#!/usr/bin/python

"""
main.py

"""

import sys
from ibm import IBM
from investor import ConcreteInvestor

def main(*argv):
    #Create IBM stock and attach investors
    ibm = IBM('IBM', 120.00);
    ibm.attach(ConcreteInvestor('Sorros'));
    ibm.attach(ConcreteInvestor('Berkshire'));

    # Fluctuating prices will notify investors
    ibm.Price = 120.10;
    ibm.Price = 121.00;
    ibm.Price = 120.50;
    ibm.Price = 120.75;


if __name__ == '__main__':
    main(sys.argv)
