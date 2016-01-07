"""
main.py
"""

import sys

from Director import Director
from VicePresident import VicePresident
from President import President
from Purchase import Purchase

def main(*argv):
    larry = Director()
    sam = VicePresident()
    tammy = President()

    larry.setsuccessor(sam)
    sam.setsuccessor(tammy)

    p = Purchase(2034, 350.00, "Assets");
    larry.process_request(p);

    p = Purchase(2035, 32590.10, "Project X");
    larry.process_request(p);

    p = Purchase(2036, 122100.00, "Project Y");
    larry.process_request(p);


if __name__ == '__main__':
    main(sys.argv)
