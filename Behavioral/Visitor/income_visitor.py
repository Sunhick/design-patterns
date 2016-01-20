"""
income visitor

"""

from visitor import Visitor

class IncomeVisitor(Visitor):
    """
    Income visitor
    """
    def visit(self, employee):
        # provide 10% raise
        employee.Income *= 1.10
        print("{0} {1}'s new income: {2}".
              format(type(employee).__name__, employee.Name, employee.Income))
