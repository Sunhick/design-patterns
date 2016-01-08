"""
Calculator.py

"""

class Calculator(object):
    def __init__(self):
        self._answer = float(0)

    def operation(self, operator, operand):
        if operator == '+':
            self._answer += operand
        elif operator == '-':
            self._answer -= operand
        elif operator == '*':
            self._answer *= operand
        elif operator == '/':
            self._answer /= operand

        print('Current value = {} (following {} {})'.format(self._answer, operator, operand))
