"""
User.py

"""

from CalculatorCommand import CalculatorCommand
from Calculator import Calculator


class User(object):
    """ User """

    def __init__(self):
        self._calc = Calculator()
        self._cmds = []
        self._current = 0

    def redo(self, steps):
        print('undo %d levels' % steps)
        for step in range(0, steps):
            if self._current < len(self._cmds):
                cmd = self._cmds[self._current]
                cmd.execute()
                self._current += 1

    def undo(self, steps):
        print('undo %d levels' % steps)
        for step in range(0, steps):
            if self._current > 0:
                self._current -= 1
                cmd = self._cmds[self._current]
                cmd.unexecute()


    def compute(self, operator, operand):
        cmd = CalculatorCommand(self._calc, operator, operand)
        cmd.execute()

        self._cmds.append(cmd)
        self._current += 1
