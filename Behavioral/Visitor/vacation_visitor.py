"""
vacation visitor

"""

from visitor import Visitor

class VacationVisitor(Visitor):
    """
    vacation visitor
    """
    def visit(self, employee):
        # provide 3 extra vacation days
        employee.VacationDays += 3
        print("{0} {1}'s new vacation days: {2}".
              format(type(employee).__name__, employee.Name, employee.VacationDays))
