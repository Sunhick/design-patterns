#!/usr/bin/python

"""
main.py
"""

import sys

from employees import Employees
from clerk import Clerk
from director import Director
from president import President
from income_visitor import IncomeVisitor
from vacation_visitor import VacationVisitor

def main(*argv):
    employees = Employees()
    employees.add(Clerk())
    employees.add(Director())
    employees.add(President())

    employees.accept(IncomeVisitor())
    employees.accept(VacationVisitor())

if __name__ == '__main__':
    main(sys.argv)
