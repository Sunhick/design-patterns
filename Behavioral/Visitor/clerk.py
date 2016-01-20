"""
clerk.py

"""

from employee import Employee

class Clerk(Employee):
    """ clerk """
    def __init__(self):
        super(Clerk, self).__init__('Hank', 25000.0, 14)
