"""
CalculatorCommand.py

"""

from Command import Command


class CalculatorCommand(Command):
    def __init__(self, calc, operator, operand):
        self._operator = operator
        self._operand = operand
        self._calc = calc

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        self._operator = operator

    def execute(self):
        self._calc.operation(self.operator, self._operand)

    def unexecute(self):
        self._calc.operation(self.undo(self.operator), self._operand)

    def undo(self, operator):
        if operator == '*':
            return '/'
        elif operator == '/':
            return '*'
        elif operator == '+':
            return '-'
        elif operator == '-':
            return '+'
        else:
            raise Exception('unknown operator: {op}'.format(op=operator))
