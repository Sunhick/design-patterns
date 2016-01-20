"""
director.py

"""

from employee import Employee

class Director(Employee):
    """ Director """
    def __init__(self):
        super(Director, self).__init__('Elly', 35000.0, 16)
