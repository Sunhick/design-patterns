"""
Employee.py

"""

from element import Element

class Employee(Element):
    """
    Employee class
    """

    def __init__(self, name, income, vacation_days):
        self._name = name
        self._income = income
        self._vacation_days = vacation_days

    def accept(visitor):
        visitor.visit(self)

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    @property
    def Income(self):
        return self._income

    @Income.setter
    def Income(self, income):
        self._income = income

    @property
    def VacationDays(self):
        return self._vacation_days

    @VacationDays.setter
    def VacationDays(self, days):
        self._vacation_days = days
