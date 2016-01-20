"""
Employees.py

"""


class Employees:
    """
    Employees class
    """

    def __init__(self):
        self._employees = []

    def add(self, employee):
        self._employees.append(employee)

    def remove(self, employee):
        self._employees.remove(employee)

    def accept(self, visitor):
        for employee in self._employees:
            visitor.visit(employee)
