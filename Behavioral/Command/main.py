#!/usr/bin/python

import sys
from User import User


def main(*argv):
    user = User()

    # User presses calculator buttons
    user.compute('+', 100)
    user.compute('-', 50)
    user.compute('*', 10)
    user.compute('/', 2)

    # Undo 4 commands
    user.undo(4)

    # Redo 3 commands
    user.redo(3)


if __name__ == '__main__':
    main(sys.argv)
